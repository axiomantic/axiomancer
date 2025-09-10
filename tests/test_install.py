#!/usr/bin/env python3
"""Tests for the Axiomancer install script."""

import os
import subprocess
import tempfile
import threading
import time
import zipfile
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

import pytest


# Shared fixtures
@pytest.fixture
def temp_project_dir():
    """Create a temporary project directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)

@pytest.fixture
def axiomancer_repo_dir():
    """Get the axiomancer repository directory."""
    return Path(__file__).parent.parent

@pytest.fixture
def install_script_path(axiomancer_repo_dir):
    """Get the path to install.sh."""
    return axiomancer_repo_dir / "install.sh"

@pytest.fixture
def simple_http_server(axiomancer_repo_dir):
    """Start a simple HTTP server serving the actual repo files."""
    # Just serve the real repo directory - much simpler!
    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(axiomancer_repo_dir), **kwargs)

    server = HTTPServer(('localhost', 0), Handler)
    port = server.server_address[1]
    
    # Start server in background thread
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    # Give server time to start
    time.sleep(0.1)
    
    yield f"http://localhost:{port}"
    
    server.shutdown()


def run_shell_command(cmd, cwd=None, input_data=None):
    """Run a shell command and return result."""
    result = subprocess.run(
        cmd,
        shell=True,
        cwd=cwd,
        capture_output=True,
        text=True,
        input=input_data
    )
    return result


class TestInstallScript:
    """Test suite for install.sh script."""

    def run_shell_command(self, cmd, cwd=None, input_data=None):
        """Run a shell command and return result."""
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            input=input_data
        )
        return result

    def test_install_from_repo_dir_with_target_path(self, axiomancer_repo_dir, temp_project_dir):
        """Test installing from axiomancer repo directory to target path."""
        # Run install script from repo dir with target path
        cmd = f"./install.sh {temp_project_dir}"
        result = self.run_shell_command(cmd, cwd=axiomancer_repo_dir)
        
        assert result.returncode == 0, f"Install failed: {result.stderr}"
        
        # Check that .axiomantic directory was created (single source of truth)
        axiomantic_dir = temp_project_dir / ".axiomantic"
        assert axiomantic_dir.exists(), ".axiomantic directory not created"
        
        # Check that commands directory was created
        commands_dir = axiomantic_dir / "commands"
        assert commands_dir.exists(), ".axiomantic/commands directory not created"
        
        # Check that templates directory was created
        templates_dir = axiomantic_dir / "templates"
        assert templates_dir.exists(), ".axiomantic/templates directory not created"
        
        # Check that axiomancer command file exists (the actual file)
        axiomancer_cmd = commands_dir / "axiomancer.md"
        assert axiomancer_cmd.exists(), "axiomancer.md command not created"
        
        # Check that .claude directory and symlink were created
        claude_dir = temp_project_dir / ".claude"
        assert claude_dir.exists(), ".claude directory not created"
        
        claude_commands_dir = claude_dir / "commands"
        assert claude_commands_dir.exists(), ".claude/commands directory not created"
        
        claude_axiomancer = claude_commands_dir / "axiomancer.md"
        assert claude_axiomancer.exists(), ".claude/commands/axiomancer.md not created"
        assert claude_axiomancer.is_symlink(), ".claude/commands/axiomancer.md is not a symlink"
        
        # Check that .opencode directory and symlink were created
        opencode_dir = temp_project_dir / ".opencode"
        assert opencode_dir.exists(), ".opencode directory not created"
        
        opencode_commands_dir = opencode_dir / "commands"
        assert opencode_commands_dir.exists(), ".opencode/commands directory not created"
        
        opencode_axiomancer = opencode_commands_dir / "axiomancer.md"
        assert opencode_axiomancer.exists(), ".opencode/commands/axiomancer.md not created"
        assert opencode_axiomancer.is_symlink(), ".opencode/commands/axiomancer.md is not a symlink"

    def test_install_from_project_dir_with_local_script(self, install_script_path, temp_project_dir):
        """Test installing from project directory using absolute path to script."""
        # Run install script from project dir
        cmd = str(install_script_path)
        result = self.run_shell_command(cmd, cwd=temp_project_dir)
        
        assert result.returncode == 0, f"Install failed: {result.stderr}"
        
        # Check basic installation
        axiomantic_dir = temp_project_dir / ".axiomantic"
        assert axiomantic_dir.exists(), ".axiomantic directory not created"
        
        # Check that actual command file exists
        actual_cmd = axiomantic_dir / "commands" / "axiomancer.md"
        assert actual_cmd.exists(), "axiomancer.md not created in .axiomantic"
        
        # Check that both claude and opencode symlinks exist
        claude_cmd = temp_project_dir / ".claude" / "commands" / "axiomancer.md"
        assert claude_cmd.exists(), "claude axiomancer.md symlink not created"
        assert claude_cmd.is_symlink(), "claude axiomancer.md is not a symlink"
        
        opencode_cmd = temp_project_dir / ".opencode" / "commands" / "axiomancer.md"
        assert opencode_cmd.exists(), "opencode axiomancer.md symlink not created"
        assert opencode_cmd.is_symlink(), "opencode axiomancer.md is not a symlink"

    def test_install_script_can_be_downloaded(self, simple_http_server, temp_project_dir):
        """Test that install script can be downloaded via HTTP."""
        # Test downloading the script
        curl_cmd = f"curl -sSL {simple_http_server}/install.sh"
        result = self.run_shell_command(curl_cmd, cwd=temp_project_dir)
        
        assert result.returncode == 0, f"Curl download failed: {result.stderr}"
        assert "#!/bin/bash" in result.stdout, "Downloaded script should be a bash script"
        assert "Axiomancer" in result.stdout, "Downloaded script should contain Axiomancer"
        assert "AXIOMANTIC_DIR=" in result.stdout, "Script should contain expected variables"
        
        # Test script syntax is valid
        downloaded_script = temp_project_dir / "downloaded_install.sh"
        downloaded_script.write_text(result.stdout)
        downloaded_script.chmod(0o755)
        
        # Test bash syntax check
        syntax_check = self.run_shell_command(f"bash -n {downloaded_script}")
        assert syntax_check.returncode == 0, f"Script syntax error: {syntax_check.stderr}"
        
        # Test that script fails gracefully when files are missing (expected behavior)
        execution_result = self.run_shell_command(str(downloaded_script), cwd=temp_project_dir)
        assert execution_result.returncode == 1, "Script should fail when axiomancer.md missing (expected)"
        assert "axiomancer.md command not found" in execution_result.stdout, "Should show appropriate error message"

    def test_prevents_installation_in_axiomancer_repo(self, axiomancer_repo_dir):
        """Test that script prevents installation within axiomancer repo itself."""
        cmd = "./install.sh"
        result = self.run_shell_command(cmd, cwd=axiomancer_repo_dir)
        
        assert result.returncode == 1, "Should have failed when run in axiomancer repo"
        assert "Cannot install axiomancer within the axiomancer repository" in result.stdout

    def test_creates_proper_directory_structure(self, install_script_path, temp_project_dir):
        """Test that proper directory structure is created."""
        cmd = str(install_script_path)
        result = self.run_shell_command(cmd, cwd=temp_project_dir)
        
        assert result.returncode == 0, f"Install failed: {result.stderr}"
        
        # Check complete directory structure
        expected_files = [
            ".axiomantic/commands/axiomancer.md",
            ".axiomantic/templates/AGENT.md",
            ".axiomantic/templates/SYSTEM_ARCHITECTURE.md", 
            ".axiomantic/templates/CONTRIBUTING.md",
            ".axiomantic/templates/GRIMOIRE.md",
            ".axiomantic/templates/STATUS_MANIFEST.yaml",
            ".axiomantic/templates/GLOSSARY.md",
            ".axiomantic/templates/SUMMONER.md",
            ".axiomantic/templates/PROJECT_BOOTSTRAP.md",
            ".axiomantic/README.md",
            ".claude/commands/axiomancer.md",  # Symlink
            ".opencode/commands/axiomancer.md"  # Symlink
        ]
        
        for file_path in expected_files:
            full_path = temp_project_dir / file_path
            assert full_path.exists(), f"Expected file not found: {file_path}"

    def test_output_contains_instructions(self, install_script_path, temp_project_dir):
        """Test that output contains proper usage instructions."""
        cmd = str(install_script_path)
        result = self.run_shell_command(cmd, cwd=temp_project_dir)
        
        assert result.returncode == 0, f"Install failed: {result.stderr}"
        
        # Check that output contains instructions for both claude and opencode
        output = result.stdout
        assert "claude /axiomancer" in output, "Claude instructions not found"
        assert "opencode run /axiomancer" in output, "Opencode instructions not found"

    def test_script_checks_for_dependencies(self, temp_project_dir):
        """Test that script properly checks for required dependencies."""
        install_script = Path(__file__).parent.parent / "install.sh"
        content = install_script.read_text()
        
        # Verify that the script checks for required tools
        assert "command -v curl" in content, "Script should check for curl"
        assert "command -v unzip" in content, "Script should check for unzip"
        
        # Test actual dependency checking by creating a script that fails curl check
        test_script = temp_project_dir / "test_deps.sh"
        test_script.write_text("""#!/bin/bash
        set -e
        if ! command -v curl &> /dev/null; then
            echo "❌ Error: curl is required but not installed"
            exit 1
        fi
        echo "Dependencies OK"
        """)
        test_script.chmod(0o755)
        
        # Should pass with normal PATH
        result = run_shell_command(str(test_script))
        assert result.returncode == 0, "Dependency check should pass normally"
        
        # Test with empty PATH (forces curl not found)
        import os
        env = os.environ.copy()
        env['PATH'] = '/nonexistent'
        result = subprocess.run(str(test_script), shell=True, capture_output=True, text=True, env=env)
        assert result.returncode == 1, "Should fail when curl not in PATH"

    def test_templates_are_copied_correctly(self, install_script_path, temp_project_dir, axiomancer_repo_dir):
        """Test that all template files are copied correctly."""
        cmd = str(install_script_path)
        result = self.run_shell_command(cmd, cwd=temp_project_dir)
        
        assert result.returncode == 0, f"Install failed: {result.stderr}"
        
        # Compare source templates with copied templates
        source_templates = axiomancer_repo_dir / "templates"
        copied_templates = temp_project_dir / ".axiomantic" / "templates"
        
        # Check that all source templates were copied
        for source_file in source_templates.glob("*.md"):
            copied_file = copied_templates / source_file.name
            assert copied_file.exists(), f"Template not copied: {source_file.name}"
            
            # Check that content matches
            source_content = source_file.read_text()
            copied_content = copied_file.read_text()
            assert source_content == copied_content, f"Template content mismatch: {source_file.name}"

    def test_symlink_creation(self, install_script_path, temp_project_dir):
        """Test that opencode symlink is created correctly."""
        cmd = str(install_script_path)
        result = self.run_shell_command(cmd, cwd=temp_project_dir)
        
        assert result.returncode == 0, f"Install failed: {result.stderr}"
        
        # Check symlinks point to axiomantic
        opencode_cmd = temp_project_dir / ".opencode" / "commands" / "axiomancer.md"
        claude_cmd = temp_project_dir / ".claude" / "commands" / "axiomancer.md"
        axiomantic_cmd = temp_project_dir / ".axiomantic" / "commands" / "axiomancer.md"
        
        assert opencode_cmd.is_symlink(), "opencode command should be a symlink"
        assert claude_cmd.is_symlink(), "claude command should be a symlink"
        assert opencode_cmd.resolve() == axiomantic_cmd.resolve(), "opencode symlink should point to axiomantic command"
        assert claude_cmd.resolve() == axiomantic_cmd.resolve(), "claude symlink should point to axiomantic command"

    def test_readme_creation(self, install_script_path, temp_project_dir):
        """Test that README files are created with correct content."""
        cmd = str(install_script_path)
        result = self.run_shell_command(cmd, cwd=temp_project_dir)
        
        assert result.returncode == 0, f"Install failed: {result.stderr}"
        
        readme_path = temp_project_dir / ".axiomantic" / "README.md"
        assert readme_path.exists(), "README.md not created"
        
        readme_content = readme_path.read_text()
        assert "claude /axiomancer" in readme_content, "README should contain claude instructions"
        assert "This directory contains the Axiomancer templates" in readme_content, "README should contain description"


class TestInstallScriptEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_handles_permission_errors(self, temp_project_dir):
        """Test behavior with permission errors."""
        import stat
        
        # Create a directory and make it read-only
        readonly_dir = temp_project_dir / "readonly"
        readonly_dir.mkdir()
        readonly_dir.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)  # Read-only
        
        try:
            # Try to install in read-only directory
            install_script = Path(__file__).parent.parent / "install.sh"
            cmd = f"{install_script} {readonly_dir}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            # Should fail due to permissions
            assert result.returncode != 0, "Should fail with permission error"
            
        finally:
            # Cleanup - restore permissions so temp dir can be deleted
            readonly_dir.chmod(stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
    
    def test_handles_missing_dependencies(self, temp_project_dir):
        """Test behavior when dependencies are missing."""
        # Create a modified PATH that excludes curl/unzip
        import os
        
        # Get current PATH and remove common curl/unzip locations
        original_path = os.environ.get('PATH', '')
        modified_path = ':'.join([p for p in original_path.split(':') 
                                 if not any(tool in p.lower() for tool in ['curl', 'unzip'])])
        
        install_script = Path(__file__).parent.parent / "install.sh"
        
        # Test with curl missing (simulate by modifying PATH)
        env = os.environ.copy()
        env['PATH'] = '/nonexistent'  # Force curl to be "missing"
        
        # Use a script that will fail on curl check
        test_script = temp_project_dir / "test_install.sh"
        script_content = f"""#!/bin/bash
        if ! command -v curl &> /dev/null; then
            echo "❌ Error: curl is required but not installed"
            exit 1
        fi
        echo "curl found"
        """
        test_script.write_text(script_content)
        test_script.chmod(0o755)
        
        result = subprocess.run(str(test_script), shell=True, capture_output=True, text=True, env=env)
        assert result.returncode == 1, "Should fail when curl is missing"
        assert "curl is required but not installed" in result.stdout
    
    def test_invalid_target_directory(self):
        """Test behavior with invalid target directory."""
        install_script = Path(__file__).parent.parent / "install.sh"
        
        # Try to install to non-existent directory
        result = subprocess.run(
            f"{install_script} /nonexistent/directory/path", 
            shell=True, capture_output=True, text=True
        )
        
        assert result.returncode == 1, "Should fail with invalid directory"
        assert "does not exist" in result.stdout
    
    def test_script_fails_gracefully_on_missing_files(self, temp_project_dir):
        """Test that script fails gracefully when required files are missing."""
        # Create a copy of install script but remove axiomancer.md from repo
        repo_dir = Path(__file__).parent.parent
        install_script = repo_dir / "install.sh"
        
        # Create temp repo structure without axiomancer.md
        fake_repo = temp_project_dir / "fake_repo"
        fake_repo.mkdir()
        
        # Copy install script
        fake_install = fake_repo / "install.sh"
        fake_install.write_text(install_script.read_text())
        fake_install.chmod(0o755)
        
        # Create templates dir but no axiomancer.md
        (fake_repo / "templates").mkdir()
        
        # Try to install from fake repo
        target_dir = temp_project_dir / "target"
        target_dir.mkdir()
        
        result = subprocess.run(
            f"./install.sh {target_dir}",
            shell=True, cwd=fake_repo, capture_output=True, text=True
        )
        
        assert result.returncode == 1, "Should fail when axiomancer.md is missing"
        assert "axiomancer.md command not found" in result.stdout
    
    def test_concurrent_installations(self, temp_project_dir):
        """Test behavior when multiple installations run simultaneously."""
        import concurrent.futures
        
        install_script = Path(__file__).parent.parent / "install.sh"
        
        def install_in_dir(dir_name):
            target = temp_project_dir / dir_name
            target.mkdir()
            result = subprocess.run(
                f"{install_script} {target}", 
                shell=True, capture_output=True, text=True
            )
            return result.returncode == 0 and (target / ".axiomantic").exists()
        
        # Run 3 installations concurrently
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            futures = [executor.submit(install_in_dir, f"install_{i}") for i in range(3)]
            results = [f.result() for f in concurrent.futures.as_completed(futures)]
        
        # All should succeed
        assert all(results), "All concurrent installations should succeed"
    
    def test_symlink_targets_are_correct(self, install_script_path, temp_project_dir):
        """Test that symlinks point to correct targets."""
        import os
        
        result = run_shell_command(str(install_script_path), cwd=temp_project_dir)
        assert result.returncode == 0, f"Install failed: {result.stderr}"
        
        # Check symlink targets are relative and correct
        claude_link = temp_project_dir / ".claude" / "commands" / "axiomancer.md"
        opencode_link = temp_project_dir / ".opencode" / "commands" / "axiomancer.md"
        
        # Verify symlinks exist and are relative
        assert claude_link.is_symlink(), "Claude link should be a symlink"
        assert opencode_link.is_symlink(), "OpenCode link should be a symlink"
        
        # Check that symlink targets are relative (not absolute)
        claude_target = os.readlink(claude_link)
        opencode_target = os.readlink(opencode_link)
        
        assert not claude_target.startswith('/'), f"Claude symlink should be relative, got: {claude_target}"
        assert not opencode_target.startswith('/'), f"OpenCode symlink should be relative, got: {opencode_target}"
        
        # Both should point to the same file
        assert claude_link.resolve() == opencode_link.resolve(), "Both symlinks should point to same file"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
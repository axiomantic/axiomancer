#!/bin/bash

# Axiomancer Installation Script
# Installs axiomancer templates and prompt in current directory
# Can be run locally or via: curl -sSL https://raw.githubusercontent.com/axiomantic/axiomancer/main/install.sh | bash

set -e  # Exit on any error

AXIOMANTIC_DIR=".axiomantic"
CLAUDE_DIR=".claude"
OPENCODE_DIR=".opencode"
GITHUB_REPO="axiomantic/axiomancer"
GITHUB_BRANCH="main"

# Handle command line arguments
if [[ $# -gt 0 ]]; then
    TARGET_DIR="$1"
    if [[ ! -d "$TARGET_DIR" ]]; then
        echo "❌ Error: Target directory '$TARGET_DIR' does not exist"
        exit 1
    fi
else
    TARGET_DIR="$PWD"
fi

# Store original working directory for relative path calculations
ORIGINAL_DIR="$PWD"

echo "🧙‍♂️ Installing Axiomancer to: $TARGET_DIR"

# Check if we're in the axiomancer repository itself (only if no target specified)
if [[ $# -eq 0 ]] && [[ "$(basename "$PWD")" == "axiomancer" ]] && [[ -f "install.sh" ]]; then
    echo "❌ Error: Cannot install axiomancer within the axiomancer repository itself"
    echo "   Please run this script from your target project directory, or specify a target:"
    echo "   ./install.sh /path/to/your/project"
    exit 1
fi

# Determine if we're running locally or from curl
if [[ -n "${BASH_SOURCE[0]}" ]] && [[ -f "${BASH_SOURCE[0]}" ]]; then
    # Running locally
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    LOCAL_MODE=true
    echo "📍 Running in local mode from $SCRIPT_DIR"
else
    # Running from curl pipe
    LOCAL_MODE=false
    TEMP_DIR=$(mktemp -d)
    SCRIPT_DIR="$TEMP_DIR/axiomancer-$GITHUB_BRANCH"

    echo "📥 Downloading axiomancer from GitHub..."

    # Check for required tools
    if ! command -v curl &> /dev/null; then
        echo "❌ Error: curl is required but not installed"
        exit 1
    fi

    if ! command -v unzip &> /dev/null; then
        echo "❌ Error: unzip is required but not installed"
        exit 1
    fi

    # Download and extract
    cd "$TEMP_DIR"
    curl -sSL "https://github.com/$GITHUB_REPO/archive/refs/heads/$GITHUB_BRANCH.zip" -o axiomancer.zip
    unzip -q axiomancer.zip
    cd - > /dev/null

    echo "✅ Downloaded axiomancer successfully"
fi

# Create directory structures
echo "📁 Creating Axiomantic directory structure..."
mkdir -p "$TARGET_DIR/$AXIOMANTIC_DIR/commands"
mkdir -p "$TARGET_DIR/$AXIOMANTIC_DIR/templates"
mkdir -p "$TARGET_DIR/$CLAUDE_DIR/commands"
mkdir -p "$TARGET_DIR/$OPENCODE_DIR/commands"

# Copy axiomancer command to axiomantic directory
echo "📋 Copying axiomancer command..."
if [[ -f "$SCRIPT_DIR/axiomancer.md" ]]; then
    cp "$SCRIPT_DIR/axiomancer.md" "$TARGET_DIR/$AXIOMANTIC_DIR/commands/axiomancer.md"
else
    echo "❌ Error: axiomancer.md command not found"
    exit 1
fi

# Copy templates to axiomantic directory
echo "📄 Copying templates..."
if [[ -d "$SCRIPT_DIR/templates" ]]; then
    cp -r "$SCRIPT_DIR/templates/"* "$TARGET_DIR/$AXIOMANTIC_DIR/templates/"
else
    echo "❌ Error: templates directory not found at $SCRIPT_DIR/templates"
    exit 1
fi

# Create symlinks from claude and opencode to axiomantic
echo "🔗 Creating Claude and OpenCode symlinks..."
cd "$TARGET_DIR"
ln -sf "../../$AXIOMANTIC_DIR/commands/axiomancer.md" "$CLAUDE_DIR/commands/axiomancer.md"
ln -sf "../../$AXIOMANTIC_DIR/commands/axiomancer.md" "$OPENCODE_DIR/commands/axiomancer.md"
cd "$ORIGINAL_DIR"

# Clean up temporary directory if we downloaded
if [[ "$LOCAL_MODE" == false ]]; then
    echo "🧹 Cleaning up temporary files..."
    rm -rf "$TEMP_DIR"
fi

# Create usage instructions
cat > "$TARGET_DIR/$AXIOMANTIC_DIR/README.md" << 'EOF'
# Axiomancer Installation

This directory contains the Axiomancer templates and prompts for your project.

## Usage

### Bootstrap a New Project
```bash
claude /axiomancer
# Then: "create ProjectName" or "bootstrap web application"
```

### Organize an Existing Project
```bash
claude /axiomancer
# Then: "organize this project" or "bring order to this codebase"
```

### After Initialization
Once your project is bootstrapped/organized, use:
```bash
claude --prompt AGENT.md
# Then: "summon component-name" to implement specific components
```

## Cleanup

After successful bootstrap/organization, the Axiomancer will automatically clean up the `.axiomantic/` directory and associated symlinks to keep your project clean.

EOF

echo ""
echo "✅ Axiomancer installed successfully!"
echo ""
echo "🚀 To bootstrap/organize your project:"
echo ""
echo "   claude /axiomancer"
echo "   # or"
echo "   opencode run /axiomancer"
echo ""
echo "💬 Available commands:"
echo "   • For NEW projects: 'create ProjectName' or 'bootstrap web application'"
echo "   • For EXISTING projects: 'organize this project' or 'bring order to this codebase'"
echo ""
echo "📚 Note: Installation directories will be automatically cleaned up after successful bootstrap."
echo ""

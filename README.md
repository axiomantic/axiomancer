# Axiomancer: Project Template System

A comprehensive template system for bootstrapping high-quality software projects with systematic development workflows and intelligent AI coding assistant integration.

## Overview

Axiomancer is a complete project lifecycle tool that both **bootstraps new software projects from scratch** and **brings order to existing projects**. For new projects, it guides you through conception, technology selection, and complete project setup with industry best practices. For existing projects, it analyzes your codebase and creates a systematic development environment - giving you structured workflows, component tracking, quality gates, and a project-aware AI coding assistant that understands your specific architecture and patterns.

## Philosophy

**From chaos to order, from undocumented to systematic, from isolated to integrated.**

Axiomancer embodies the principle that excellent software emerges from:
- **Systematic Architecture**: Clear structural principles and component relationships
- **Rigorous Development**: Test-driven development with comprehensive validation
- **Quality Focus**: Uncompromising standards for code quality and maintainability
- **Effective Documentation**: Living documentation that actually helps developers

## The Template System

### Core Templates

**`templates/AGENT.md`**  
System prompt template for coding assistants, incorporating the **Five Pillars of Excellence**: Precision, Elegance, Robustness, Quality, and Wisdom.

**`templates/SYSTEM_ARCHITECTURE.md`**  
Comprehensive architectural documentation template covering philosophy, component design, data architecture, quality assurance, and evolution strategy.

**`templates/CONTRIBUTING.md`**  
Development workflow template implementing the **Three Rings of Validation**:
- Inner Ring: Unit testing with TDD
- Middle Ring: Integration testing without mocks
- Outer Ring: Quality gates and standards

**`templates/GRIMOIRE.md`**  
Universal implementation template providing step-by-step guidance for building components with systematic validation and evidence collection.

**`templates/STATUS_MANIFEST.yaml`**  
Component tracking system with status progression: `PLANNED` → `IN_PROGRESS` → `USER_REVIEW` → `COMPLETED`

**`templates/GLOSSARY.md`**  
Project-specific terminology and architectural concept definitions.

**`templates/SUMMONER.md`**  
Template for generating detailed, component-specific implementation plans ("Scrolls") from high-level requirements.

**`templates/PROJECT_BOOTSTRAP.md`**  
Comprehensive guide for bootstrapping new projects from conception through technology selection and initial implementation structure.

### The Axiomancer Assistant

**`.claude/prompts/axiomancer.md`**  
Specialized Claude prompt for both new project bootstrapping and existing project systematization. Guides technology selection, analyzes codebases, and creates complete documentation ecosystems.

## Installation

### Quick Install (Recommended)

Install and launch Axiomancer in any project directory:

```bash
# Navigate to your project directory
cd /path/to/your/project

# Install and launch Axiomancer
curl -sSL https://raw.githubusercontent.com/axiomantic/axiomancer/main/install.sh | bash
```

This will:
1. Download the latest Axiomancer templates
2. Set up the `.claude/` directory in your project
3. Automatically launch Claude with the Axiomancer prompt (`claude /axiomancer`)
4. Clean up installation files after successful bootstrap

### Manual Install

```bash
# Clone the repository
git clone https://github.com/axiomantic/axiomancer.git
cd axiomancer

# Navigate to your project directory
cd /path/to/your/project

# Run the install script
/path/to/axiomancer/install.sh
```

### Prerequisites

- **Claude CLI**: Install from [Claude CLI Documentation](https://docs.anthropic.com/en/docs/tooling/claude-cli)
- **curl** and **unzip** (for remote installation)

## Usage

### Understanding "Summon"

**Important**: When you "summon" a component, Axiomancer doesn't just create a plan - it **generates the plan AND immediately implements it completely**. A summon is a full end-to-end process that results in tested, working code ready for review.

- `summon authentication-system` → Plan generated + Full implementation completed
- `summon user-dashboard` → Plan generated + Complete component built
- `summon data-processor` → Plan generated + All code and tests written

### Bootstrap a New Project

```bash
# Create and navigate to project directory
mkdir my-new-project && cd my-new-project

# Install and launch Axiomancer
curl -sSL https://raw.githubusercontent.com/axiomantic/axiomancer/main/install.sh | bash

# Then use prompts like:
# "create TaskManager" or "bootstrap web application"
```

The axiomancer will:
1. **Interview you about requirements** (purpose, users, technical needs)
2. **Recommend appropriate technology stack** (languages, frameworks, tools)
3. **Create complete project structure** with configuration files
4. **Generate systematic documentation** and development workflow
5. **Set up quality gates** and testing framework

### Organize an Existing Project

```bash
# Navigate to your existing project directory
cd /path/to/your/project

# Install and launch Axiomancer
curl -sSL https://raw.githubusercontent.com/axiomantic/axiomancer/main/install.sh | bash

# Then use prompts like:
# "organize this project" or "bring order to this codebase"
```

The axiomancer will:
1. **Analyze your project structure** (languages, frameworks, existing patterns)
2. **Create architectural guides** that map your actual codebase structure
3. **Generate component tracking system** reflecting real architecture boundaries
4. **Set up AI coding assistant configuration** tailored to your specific project
5. **Establish systematic development workflow** using your existing tools

### Generated Project Organization

After initialization, your project will have a complete organizational framework:

```
project/
├── AGENT.md              # AI coding assistant configuration
├── CLAUDE.md             # Symlink to AGENT.md  
├── AGENTS.md             # Symlink to AGENT.md
├── SYSTEM_ARCHITECTURE.md # Architectural guide mapping your codebase
├── CONTRIBUTING.md       # Development workflow and quality standards
├── GRIMOIRE.md          # Implementation patterns and templates
├── STATUS_MANIFEST.yaml # Component tracking and dependency management
├── GLOSSARY.md          # Project terminology and concepts
└── plans/               # Component-specific implementation plans
    └── (generated as needed)

Note: The .claude/ installation directory is automatically cleaned up after successful bootstrap.
```

### Development Workflow

1. **Component Selection**: Choose `PLANNED` component from `STATUS_MANIFEST.yaml`
2. **Summon Component**: Request "summon [component-id]" which will:
   - Generate a detailed implementation plan
   - **Immediately begin implementation** following Three Rings of Validation:
     - Write failing tests first (Inner Ring)
     - Implement functionality (Middle Ring)  
     - Pass quality gates (Outer Ring)
3. **Review Process**: Component automatically updated to `USER_REVIEW` → Human approval → `COMPLETED`

**Important**: "Summon" is a complete end-to-end process that generates the plan AND implements it immediately. It's not just planning - it's full implementation to completion.

## Key Principles

### Five Pillars of Excellence

1. **Precision**: Exact problem solving and requirement fulfillment
2. **Elegance**: Clean, readable, well-structured code
3. **Robustness**: Comprehensive error handling and edge case coverage
4. **Quality**: Adherence to standards, performance, and security
5. **Wisdom**: Deep understanding and thoughtful architectural decisions

### Three Rings of Validation

1. **Inner Ring (Unit Tests)**: Component isolation testing
2. **Middle Ring (Integration Tests)**: Workflow validation without mocks
3. **Outer Ring (Quality Gates)**: Code quality and standard compliance

### Sacred Laws of Development

- **Law of Quality**: Excellence is the minimum standard
- **Law of Verification**: Trust nothing without evidence
- **Law of Progress**: Every change advances the project
- **Law of Documentation**: Undocumented work doesn't exist

## Project Structure

```
axiomancer/
├── .claude/
│   └── prompts/
│       └── axiomancer.md    # Project initialization assistant
├── templates/               # Master templates
│   ├── AGENT.md
│   ├── SYSTEM_ARCHITECTURE.md
│   ├── CONTRIBUTING.md
│   ├── GRIMOIRE.md
│   ├── STATUS_MANIFEST.yaml
│   ├── GLOSSARY.md
│   └── SUMMONER.md
├── examples/               # Example generated documentation
└── README.md              # This file
```

## Features

### Intelligent Analysis
- **Code-Driven**: Analyzes actual project structure, not assumptions
- **Context-Aware**: Adapts to specific languages, frameworks, and patterns
- **Quality-Focused**: Emphasizes maintainability and best practices

### Complete Organizational Framework
- **Living Structure**: Framework that evolves with the project
- **Practical Focus**: Guides that developers actually use and follow
- **AI Assistant Ready**: Seamless integration with coding assistants

### Systematic Development
- **Structured Workflow**: Clear process for component development
- **Quality Assurance**: Built-in testing and validation requirements
- **Progress Tracking**: Component status and dependency management

## Examples

### Python Web Application
```yaml
PROJECT_NAME: "TaskFlow API"
LANGUAGE: "python"
TESTING_PHILOSOPHY: "pytest with comprehensive coverage"
QUALITY_GATES: "black --check; mypy; pytest --cov=src"
ARCHITECTURE: "Clean architecture with FastAPI"
```

### Rust Systems Project  
```yaml
PROJECT_NAME: "DataStream Engine"
LANGUAGE: "rust"
TESTING_PHILOSOPHY: "Property-based testing with unit coverage"
QUALITY_GATES: "cargo fmt --check; cargo clippy; cargo test"
ARCHITECTURE: "Memory-safe systems programming"
```

### TypeScript Frontend
```yaml
PROJECT_NAME: "Analytics Dashboard"  
LANGUAGE: "typescript"
TESTING_PHILOSOPHY: "Jest with React Testing Library"
QUALITY_GATES: "npm run lint; npm run type-check; npm test"
ARCHITECTURE: "Component-based React with TypeScript"
```

## Success Metrics

Axiomancer succeeds when:
- Project organization accurately reflects the actual codebase
- Development workflow integrates with existing tooling
- AI coding assistant provides effective, project-specific guidance
- Quality gates use tools already in the project
- Developers actually follow the systematic workflow
- Component tracking matches real architectural boundaries

## Philosophy in Practice

### From Chaos to Order
Transform any project into a well-organized, systematically documented codebase.

### From Undocumented to Systematic
Create comprehensive documentation that guides development and decision-making.

### From Isolated to Integrated
Enable seamless integration between human developers and AI coding assistants.

---

**Axiomancer: Where systematic excellence meets practical development.**

*"Quality is not an accident; it is the result of intelligent effort, systematic process, and unwavering commitment to excellence."*
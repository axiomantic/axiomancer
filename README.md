# Axiomancer: Project Template System

A comprehensive template system for bootstrapping high-quality software projects with systematic development workflows and intelligent AI coding assistant integration.

## Quick Start

```bash
# Navigate to your project directory (new or existing)
cd /path/to/your/project
curl -sSL https://raw.githubusercontent.com/axiomantic/axiomancer/main/install.sh | bash
claude /axiomancer
# or `opencode run /axiomancer`
```

**Then run:** `claude /axiomancer` (or `opencode run /axiomancer`)

## Table of Contents

- [What is Axiomancer?](#what-is-axiomancer)
- [Philosophy](#philosophy)
- [The Template System](#the-template-system)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Project Management](#project-management)
- [Key Principles](#key-principles)
- [Project Structure](#project-structure)
- [Features](#features)
- [Examples](#examples)
- [Success Metrics](#success-metrics)
- [Philosophy in Practice](#philosophy-in-practice)

## What is Axiomancer?

Axiomancer is a **template-driven project organization system** that installs directly into your projects to provide:

- **For New Projects**: Complete project bootstrapping from conception to working code
- **For Existing Projects**: Systematic organization and documentation of your codebase
- **For All Projects**: AI coding assistant integration with project-specific knowledge

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

## How It Works

1. **Install**: Run the install script in your project directory
2. **Invoke**: Use `claude /axiomancer` to start the specialized assistant
3. **Initialize**: The assistant analyzes your project and creates systematic documentation
4. **Develop**: Use the generated project structure for organized development
5. **Clean**: Installation files are automatically removed after setup

## Installation

### Prerequisites

- **Claude CLI** or **OpenCode**: For AI assistant integration
- **curl** and **unzip** (for remote installation)

### Remote Install (Recommended)

```bash
# Navigate to your project directory (new or existing)
cd /path/to/your/project
curl -sSL https://raw.githubusercontent.com/axiomantic/axiomancer/main/install.sh | bash
claude /axiomancer
# or `opencode run /axiomancer`
```

### Local Install

```bash
git clone https://github.com/axiomantic/axiomancer.git
cd axiomancer
./install.sh /path/to/your/project
claude /axiomancer
# or `opencode run /axiomancer`
```

## Usage

The installation script automatically launches the Axiomancer assistant, which configures your project and then removes itself. After configuration, you use the generated project documentation.

### User Stories & Workflows

#### 🆕 New Project Bootstrap

**Install & Initialize** (runs automatically):
```bash
mkdir my-project
cd my-project
curl -sSL https://raw.githubusercontent.com/axiomantic/axiomancer/main/install.sh | bash
claude /axiomancer
# or `opencode run /axiomancer`
```

**Provide Project Details** with detailed instructions:
```bash
claude "create TaskManager - a web app for team task management with user authentication, project organization, real-time updates, and deadline tracking. Use TypeScript, React, and Node.js with PostgreSQL."
```

Or start simple and let it interview you:
```
claude "bootstrap web application"
claude "create mobile app"
```

**What Happens During Bootstrap**:
1. **Requirements gathering** through interactive interview or from your detailed prompt
2. **Technology stack recommendation** and finalization
3. **System architecture document creation** (`SYSTEM_ARCHITECTURE.md`) with your specific technical design
4. **Implementation plan generation** (`STATUS_MANIFEST.yaml`) with all components identified
5. **Project structure setup** with configuration files and development workflow
6. **AI assistant configuration** (`AGENT.md`) tuned to your project

**Result**: Complete project with architecture docs, implementation roadmap, and systematic development process

#### 🔧 Existing Project Organization

**Install & Analyze** (runs automatically):
```bash
# In existing project directory
curl -sSL https://raw.githubusercontent.com/axiomantic/axiomancer/main/install.sh | bash
claude /axiomancer
# or `opencode run /axiomancer`
```

**Guide the Analysis** with context:
```bash
claude "systematize this codebase - it's a Python Flask API with SQLAlchemy, handles user management and data processing. Focus on the authentication system and API endpoints structure."
```

Or let it discover everything:
```bash
claude "organize this project"
claude "bring order to this codebase"
```

**What Happens During Organization**:
1. **Codebase analysis** of languages, frameworks, existing patterns, and architecture
2. **System architecture documentation** (`SYSTEM_ARCHITECTURE.md`) mapping your actual code structure
3. **Component identification** and status tracking (`STATUS_MANIFEST.yaml`) based on real boundaries
4. **Development workflow establishment** using your existing tools and practices
5. **AI assistant configuration** (`AGENT.md`) with project-specific knowledge

**Result**: Organized project with documentation that reflects your actual codebase and systematic development process

#### ⚡ Component Implementation

**Provide Detailed Implementation Instructions**:
```bash
claude "summon authentication-system - implement JWT-based auth with login, logout, token refresh, password reset via email, and role-based permissions. Include rate limiting and security headers."
```

**Or Use Simple Commands**:
```bash
claude "summon user-dashboard"
claude "summon data-processor"
```

**What Happens During Summon**:
1. **Implementation plan creation** in `plans/` directory with detailed technical specifications
2. **Complete implementation** following Three Rings of Validation:
   - Write failing tests first (Inner Ring)
   - Implement functionality (Middle Ring)
   - Pass quality gates (Outer Ring)
3. **Component status progression** `PLANNED` → `IN_PROGRESS` → `USER_REVIEW` → `COMPLETED`

**Result**: Fully implemented, tested component with documentation ready for review

**Important**: "Summon" is an end-to-end process that generates plans AND implements them completely!

### Key Differences: New vs Existing Projects

| Aspect | New Project | Existing Project |
|--------|-------------|------------------|
| **Architecture Docs** | Created from requirements | Created from code analysis |
| **Component Plan** | Based on feature planning | Based on existing code structure |
| **Development Workflow** | New best practices setup | Integrated with existing tools |
| **Quality Gates** | New testing framework | Uses existing test setup |

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
    └── (generated during summon commands)
```

**Note**: The `.axiomancer/` installation directory is automatically cleaned up after successful bootstrap to keep your project clean.

### Development Workflow Summary

1. **Install Axiomancer** → Automatic project analysis and documentation generation
2. **Review Generated Docs** → `SYSTEM_ARCHITECTURE.md`, `STATUS_MANIFEST.yaml`, etc.
3. **Start Development** → `claude AGENT.md` for component work
4. **Select Components** → Choose `PLANNED` items from `STATUS_MANIFEST.yaml`
5. **Summon & Implement** → Complete end-to-end implementation with testing
6. **Review & Approve** → Component moves from `USER_REVIEW` to `COMPLETED`

## Project Management

### Project Status Overview
- **`STATUS_MANIFEST.yaml`** - Central dashboard showing all components and their current status
- **Component Statuses**: `PLANNED` → `IN_PROGRESS` → `USER_REVIEW` → `COMPLETED`
- **Dependencies**: Clear tracking of component dependencies and implementation order
- **Effort Estimates**: Time estimates for each component to aid in planning

### Updating Plans and Architecture

**Add New Components to Plan**:
```bash
claude "add component user-notifications to the plan - handles email, SMS, and push notifications with templating and scheduling"
```

**Update System Architecture**:
```bash
claude "update system architecture to reflect the new microservices pattern we're adopting"
```

**Modify Component Specifications**:
```bash
claude "update the authentication component to use OAuth2 instead of JWT tokens"
```

### How System Architecture Gets Created

**For New Projects** - Interactive Interview Process:
1. **Project Purpose**: What problem does this solve? Who are the users?
2. **Technical Requirements**: Type of application, platforms, performance needs
3. **Technology Preferences**: Existing constraints, team experience, preferred stack
4. **Architecture Design**: Based on requirements, creates detailed technical architecture
5. **Component Planning**: Breaks down architecture into implementable components
6. **Template Population**: Fills in `{{PROJECT_NAME}}`, `{{ARCHITECTURE_TYPE}}`, etc. in templates

**For Existing Projects** - Code Analysis Process:
1. **Codebase Scanning**: Analyzes existing files, frameworks, and patterns
2. **Architecture Discovery**: Maps actual structure and component boundaries
3. **Documentation Creation**: Creates architecture docs reflecting real codebase
4. **Gap Identification**: Identifies missing components or improvement opportunities
5. **Integration Planning**: Plans how to integrate systematic development into existing workflow

**User Can Provide Details**: Instead of full interview, you can give comprehensive requirements:
```bash
claude "create TaskManager - a web application for team task management with user authentication, project organization, real-time collaboration, deadline tracking, and reporting. Target 100+ concurrent users, needs mobile responsiveness, integrate with Slack/email, use TypeScript/React frontend with Node.js/PostgreSQL backend, deploy on AWS with Docker containers."
```

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

# Project Bootstrap Template

**Purpose:** Guide for bootstrapping new projects from conception to systematic implementation  
**Context:** This template is used by the Axiomancer when creating new projects from scratch

---

## Project Conception Interview

When bootstrapping a new project, gather comprehensive requirements through structured inquiry:

### 1. Project Purpose & Goals
- **What problem does this project solve?**
- **Who are the target users?**
- **What are the core features/capabilities needed?**
- **What does success look like for this project?**

### 2. Technical Requirements
- **What type of application is this?** (web app, API, CLI tool, library, desktop app, mobile app, etc.)
- **What platforms must it support?** (web browsers, operating systems, mobile platforms)
- **What are the performance requirements?** (response time, throughput, concurrent users)
- **What are the scalability needs?** (expected growth, load patterns)
- **Are there specific security requirements?**
- **What integration points are needed?** (databases, APIs, services)

### 3. Team & Resources
- **How many developers will work on this?**
- **What's their experience level with different technologies?**
- **What's the timeline for initial version and ongoing development?**
- **What's the deployment/hosting environment?**

### 4. Constraints & Preferences
- **Are there any technology constraints or preferences?**
- **Are there existing systems this must integrate with?**
- **What's the budget for infrastructure/tools?**
- **Are there compliance or regulatory requirements?**

---

## Technology Stack Recommendations

Based on requirements, recommend appropriate technologies following these principles:

### Selection Criteria
1. **Community Support**: Large, active communities with good documentation
2. **Ecosystem Maturity**: Well-established with stable releases and long-term support
3. **Learning Curve**: Appropriate for team experience level
4. **Performance**: Meets stated performance requirements  
5. **Scalability**: Supports expected growth patterns
6. **Maintenance**: Long-term viability and support

### Common Stacks by Project Type

#### Web Applications (Full-Stack)
**Modern JavaScript/TypeScript:**
- Frontend: React/Next.js or Vue/Nuxt.js with TypeScript
- Backend: Node.js with Express/Fastify or Next.js API routes
- Database: PostgreSQL with Prisma ORM
- Deployment: Vercel/Netlify or Docker containers
- Testing: Jest, Cypress, Playwright

**Python Web:**
- Framework: FastAPI or Django
- Database: PostgreSQL with SQLAlchemy or Django ORM
- Frontend: React/Vue.js or Django templates
- Deployment: Docker with gunicorn
- Testing: pytest, Selenium

**Rust Web (Performance-Critical):**
- Framework: Axum or Actix-web
- Database: PostgreSQL with SQLx or Diesel
- Frontend: WASM + JS framework or separate frontend
- Deployment: Docker containers
- Testing: Built-in test framework

#### APIs & Microservices
**Node.js/TypeScript:**
- Framework: Express, Fastify, or Nest.js
- Database: PostgreSQL, MongoDB, or Redis
- Documentation: OpenAPI/Swagger
- Testing: Jest, Supertest

**Python:**
- Framework: FastAPI (preferred) or Flask
- Database: PostgreSQL with SQLAlchemy
- Documentation: FastAPI auto-docs
- Testing: pytest, httpx

**Go:**
- Framework: Gin, Echo, or net/http
- Database: PostgreSQL with GORM or sqlx
- Documentation: Swagger/OpenAPI
- Testing: Built-in testing package

#### CLI Tools
**Python:**
- Framework: Click, Typer, or argparse
- Distribution: PyPI with pip
- Testing: pytest
- Documentation: Sphinx

**Rust:**
- Framework: clap or structopt
- Distribution: Cargo/crates.io
- Testing: Built-in test framework
- Documentation: rustdoc

**Go:**
- Framework: Cobra or flag package
- Distribution: Go modules
- Testing: Built-in testing
- Documentation: godoc

#### Desktop Applications
**Cross-Platform:**
- Electron with React/Vue (web technologies)
- Tauri with Rust backend + web frontend
- Flutter Desktop

**Native:**
- macOS: Swift with SwiftUI
- Windows: C#/.NET with WPF/WinUI
- Linux: GTK with Python/Rust/C++

#### Mobile Applications
**Cross-Platform:**
- React Native (JavaScript/TypeScript)
- Flutter (Dart)
- .NET MAUI (C#)

**Native:**
- iOS: Swift with SwiftUI
- Android: Kotlin with Jetpack Compose

#### Libraries & SDKs
**Match Target Language:**
- JavaScript/TypeScript: npm, TypeScript definitions
- Python: PyPI, proper package structure
- Rust: Cargo, comprehensive documentation
- Go: Go modules, idiomatic APIs

---

## Initial Project Structure Generation

Create appropriate directory structure and configuration files:

### Universal Structure Elements
```
{{PROJECT_NAME}}/
├── README.md                 # Project overview and setup
├── .gitignore               # Version control exclusions
├── .env.example             # Environment variable template
├── LICENSE                  # Open source license (if applicable)
├── docs/                    # Additional documentation
│   └── api.md              # API documentation (if applicable)
├── tests/                   # Test files
│   ├── unit/               # Unit tests
│   └── integration/        # Integration tests
└── scripts/                # Development and deployment scripts
    ├── setup.sh            # Environment setup
    ├── test.sh             # Test runner
    └── deploy.sh           # Deployment script
```

### Language-Specific Additions

#### Python Projects
```
├── pyproject.toml           # Project configuration
├── requirements.txt         # Dependencies
├── requirements-dev.txt     # Development dependencies
├── {{PACKAGE_NAME}}/        # Main package directory
│   ├── __init__.py
│   ├── main.py             # Entry point
│   ├── config.py           # Configuration
│   └── core/               # Core modules
├── tests/
│   └── test_{{PACKAGE}}.py
└── .python-version          # Python version specification
```

#### Node.js/TypeScript Projects
```
├── package.json             # Project configuration and dependencies
├── tsconfig.json           # TypeScript configuration
├── jest.config.js          # Test configuration
├── .eslintrc.js            # Linting configuration
├── .prettierrc             # Code formatting
├── src/                    # Source code
│   ├── index.ts            # Entry point
│   ├── config.ts           # Configuration
│   └── core/               # Core modules
├── dist/                   # Compiled output
└── __tests__/              # Test files
```

#### Rust Projects
```
├── Cargo.toml              # Project configuration
├── src/                    # Source code
│   ├── main.rs             # Entry point (binary)
│   ├── lib.rs              # Library root
│   ├── config.rs           # Configuration
│   └── core/               # Core modules
├── tests/                  # Integration tests
├── benches/                # Benchmarks
└── examples/               # Usage examples
```

#### Go Projects
```
├── go.mod                  # Module definition
├── go.sum                  # Dependency checksums
├── cmd/                    # Application entry points
│   └── {{APP_NAME}}/
│       └── main.go
├── internal/               # Private application code
│   ├── config/
│   └── core/
├── pkg/                    # Public library code
├── api/                    # API definitions
├── web/                    # Web assets
└── deployments/            # Deployment configurations
```

---

## Configuration File Templates

### Python (pyproject.toml)
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "{{PROJECT_NAME}}"
version = "0.1.0"
description = "{{PROJECT_DESCRIPTION}}"
authors = [{name = "{{AUTHOR_NAME}}", email = "{{AUTHOR_EMAIL}}"}]
license = {text = "MIT"}
requires-python = ">=3.9"
dependencies = [
    # Core dependencies
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
    "black>=22.0",
    "mypy>=1.0",
    "ruff>=0.1.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "--cov={{PACKAGE_NAME}} --cov-report=html --cov-report=term"

[tool.black]
line-length = 88
target-version = ['py39']

[tool.mypy]
python_version = "3.9"
strict = true

[tool.ruff]
line-length = 88
target-version = "py39"
```

### Node.js/TypeScript (package.json)
```json
{
  "name": "{{PROJECT_NAME}}",
  "version": "0.1.0",
  "description": "{{PROJECT_DESCRIPTION}}",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "ts-node src/index.ts",
    "test": "jest",
    "test:watch": "jest --watch",
    "lint": "eslint src/**/*.ts",
    "format": "prettier --write src/**/*.ts"
  },
  "dependencies": {
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "typescript": "^5.0.0",
    "ts-node": "^10.9.0",
    "jest": "^29.0.0",
    "@types/jest": "^29.0.0",
    "ts-jest": "^29.0.0",
    "eslint": "^8.0.0",
    "@typescript-eslint/eslint-plugin": "^6.0.0",
    "@typescript-eslint/parser": "^6.0.0",
    "prettier": "^3.0.0"
  }
}
```

### Rust (Cargo.toml)
```toml
[package]
name = "{{PROJECT_NAME}}"
version = "0.1.0"
edition = "2021"
description = "{{PROJECT_DESCRIPTION}}"
authors = ["{{AUTHOR_NAME}} <{{AUTHOR_EMAIL}}>"]
license = "MIT"
repository = "{{REPOSITORY_URL}}"

[dependencies]
# Core dependencies

[dev-dependencies]
# Development dependencies

[[bin]]
name = "{{PROJECT_NAME}}"
path = "src/main.rs"

[lib]
name = "{{PACKAGE_NAME}}"
path = "src/lib.rs"
```

---

## Quality Gate Setup

Establish quality gates appropriate for the technology stack:

### Python Quality Gates
```bash
# Format check
black --check .

# Type checking
mypy .

# Linting
ruff check .

# Testing
pytest --cov={{PACKAGE_NAME}} --cov-report=term-missing

# Security
bandit -r {{PACKAGE_NAME}}/
```

### Node.js/TypeScript Quality Gates
```bash
# Type checking
npx tsc --noEmit

# Linting
npx eslint src/**/*.ts

# Format check
npx prettier --check src/**/*.ts

# Testing
npm test

# Security audit
npm audit
```

### Rust Quality Gates
```bash
# Format check
cargo fmt --check

# Linting
cargo clippy -- -D warnings

# Testing
cargo test

# Security audit
cargo audit

# Documentation
cargo doc --no-deps
```

---

## Initial Documentation Generation

Create essential documentation files:

### README.md Template
```markdown
# {{PROJECT_NAME}}

{{PROJECT_DESCRIPTION}}

## Features

- {{FEATURE_1}}
- {{FEATURE_2}}
- {{FEATURE_3}}

## Installation

{{INSTALLATION_INSTRUCTIONS}}

## Usage

{{USAGE_EXAMPLES}}

## Development

### Prerequisites

- {{PREREQUISITE_1}}
- {{PREREQUISITE_2}}

### Setup

{{SETUP_INSTRUCTIONS}}

### Testing

{{TEST_INSTRUCTIONS}}

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

## License

{{LICENSE_INFO}}
```

### Initial Component Architecture

Based on project requirements, create appropriate component breakdown for STATUS_MANIFEST.yaml:

#### Web Application Components
1. **Core Foundation** - Basic setup, configuration, error handling
2. **Authentication** - User management and security
3. **Database Layer** - Data models and persistence
4. **API Layer** - REST/GraphQL endpoints
5. **Business Logic** - Core application logic
6. **Frontend Components** - UI components and pages
7. **Integration Layer** - External service integrations
8. **Testing Framework** - Comprehensive test suite

#### API/Service Components
1. **Core Foundation** - Basic setup, configuration
2. **API Framework** - Routing and middleware
3. **Data Layer** - Database and models
4. **Business Logic** - Core service logic
5. **External Integrations** - Third-party services
6. **Authentication & Authorization** - Security layer
7. **Testing & Documentation** - QA and API docs

#### CLI Tool Components
1. **Core Foundation** - Basic setup and configuration
2. **Command Parser** - CLI interface and argument handling
3. **Core Logic** - Main functionality
4. **Output Formatting** - User-friendly output
5. **Configuration Management** - Settings and preferences
6. **Error Handling** - Robust error reporting
7. **Testing Framework** - Comprehensive test coverage

---

## Success Criteria for Bootstrap

A successful project bootstrap includes:

### 1. Complete Project Structure ✅
- Appropriate directory layout for technology stack
- Configuration files with sensible defaults
- Development scripts and tooling setup
- Version control initialization

### 2. Technology Stack Validation ✅
- All recommended technologies are well-supported and mature
- Dependencies are current and secure
- Build system is configured and functional
- Quality gates are established and working

### 3. Documentation Foundation ✅
- Clear README with setup and usage instructions
- Architecture documentation reflecting actual structure
- Development guidelines and contribution process
- Component breakdown suitable for iterative development

### 4. Development Readiness ✅
- Project can be built and run immediately
- Tests can be executed successfully
- Quality gates pass on initial codebase
- Development environment is fully configured

### 5. Systematic Structure ✅
- STATUS_MANIFEST.yaml defines all components
- SYSTEM_ARCHITECTURE.md matches actual structure
- CONTRIBUTING.md reflects chosen technology stack
- AGENT.md configured for project-specific development

---

**Project bootstrapping is the foundation of systematic development. A well-structured beginning enables sustainable growth and maintainable evolution.**

*"Every great project begins with a single, well-planned step."*
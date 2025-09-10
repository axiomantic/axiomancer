# How to Contribute to {{PROJECT_NAME}}

**Version:** 1.0  
**Project Phase:** {{PROJECT_PHASE}}

## 1. The Philosophy of Development

Contributing to {{PROJECT_NAME}} is a disciplined practice of creating high-quality, maintainable software through systematic development and rigorous validation. Our workflow ensures quality, safety, and consistent progress through structured implementation.

Our development process is built upon key artifacts, each serving a critical purpose:

- **The Canon (`SYSTEM_ARCHITECTURE.md`)**: The architectural constitution and single source of truth defining the system design and principles
- **The Implementation Guide (`GRIMOIRE.md`)**: Universal template for implementing components following established patterns
- **The Progress Tracker (`STATUS_MANIFEST.yaml`)**: Live tracking of all component status, dependencies, and progress
- **The Contribution Guidelines (This Document)**: The exact workflow and standards for all development work
- **The Sacred Tests**: Comprehensive validation ensuring quality and preventing regressions

## 2. The Sacred Laws of Development

All development follows these inviolable principles:

### 2.1. The Law of Quality
**"Excellence is the minimum standard"**
- All code must meet established quality gates
- All implementations must follow established patterns  
- All components must integrate cleanly with the system
- All work must advance project objectives

### 2.2. The Law of Verification
**"Trust nothing without evidence"**
- All functionality must be tested comprehensively
- All claims must be proven with concrete evidence
- All implementations must be validated against requirements
- All changes must be verified through quality gates

### 2.3. The Law of Progress
**"Every change advances the project"**
- Every contribution must move the project forward
- No work should introduce technical debt without justification
- All implementations must maintain or improve system quality
- Dependencies must be respected and completed in order

### 2.4. The Law of Documentation
**"Undocumented work doesn't exist"**
- All components must be properly documented
- All decisions must be recorded with rationale
- All interfaces must be clearly specified
- All complex logic must be explained

## 3. The Development Workflow

All development follows this precise ritual for implementing components:

### Step 1: Component Selection and Summoning
- Examine `STATUS_MANIFEST.yaml` to identify components with status `PLANNED`
- Verify all dependencies are `COMPLETED`
- **Summon the component**: Request "summon [component-id]" which will:
  - Generate a detailed implementation plan
  - **Immediately implement the component completely**
  - Update status to `USER_REVIEW` when done

### Step 2: Manual Implementation (Alternative Path)
If you prefer manual implementation instead of summoning, perform these preparatory steps:

**2.1. Architectural Alignment**
- Review relevant sections of `SYSTEM_ARCHITECTURE.md` to understand the component's role
- Identify integration points with existing components
- Understand established patterns and conventions

**2.2. Dependency Verification**
- Confirm all prerequisite components are `COMPLETED`
- Verify no circular dependencies exist
- Check that required resources are available

**2.3. Test Strategy Formation**
- Define success criteria from requirements
- Plan comprehensive test coverage
- Design integration scenarios
- Establish performance benchmarks

### Step 3: Test-Driven Implementation

**The Three Rings of Validation**: All components must pass through three concentric rings of testing:

#### The Inner Ring (Unit Tests)
**Purpose**: Validate individual component behavior in isolation

1. **Write Failing Tests First**: Create comprehensive unit tests that define expected behavior
2. **Implement Minimum Code**: Write only enough code to make tests pass
3. **Refactor for Quality**: Improve code structure while maintaining passing tests
4. **Coverage Requirements**: Achieve minimum {{COVERAGE_PERCENTAGE}}% coverage

Example:
```{{LANGUAGE}}
{{UNIT_TEST_EXAMPLE}}
```

#### The Middle Ring (Integration Tests)
**Purpose**: Validate component interactions and workflows

1. **Test Real Scenarios**: Create tests that simulate actual usage patterns
2. **No Mocking**: Test against real implementations where possible
3. **Validate Workflows**: Ensure complete user journeys work correctly
4. **Performance Testing**: Verify performance meets requirements

Example:
```{{LANGUAGE}}
{{INTEGRATION_TEST_EXAMPLE}}
```

#### The Outer Ring (Quality Gates)
**Purpose**: Ensure code quality and maintainability

1. **Static Analysis**: Pass all linting and style checks
2. **Type Safety**: Ensure proper typing throughout
3. **Security Scanning**: Address any security vulnerabilities
4. **Documentation**: Complete all documentation requirements

Quality Gate Commands:
```bash
{{QUALITY_GATE_COMMANDS}}
```

### Step 4: Evidence Collection
Document comprehensive evidence of successful implementation:

**4.1. Test Evidence**
```bash
# Unit test evidence
{{UNIT_TEST_COMMAND}}
# All tests must pass

# Integration test evidence
{{INTEGRATION_TEST_COMMAND}}
# All workflows must succeed

# Coverage evidence
{{COVERAGE_COMMAND}}
# Must meet minimum coverage requirements
```

**4.2. Quality Evidence**
```bash
# Code quality evidence
{{QUALITY_COMMANDS}}
# All quality gates must pass
```

**4.3. Performance Evidence**
```
{{PERFORMANCE_METRICS_EXAMPLE}}
```

### Step 5: Completion and Review

**5.1. Update Status to USER_REVIEW**
```yaml
# STATUS_MANIFEST.yaml
{{COMPONENT_ID}}:
  status: USER_REVIEW  # Changed from IN_PROGRESS
  completion_date: "{{TIMESTAMP}}"
  evidence_provided: true
  test_coverage: "{{COVERAGE}}%"
  quality_gates: "PASSED"
  review_notes: "Ready for human approval - all evidence provided"
```

**5.2. Request Human Review**
- Notify human reviewer that component is complete
- Provide summary of implementation and key achievements
- Component remains in `USER_REVIEW` until approved
- Human updates to `COMPLETED` when satisfied

**5.3. Version Control** (After approval)
- Create feature branch: `feature/{{COMPONENT_ID}}-description`
- Commit with clear, descriptive messages
- Open pull request with comprehensive description
- Include all evidence in PR description

## 4. Component Implementation Standards

### 4.1. Code Standards

**Quality Requirements**:
```{{LANGUAGE}}
{{CODE_STANDARDS_EXAMPLE}}
```

**Error Handling Requirements**:
```{{LANGUAGE}}
{{ERROR_HANDLING_EXAMPLE}}
```

**Documentation Requirements**:
```{{LANGUAGE}}
{{DOCUMENTATION_EXAMPLE}}
```

### 4.2. Testing Standards

**Test Structure**:
```{{LANGUAGE}}
{{TEST_STRUCTURE_EXAMPLE}}
```

**Test Naming Conventions**:
- Unit tests: `test_{{component}}_{{specific_behavior}}`
- Integration tests: `test_integration_{{workflow}}`
- Performance tests: `test_performance_{{operation}}`

### 4.3. Documentation Standards

**Component Documentation**:
- Purpose and responsibilities
- Interface specifications
- Usage examples
- Integration guidelines
- Performance characteristics

## 5. The Conflict Resolution Protocol

**The Canon is Law**: `SYSTEM_ARCHITECTURE.md` is the ultimate source of truth.

### When Conflicts Arise:

1. **STOP**: Immediately halt all implementation work
2. **DOCUMENT**: Create a `CONFLICT` notice stating:
   - The architectural section in conflict
   - The conflicting requirement or instruction
   - Suggested resolution approaches
3. **RESOLVE**: Work with team to update Canon and resolve conflict
4. **PROCEED**: Continue only after conflict is resolved

## 6. Quality Gates and Requirements

### 6.1. Code Quality Gates
- **Linting**: All code must pass {{LINTER}} with no errors
- **Formatting**: All code must be formatted with {{FORMATTER}}
- **Type Checking**: All code must pass {{TYPE_CHECKER}}
- **Security**: No critical security vulnerabilities

### 6.2. Testing Requirements
- **Unit Test Coverage**: Minimum {{UNIT_COVERAGE}}%
- **Integration Coverage**: All critical paths tested
- **Performance**: Meets established benchmarks
- **Regression**: No existing tests broken

### 6.3. Documentation Requirements
- **Code Comments**: All complex logic explained
- **API Documentation**: All public interfaces documented
- **Examples**: Usage examples for key features
- **Architecture**: Component fits documented architecture

## 7. Emergency Protocols

### 7.1. Build Failure Protocol
If builds fail after changes:
1. Revert changes immediately
2. Fix issues in isolated environment
3. Re-test comprehensively before resubmitting

### 7.2. Performance Regression Protocol
If performance degrades:
1. Profile to identify bottlenecks
2. Compare against baseline metrics
3. Optimize without compromising functionality
4. Document performance analysis

### 7.3. Security Issue Protocol
If security vulnerabilities are found:
1. **CRITICAL**: Fix immediately, notify team
2. **HIGH**: Fix within current iteration
3. **MEDIUM/LOW**: Document and schedule fix

## 8. Contribution Workflow Summary

```
1. SELECT component (STATUS_MANIFEST.yaml) → Update to IN_PROGRESS
2. PLAN implementation → Review architecture, verify dependencies
3. TEST FIRST → Write comprehensive failing tests
4. IMPLEMENT → Write minimum code to pass tests
5. REFACTOR → Improve quality while maintaining tests
6. VALIDATE → Pass all quality gates and requirements
7. DOCUMENT → Complete all documentation
8. REVIEW → Update to USER_REVIEW, await approval
9. COMPLETE → Human approval updates to COMPLETED
```

## 9. Status Workflow

### Status Progression:
```
PLANNED → IN_PROGRESS → USER_REVIEW → COMPLETED
    ↑                                       ↓
    └──────── (if revisions needed) ────────┘
```

### Status Definitions:
- **PLANNED**: Component identified but not started
- **IN_PROGRESS**: Component actively being implemented
- **USER_REVIEW**: Implementation complete, awaiting review
- **COMPLETED**: Implementation reviewed and approved

## 10. Best Practices

### 10.1. Before Starting
- Review all relevant documentation
- Understand component dependencies
- Plan comprehensive test strategy
- Allocate sufficient time for quality

### 10.2. During Development
- Follow TDD rigorously
- Commit frequently with clear messages
- Run tests continuously
- Keep documentation updated

### 10.3. Before Completion
- Verify all tests pass
- Check coverage meets requirements
- Ensure documentation is complete
- Validate against requirements

## 11. Getting Help

If you encounter issues:
1. Check existing documentation
2. Review similar completed components
3. Consult architectural guidelines
4. Request clarification before proceeding

---

**Excellence in software development comes from disciplined process, rigorous testing, and unwavering commitment to quality. Follow these guidelines to contribute effectively to {{PROJECT_NAME}}.**

*"Quality is not an act, it is a habit."*
#!/bin/bash

# Development setup script for Axiomancer
# Installs development dependencies and sets up pre-commit hooks

set -e

echo "🔧 Setting up Axiomancer development environment..."

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not installed"
    exit 1
fi

# Install test dependencies
echo "📦 Installing test dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements-test.txt

# Install pre-commit
echo "🪝 Installing pre-commit..."
python3 -m pip install pre-commit

# Install pre-commit hooks
echo "⚙️  Installing pre-commit hooks..."
pre-commit install

# Run initial checks
echo "✅ Running initial pre-commit checks..."
pre-commit run --all-files || echo "⚠️  Some checks failed - fix and commit to resolve"

echo ""
echo "🎉 Development environment setup complete!"
echo ""
echo "📋 Available commands:"
echo "   • Run tests: python -m pytest tests/ -v"
echo "   • Run tests with coverage: python -m pytest tests/ -v --cov=."
echo "   • Run pre-commit checks: pre-commit run --all-files"
echo "   • Install locally: ./install.sh"
echo ""
echo "🧹 Pre-commit hooks are now installed and will run automatically on commit"
echo ""
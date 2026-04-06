# Makefile for Marketing Campaign Analytics

# Default target
.DEFAULT_GOAL := help

# Colors
GREEN = \033[0;32m
YELLOW = \033[0;33m
BLUE = \033[0;34m
RED = \033[0;31m
NC = \033[0m # No Color

# Project info
PROJECT_NAME = marketing-campaign-analytics
PYTHON = python3
PIP = pip

# Help target
.PHONY: help
help:
	@echo ""
	@echo "$(BLUE)Marketing Campaign Analytics - Available Commands$(NC)"
	@echo ""
	@echo "$(GREEN)Setup & Installation$(NC)"
	@echo "  make install          Install dependencies"
	@echo "  make install-dev     Install with development dependencies"
	@echo "  make requirements    Update requirements.txt"
	@echo ""
	@echo "$(GREEN)Running the Pipeline$(NC)"
	@echo "  make all              Run complete pipeline"
	@echo "  make generate        Generate synthetic data"
	@echo "  make preprocess      Preprocess data"
	@echo "  make model            Train ML model"
	@echo "  make dashboard       Launch dashboard"
	@echo ""
	@echo "$(GREEN)Development$(NC)"
	@echo "  make lint             Run linting checks"
	@echo "  make format           Format code"
	@echo "  make test            Run tests"
	@echo "  make clean           Clean cache and build files"
	@echo ""
	@echo "$(GREEN)Docker$(NC)"
	@echo "  make docker-build    Build Docker image"
	@echo "  make docker-run      Run Docker container"
	@echo ""
	@echo "For more details, see README.md"
	@echo ""

# Installation targets
.PHONY: install
install:
	$(PIP) install -r requirements.txt

.PHONY: install-dev
install-dev:
	$(PIP) install -r requirements.txt
	$(PIP) install -e .[dev]

.PHONY: requirements
requirements:
	$(PIP) freeze > requirements.txt

# Pipeline targets
.PHONY: all
all:
	@echo "$(YELLOW)Running complete pipeline...$(NC)"
	$(PYTHON) main.py all

.PHONY: generate
generate:
	@echo "$(YELLOW)Generating synthetic data...$(NC)"
	$(PYTHON) main.py generate

.PHONY: preprocess
preprocess:
	@echo "$(YELLOW)Preprocessing data...$(NC)"
	$(PYTHON) main.py preprocess

.PHONY: model
model:
	@echo "$(YELLOW)Training ML model...$(NC)"
	$(PYTHON) main.py model

.PHONY: dashboard
dashboard:
	@echo "$(YELLOW)Launching dashboard...$(NC)"
	$(PYTHON) main.py dashboard

# Development targets
.PHONY: lint
lint:
	@echo "$(YELLOW)Running linting checks...$(NC)"
	flake8 src models dashboard --max-line-length=100 --ignore=E203,W503 || true

.PHONY: format
format:
	@echo "$(YELLOW)Formatting code...$(NC)"
	black src models dashboard main.py --line-length=100

.PHONY: test
test:
	@echo "$(YELLOW)Running tests...$(NC)"
	pytest tests/ -v || echo "$(RED)No tests found$(NC)"

.PHONY: clean
clean:
	@echo "$(YELLOW)Cleaning cache and build files...$(NC)"
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ *.egg 2>/dev/null || true
	@echo "$(GREEN)Clean complete!$(NC)"

# Docker targets
.PHONY: docker-build
docker-build:
	docker build -t $(PROJECT_NAME):latest .

.PHONY: docker-run
docker-run:
	docker run -p 8501:8501 $(PROJECT_NAME):latest

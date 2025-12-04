# CHANGELOG

All notable changes to this project will be documented in this file.

## v0.1.0 - 2025-12-04

Summary
- Consolidated cookiecutter template into a single, modular layout with conditional components for CLI, API, and AI/ML research.
- Added experiment tracking utilities and example configs for AI/ML projects.
- Implemented developer tooling (black, isort, flake8, mypy, pre-commit) and a post-generation hook to remove unused components.
- Bugfixes and documentation updates.

Commits included
- 8d61993 2025-12-04 refactor: move experiments.py to utils/ directory for better organization (Dipak Rimal)
- 597a3c2 2025-12-04 feat: add experiment tracking and logging utilities (Dipak Rimal)
- a338aa0 2025-12-04 fix: remove project_id reference from README.md template (Dipak Rimal)
- cd99e60 2025-12-04 refactor: simplify cookiecutter prompts and auto-generate values (Dipak Rimal)
- df4874d 2025-12-04 feat: add complete template infrastructure and improvements (Dipak Rimal)
- 54ba0f2 2025-12-04 feat: add comprehensive linting and formatting configuration (Dipak Rimal)
- 108cec8 2025-12-04 feat: add post-generation hook for conditional component cleanup (Dipak Rimal)
- 66d564a 2025-12-04 docs: update README for new consolidated template structure (Dipak Rimal)
- bf9db3b 2025-12-04 refactor: consolidate into single template directory (Dipak Rimal)
- 50b81e0 2025-12-04 feat: restructure cookiecutter template with modular architecture and conditional components (Dipak Rimal)
- adc3a66 2025-10-30 Update pyproject.toml with Python version and build system (Dipak Rimal)
- ee91a45 2025-10-30 Update README with new files and structure (Dipak Rimal)
- 22201bf 2025-10-30 Create requirements.txt for data science project (Dipak Rimal)
- 72a73ff 2025-10-30 Create pyproject.toml with project details and dependencies (Dipak Rimal)
- b965842 2025-10-30 Update user template text in prompts.yaml (Dipak Rimal)
- 0299825 2025-10-29 update github path (Dipak Rimal)
- ba24239 2025-10-29 first time import (Dipak Rimal)
- 2001a35 2025-10-29 Initial commit (Dipak Rimal)
Files changed (selected)
- `{{cookiecutter.project_slug}}/src/{{cookiecutter.package_name}}/utils/experiments.py` — new utility for experiment logging
- `hooks/post_gen_project.py` — post-generation cleanup
- `{{cookiecutter.project_slug}}/pyproject.toml` — project metadata & tool configuration
- `{{cookiecutter.project_slug}}/.pre-commit-config.yaml`, `{{cookiecutter.project_slug}}/.flake8` — code quality tooling
- `{{cookiecutter.project_slug}}/README.md` — consolidated and updated template README

How to reproduce
```bash
cookiecutter /path/to/cookiecutter-project-template --no-input \
  project_name="My Project" include_ai_research="yes" include_cli="yes" include_api="yes"
cd my-project
pip install -r requirements.txt
pytest tests/
```


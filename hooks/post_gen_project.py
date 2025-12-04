#!/usr/bin/env python
"""Post-generation hook to clean up conditional directories and files."""

import os
import shutil
from pathlib import Path

# Get cookiecutter variables
include_cli = "{{ cookiecutter.include_cli }}" == "yes"
include_api = "{{ cookiecutter.include_api }}" == "yes"
include_ai_research = "{{ cookiecutter.include_ai_research }}" == "yes"
package_name = "{{ cookiecutter.package_name }}"

project_root = Path(".")

def remove_if_exists(path):
    """Remove a file or directory if it exists."""
    if path.exists():
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
        print(f"Removed: {path}")

# Remove AI/ML research directories if not included
if not include_ai_research:
    remove_if_exists(project_root / "data")
    remove_if_exists(project_root / "experiments")
    remove_if_exists(project_root / "notebooks")
    remove_if_exists(project_root / "reports")
    remove_if_exists(project_root / "tests" / "test_models.py")
    remove_if_exists(project_root / "tests" / "test_train.py")

# Remove API directories if not included
if not include_api:
    remove_if_exists(project_root / "scripts")
    api_path = project_root / "src" / package_name / "api"
    remove_if_exists(api_path)
    remove_if_exists(project_root / "tests" / "test_api.py")

# Remove CLI file if not included
if not include_cli:
    cli_path = project_root / "src" / package_name / "cli.py"
    remove_if_exists(cli_path)
    remove_if_exists(project_root / "tests" / "test_cli.py")

print("✅ Project generation complete!")
print(f"   Include CLI: {include_cli}")
print(f"   Include API: {include_api}")
print(f"   Include AI/ML Research: {include_ai_research}")

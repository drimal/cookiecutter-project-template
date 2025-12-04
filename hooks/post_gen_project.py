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
        print(f"✓ Removed: {path}")

# Remove AI/ML research directories if not included
if not include_ai_research:
    print("\n📁 Removing AI/ML research modules...")
    remove_if_exists(project_root / "data")
    remove_if_exists(project_root / "experiments")
    remove_if_exists(project_root / "notebooks")
    remove_if_exists(project_root / "reports")
    remove_if_exists(project_root / "src" / package_name / "data")
    remove_if_exists(project_root / "src" / package_name / "features")
    remove_if_exists(project_root / "src" / package_name / "models")
    remove_if_exists(project_root / "src" / package_name / "train")
    remove_if_exists(project_root / "src" / package_name / "eval")
    remove_if_exists(project_root / "src" / package_name / "infer")
    remove_if_exists(project_root / "tests" / "test_models.py")
    remove_if_exists(project_root / "tests" / "test_train.py")

# Remove API directories if not included
if not include_api:
    print("\n🔌 Removing API modules...")
    remove_if_exists(project_root / "scripts")
    api_path = project_root / "src" / package_name / "api"
    remove_if_exists(api_path)
    remove_if_exists(project_root / "tests" / "test_api.py")

# Remove CLI file if not included
if not include_cli:
    print("\n💻 Removing CLI modules...")
    cli_path = project_root / "src" / package_name / "cli.py"
    remove_if_exists(cli_path)
    remove_if_exists(project_root / "tests" / "test_cli.py")

print("\n✅ Project generation complete!")
print(f"📋 Configuration:")
print(f"   • CLI support: {'✅ Enabled' if include_cli else '❌ Disabled'}")
print(f"   • API support: {'✅ Enabled' if include_api else '❌ Disabled'}")
print(f"   • AI/ML research: {'✅ Enabled' if include_ai_research else '❌ Disabled'}")
project_dir = Path.cwd().name

print(f"\n📚 Next steps:")
print(f"   1. cd {project_dir}")

# Prefer 'uv' (if available) as an alternative virtualenv helper.
# `uv` is a Python package that provides a small virtualenv helper. It may be
# installed globally, via `pipx`, or in user site-packages. We cannot import
# it reliably here, so show both usage and install instructions for Unix and
# Windows (PowerShell and cmd) users.
if shutil.which("uv"):
    print(f"   2. (optional) create/activate virtualenv with `uv`: e.g. `uv .venv --python 3.11`")
    print(f"    `source .venv/bin/activate` (Linux/Mac) OR `source .venv/Scripts/activate` (If Windows)")
   
else:
    # Unix / macOS
    print(f"   2. python -m venv .venv && source .venv/bin/activate")
    print(f"      OR, to use the `uv` helper (if you prefer):")
    print(f"         - install via pipx: `pipx install uv`")
    print(f"         - or install via pip: `pip install --user uv`")
    print(f"         then run: `uv .venv`")
    # Windows examples
    print(f"      Windows (PowerShell):")
    print(f"         python -m venv .venv")
    print(f"         .\\.venv\\Scripts\\Activate.ps1")
    print(f"      Windows (cmd.exe):")
    print(f"         python -m venv .venv")
    print(f"         .\\.venv\\Scripts\\activate.bat")
    print(f"      To install `uv` on Windows (optional):")
    print(f"         python -m pip install --user pipx && python -m pipx ensurepath")
    print(f"         pipx install uv")

print(f"   3. pip install -r requirements.txt OR uv pip install -r requirements.txt ")
print(f"   4. pytest tests/")


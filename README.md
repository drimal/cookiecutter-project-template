# cookiecutter-project-template

A flexible cookiecutter template for creating Python projects with support for multiple project types: utilities, REST APIs, and AI/ML research workflows.

## Quick Start

### 1. Install & Create a Project

```bash
pip install cookiecutter
cookiecutter https://github.com/drimal/cookiecutter-project-template.git
```

You'll be prompted to enter:
- **project_id**: Unique project identifier (e.g., `PRJ-001`)
- **project_name**: Full project name (e.g., `Data Analysis Tool`)
- **project_slug**: URL-friendly slug (e.g., `data-analysis-tool`)
- **package_name**: Python package name (e.g., `data_analysis_tool`)
- **author_name**: Your name
- **date_created**: Creation date
- **include_cli**: Enable CLI interface? (yes/no)
- **include_api**: Enable REST API? (yes/no)
- **include_ai_research**: Enable AI/ML research modules? (yes/no)

This generates a complete, ready-to-use project structure.

### 2. Project Structure

The generated project includes:

```
{{cookiecutter.project_slug}}/
├── README.md                    # Project documentation
├── .gitignore                   # Git ignore rules
├── pyproject.toml              # Project configuration & dependencies
├── requirements.txt            # Python dependencies
│
├── src/{{cookiecutter.package_name}}/
│   ├── __init__.py             # Package initialization
│   ├── core/                   # Core functionality modules
│   ├── utils/                  # Utility functions & helpers
│   ├── cli.py                  # CLI interface (if enabled)
│   ├── api/                    # REST API with FastAPI (if enabled)
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── routes/
│   │   └── utils/
│   └── [AI/ML modules]         # (if include_ai_research enabled)
│       ├── data/               # Data processing
│       ├── features/           # Feature engineering
│       ├── models/             # Model definitions
│       ├── train/              # Training utilities
│       ├── eval/               # Evaluation utilities
│       └── infer/              # Inference utilities
│
├── notebooks/                  # Jupyter notebooks (AI/ML only)
├── experiments/                # Experiment tracking (AI/ML only)
│   ├── configs/
│   └── runs/
├── data/                       # Data directory (AI/ML only)
│   ├── raw/
│   └── processed/
├── reports/                    # Reports & outputs (AI/ML only)
│   ├── figures/
│   └── tables/
├── scripts/                    # Utility scripts (API only)
└── tests/                      # Test suite
    ├── test_core.py
    ├── test_cli.py             # (if CLI enabled)
    ├── test_api.py             # (if API enabled)
    ├── test_models.py          # (if AI/ML enabled)
    └── test_train.py           # (if AI/ML enabled)
```

### 3. Getting Started with Your Project

After generating the project:

```bash
cd {{cookiecutter.project_slug}}
pip install -r requirements.txt
pytest tests/                   # Run tests
```

**For CLI Projects:**
```bash
python -m {{cookiecutter.package_name}}.cli --help
```

**For API Projects:**
```bash
python -m {{cookiecutter.package_name}}.api.app
# Visit http://localhost:8000/docs for API documentation
```

**For AI/ML Research:**
```bash
# Open notebooks in Jupyter and run them in order
jupyter notebook notebooks/
```

### 4. Development Workflow

#### Writing Code
- **Core logic**: `src/{{cookiecutter.package_name}}/core/`
- **Utilities**: `src/{{cookiecutter.package_name}}/utils/`
- **Tests**: `tests/test_*.py`

#### Running Tests
```bash
pytest tests/ -v                # Verbose output
pytest tests/ --cov            # With coverage report
```

#### Code Quality
```bash
black src/ tests/              # Format code
flake8 src/ tests/             # Lint
mypy src/                      # Type checking
```

#### Notebook Development (AI/ML projects)
Develop functions in notebooks and sync to source files:

```python
%%writefile -a ../src/{{cookiecutter.package_name}}/utils/__init__.py
def my_helper(x, y):
    """Example helper function"""
    return x + y
```

Import and use immediately:
```python
from {{cookiecutter.package_name}}.utils import my_helper
result = my_helper(1, 2)
```

### 5. Configuration

Edit `pyproject.toml` to:
- Add project dependencies
- Configure pytest options
- Set code formatting rules (black, isort, mypy)

Edit `requirements.txt` for simple dependency specification.

## Template Features

### Flexible Configuration
Choose which components to include:
- ✅ **CLI**: Command-line interface for tools
- ✅ **API**: FastAPI-based REST API server
- ✅ **AI/ML Research**: Complete research workflow with notebooks and experiments

### Modern Python Setup
- `pyproject.toml` for all project configuration
- Optional dependencies for different features
- Built-in pytest configuration with coverage
- Pre-configured black, isort, and flake8 settings

### Complete Test Suite
- Test files for all enabled components
- Pre-configured pytest in `pyproject.toml`
- Support for coverage reporting

### Development-Ready
- `.gitignore` with Python best practices
- Clear directory structure following Python conventions
- Modular organization for scalability

## Examples

### Basic Utility Package
```bash
cookiecutter https://github.com/drimal/cookiecutter-project-template.git
# Select: include_cli=no, include_api=no, include_ai_research=no
```
Creates a minimal Python package for libraries or utilities.

### REST API
```bash
cookiecutter https://github.com/drimal/cookiecutter-project-template.git
# Select: include_cli=no, include_api=yes, include_ai_research=no
```
Creates a FastAPI project with API routes and utilities.

### AI/ML Research
```bash
cookiecutter https://github.com/drimal/cookiecutter-project-template.git
# Select: include_cli=no, include_api=no, include_ai_research=yes
```
Creates a research project with notebooks, experiments, and data directories.

### Full Stack
```bash
cookiecutter https://github.com/drimal/cookiecutter-project-template.git
# Select: include_cli=yes, include_api=yes, include_ai_research=yes
```
Creates a complete project with CLI, API, and research capabilities.

## Repository Structure

This repository contains:
- `cookiecutter.json` - Template configuration and variables
- `{{cookiecutter.project_slug}}/` - The template directory that gets generated as your new project
- `hooks/post_gen_project.py` - Post-generation hook that removes unused directories based on your selections

### How It Works

When you run cookiecutter:
1. The template creates all possible directories and files
2. The `post_gen_project.py` hook runs after generation
3. Unused components are automatically removed based on your feature selections:
   - If `include_cli=no`: `cli.py` and `test_cli.py` are removed
   - If `include_api=no`: `api/`, `scripts/`, and `test_api.py` are removed
   - If `include_ai_research=no`: `data/`, `experiments/`, `notebooks/`, `reports/`, `test_models.py`, and `test_train.py` are removed

## Contributing

Improvements and suggestions are welcome! Feel free to open issues or pull requests.

## License

This template is provided as-is for creating new projects.

# {{ cookiecutter.project_name }} ({{ cookiecutter.project_id }})

**Author**: {{ cookiecutter.author_name }}  
**Created**: {{ cookiecutter.date_created }}  

## Overview

This is an example project demonstrating the cookiecutter template structure for data science and research projects. The template supports flexible configurations for different project types including CLI tools, REST APIs, and AI/ML research workflows.

## Project Structure

```
{{cookiecutter.project_slug}}/
├── README.md                    # Project documentation
├── .gitignore                   # Git ignore rules
├── pyproject.toml              # Project configuration
├── requirements.txt            # Python dependencies
│
├── src/{{cookiecutter.package_name}}/
│   ├── __init__.py             # Package initialization
│   ├── core/                   # Core functionality modules
│   ├── utils/                  # Utility functions
│   ├── cli.py                  # CLI interface (optional)
│   ├── api/                    # REST API (optional)
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── routes/
│   │   └── utils/
│   └── [AI/ML modules]         # If include_ai_research enabled
│       ├── data/               # Data processing
│       ├── features/           # Feature engineering
│       ├── models/             # Model definitions
│       ├── train/              # Training utilities
│       ├── eval/               # Evaluation utilities
│       └── infer/              # Inference utilities
│
├── notebooks/                  # Jupyter notebooks (if AI/ML enabled)
├── experiments/                # Experiment tracking (if AI/ML enabled)
│   ├── configs/
│   └── runs/
├── data/                       # Data storage (if AI/ML enabled)
│   ├── raw/
│   └── processed/
├── reports/                    # Reports and outputs (if AI/ML enabled)
│   ├── figures/
│   └── tables/
├── scripts/                    # Utility scripts (if API enabled)
└── tests/                      # Test suite
    ├── test_core.py
    ├── test_cli.py             # (if CLI enabled)
    ├── test_api.py             # (if API enabled)
    ├── test_models.py          # (if AI/ML enabled)
    └── test_train.py           # (if AI/ML enabled)
```

## Getting Started

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run tests**:
   ```bash
   pytest tests/
   ```

## Development Workflow

### For AI/ML Research Projects

Run notebooks in order for reproducibility:
1. Open `notebooks/0_setup.ipynb`
2. Proceed through analysis notebooks (1 → 4)

You can **develop functions inside notebooks** and automatically sync them into `src/`:

```python
%%writefile -a ../src/{{cookiecutter.package_name}}/utils/__init__.py
def my_new_helper(x, y):
    return x + y

# Now immediately usable:
from {{cookiecutter.package_name}}.utils import my_new_helper
my_new_helper(2, 3)
```

### For API Projects

Start the API server:
```bash
python -m {{cookiecutter.package_name}}.api.app
```

### For CLI Projects

Run CLI commands:
```bash
python -m {{cookiecutter.package_name}}.cli --help
```

## Configuration Options

This template is generated from a cookiecutter with the following options:
- `include_cli`: Enable CLI interface
- `include_api`: Enable REST API with FastAPI
- `include_ai_research`: Enable AI/ML research modules and notebooks

Based on your selections, only relevant directories and test files are included.

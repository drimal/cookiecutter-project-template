# {{ cookiecutter.project_name }} ({{ cookiecutter.project_id }})

**Author**: {{ cookiecutter.author_name }}  
**Created**: {{ cookiecutter.date_created }}  

## Project Structure

```
src/{{cookiecutter.package_name}}/
  ├── __init__.py               # Package initialization
  ├── core/                     # Core functionality
  ├── utils/                    # Utility functions
{%- if cookiecutter.include_cli == "yes" %}
  ├── cli.py                    # Command-line interface
{%- endif %}
{%- if cookiecutter.include_api == "yes" %}
  ├── api/                      # REST API (FastAPI)
  │   ├── __init__.py
  │   ├── app.py                # Main application
  │   ├── routes/               # API route handlers
  │   └── utils/                # API utilities
{%- endif %}
{%- if cookiecutter.include_ai_research == "yes" %}
  ├── data/                     # Data processing modules
  ├── features/                 # Feature engineering
  ├── models/                   # Model definitions
  ├── train/                    # Training utilities
  ├── eval/                     # Evaluation utilities
  └── infer/                    # Inference utilities

notebooks/                      # Jupyter notebooks for exploration
experiments/                    # Experiment tracking
  ├── configs/                  # Configuration files
  └── runs/                     # Experiment results

data/                           # Data storage
  ├── raw/                      # Original data
  └── processed/                # Processed data

reports/                        # Reports and visualizations
  ├── figures/                  # Generated figures
  └── tables/                   # Generated tables
{%- endif %}
{%- if cookiecutter.include_api == "yes" %}

scripts/                        # Utility scripts
{%- endif %}

tests/                          # Test suite
  ├── test_core.py              # Core tests
{%- if cookiecutter.include_cli == "yes" %}
  ├── test_cli.py               # CLI tests
{%- endif %}
{%- if cookiecutter.include_api == "yes" %}
  ├── test_api.py               # API tests
{%- endif %}
{%- if cookiecutter.include_ai_research == "yes" %}
  ├── test_models.py            # Model tests
  └── test_train.py             # Training tests
{%- endif %}
```

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Running Tests

```bash
pytest tests/ -v
```

{%- if cookiecutter.include_cli == "yes" %}

### CLI Usage

```bash
python -m {{cookiecutter.package_name}}.cli --help
```

{%- elif cookiecutter.include_api == "yes" %}

### Starting the API

```bash
python -m {{cookiecutter.package_name}}.api.app
```

The API will be available at `http://localhost:8000`

Visit `/docs` for interactive API documentation.

{%- elif cookiecutter.include_ai_research == "yes" %}

### Running Analysis

Open and run the notebooks in order:
1. `notebooks/0_setup.ipynb` - Setup and data loading
2. `notebooks/1_data_prep.ipynb` - Data preparation
3. `notebooks/2_analysis.ipynb` - Analysis
4. `notebooks/3_results.ipynb` - Results
5. `notebooks/4_report.ipynb` - Report generation

{%- endif %}

## Development

### Code Organization

- **src/{{cookiecutter.package_name}}/core/** - Core business logic
- **src/{{cookiecutter.package_name}}/utils/** - Reusable utilities
- **tests/** - Unit and integration tests

### Development Workflow

1. Write code in `src/{{cookiecutter.package_name}}/`
2. Write tests in `tests/`
3. Run tests: `pytest tests/`
4. Format code: `black src/ tests/`
5. Lint: `flake8 src/ tests/`

{%- if cookiecutter.include_ai_research == "yes" %}

### Notebook Development

You can develop functions in notebooks and sync them to source files:

```python
%%writefile -a ../src/{{cookiecutter.package_name}}/utils/__init__.py
def helper_function(x, y):
    """Example helper function"""
    return x + y
```

Then use it immediately:

```python
from {{cookiecutter.package_name}}.utils import helper_function
result = helper_function(1, 2)
```

{%- endif %}

## Configuration

Edit `pyproject.toml` to:
- Add dependencies
- Configure pytest options
- Set code formatting rules

Edit `requirements.txt` for simple dependency specification.

## Project Structure Notes

This project was generated with the following options:
- **include_cli**: {% if cookiecutter.include_cli == "yes" %}✅ Enabled{% else %}❌ Disabled{% endif %}
- **include_api**: {% if cookiecutter.include_api == "yes" %}✅ Enabled{% else %}❌ Disabled{% endif %}
- **include_ai_research**: {% if cookiecutter.include_ai_research == "yes" %}✅ Enabled{% else %}❌ Disabled{% endif %}

Unused components are not included in the generated project.

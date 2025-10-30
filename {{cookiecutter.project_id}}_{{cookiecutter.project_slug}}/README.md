# {{ cookiecutter.project_name }} ({{ cookiecutter.project_id }})

**Author**: {{ cookiecutter.author_name }}  
**Created**: {{ cookiecutter.date_created }}  

## Project Structure
- notebooks/: Analysis workflow broken into stages  
- data/raw: Original unmodified data  
- data/processed: Cleaned and prepared data  
- results/figures: Visualizations  
- results/tables: Tabular outputs  
- results/exports: Reports, models, or deliverables  
- src/: Reusable helper functions
- requirement.txt: requirements 
- pyproject.toml:  

## Workflow
Run notebooks in order (1 → 4) for reproducibility.


## Utility Development Workflow

This template supports a workflow where you can **develop functions inside notebooks** 
and automatically sync them into `src/utils.py`:

1. Open `notebooks/0_setup.ipynb`.
2. Use `%%writefile -a ../src/utils.py` in a cell to append a new function to `utils.py`.
3. `%autoreload` ensures that updates are immediately available without restarting the kernel.

Example:

```python
%%writefile -a ../src/utils.py
def my_new_helper(x, y):
    return x + y

# Now immediately usable:
from src import utils
utils.my_new_helper(2, 3)
```

This keeps reusable utilities in one place while letting you prototype in Jupyter naturally.

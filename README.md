# cookiecutter-project-template

# Quickstart Guide

Welcome to your analysis project scaffold! This guide summarizes the most common workflows.

---

## 1. Create a New Project
```bash
pip install cookiecutter
cookiecutter git@github.com:drimal/cookiecutter-project-template.git
```

You’ll be asked to enter:
- Project ID
- Project Name
- Slug (short identifier)
- Author
- Date

This generates a structured project with notebooks, prompts, and utilities.

---

## 2. Prompt Management
- Draft prompts in your notebook.
- Save them into the central registry with:

```python
from src import utils

system_prompt = """You are a precise assistant. Summarize in 3 sentences."""
utils.save_prompt(
    role="system_prompts",
    pid="sys_summarizer",
    description="3-sentence summarizer",
    text=system_prompt
)
```

This updates:
- `prompts/prompts.yaml` (registry with metadata)
- `prompts/archive/` (plain text versioned files for Git diffs)

---

## 3. Experiment Logging
Log each run with a link to the prompt ID:

```python
utils.log_run(
    config="GPT-4 baseline",
    dataset="essays",
    metric=0.82,
    notes="Test with summarizer",
    prompt_id="sys_summarizer_v1"
)
```

View styled log:
```python
utils.display_run_log()
```

Save to CSV:
```python
utils.save_run_log()
```

---

## 4. Analysis & Reporting
- `3_results.ipynb` compares metrics by **Prompt ID** (tables + charts).  
- `4_report.ipynb` summarizes findings in stakeholder-friendly Markdown, including per-prompt results.

---

## 5. Running the Pipeline
Re-run all notebooks in order with one command:

```bash
pip install papermill
python run_pipeline.py
```

This executes notebooks 1 → 4 and saves executed versions with `_out.ipynb` suffix.

---

## 6. Notebook Utilities Workflow
Prototype helpers in a notebook, then promote to `utils.py`:

```python
%%writefile -a src/utils.py
def plot_metrics(df):
    import matplotlib.pyplot as plt
    df.plot(x="Run ID", y="Metric", marker="o")
    plt.show()
```

With `%autoreload` enabled (in `0_setup.ipynb`), changes are instantly available.

---

## 7. Configuration
Project settings live in `project_config.yaml`.  
Update thresholds, default dataset paths, and project metadata here.

---

✅ You now have a reproducible, prompt-aware analysis workflow with minimal manual overhead.

"""Master pipeline runner for {{cookiecutter.project_name}}.

This script executes the analysis notebooks in order using Papermill.
"""

import papermill as pm

# Define the execution order of notebooks
notebooks = [
    "notebooks/1_data_prep.ipynb",
    "notebooks/2_analysis.ipynb",
    "notebooks/3_results.ipynb",
    "notebooks/4_report.ipynb"
]

def run_pipeline():
    print("Starting pipeline execution...")
    for nb in notebooks:
        print(f"Running {nb} ...")
        pm.execute_notebook(nb, nb.replace('.ipynb', '_out.ipynb'))
        print(f"Finished {nb}")
    print("Pipeline complete.")

if __name__ == "__main__":
    run_pipeline()

# Utility functions for {{cookiecutter.project_name}}

import pandas as pd
import yaml
from datetime import datetime
from IPython.display import display

# Load project config
with open("../project_config.yaml", "r") as f:
    CONFIG = yaml.safe_load(f)

# Initialize a run log
run_log = []
run_counter = 0

def log_run(config: str, dataset: str, metric: float, notes: str):
    """Log a single experimental run with auto-incrementing ID and timestamp."""
    global run_counter
    run_counter += 1
    run_id = f"{run_counter:02d}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    run_log.append({
        "Run ID": run_id,
        "Config": config,
        "Dataset": dataset,
        "Metric": metric,
        "Notes": notes,
        "Timestamp": timestamp
    })

def get_run_log():
    """Return the run log as a pandas DataFrame."""
    return pd.DataFrame(run_log)

def save_run_log(name: str = "runs"):
    """Save the run log to CSV in results/tables with timestamp."""
    df = get_run_log()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"../{CONFIG['results_folder']}/tables/{name}_{timestamp}.csv"
    df.to_csv(path, index=False)
    print(f"Run log saved to {path}")

def display_run_log(threshold: float = None):
    """Display the run log with styling to highlight metrics above/below threshold."""
    df = get_run_log()
    if df.empty:
        print("No runs logged yet.")
        return None

    if threshold is None:
        threshold = CONFIG.get("default_threshold", 0.8)

    def highlight_metric(val):
        try:
            return 'background-color: lightgreen' if val >= threshold else 'background-color: lightcoral'
        except Exception:
            return ''

    styled = df.style.applymap(highlight_metric, subset=['Metric'])
    display(styled)
    return df

def save_results(df: pd.DataFrame, folder: str = "tables", name: str = "results"):
    """Save any DataFrame into the results folder with timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"../{CONFIG['results_folder']}/{folder}/{name}_{timestamp}.csv"
    df.to_csv(path, index=False)
    print(f"Results saved to {path}")


import yaml
from pathlib import Path
from datetime import datetime

def save_prompt(role: str, pid: str, description: str, text: str,
                registry_path="../prompts/prompts.yaml",
                export_txt=True):
    """
    Save a prompt into a YAML registry (with versioning + metadata).
    Optionally also exports the text to a .txt file for Git diffs.
    """

    registry_path = Path(registry_path)
    if registry_path.exists():
        with open(registry_path, "r") as f:
            data = yaml.safe_load(f) or {}
    else:
        data = {"system_prompts": [], "user_templates": []}

    # Check existing versions
    existing = [p for p in data.get(role, []) if p["id"] == pid]
    version = len(existing) + 1

    entry = {
        "id": pid,
        "version": version,
        "description": description,
        "text": text,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data[role].append(entry)

    # Write back to YAML
    with open(registry_path, "w") as f:
        yaml.dump(data, f, sort_keys=False)

    # Optional: also export to plain .txt
    if export_txt:
        folder = Path(registry_path).parent / "archive"
        folder.mkdir(exist_ok=True)
        txt_path = folder / f"{pid}_v{version}.txt"
        with open(txt_path, "w") as f:
            f.write(text)

    print(f"✅ Saved prompt {pid} v{version} to {registry_path}")
    return entry

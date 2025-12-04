{%- if cookiecutter.include_ai_research == "yes" %}
"""Experiment tracking and logging utilities.

This module provides utilities for tracking experiments, logging results,
and managing experiment configurations.

Available in AI/ML research projects.
"""

import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional


class ExperimentLogger:
    """Logger for tracking ML experiments with JSON and CSV outputs."""

    def __init__(self, runs_dir: str = "experiments/runs"):
        """Initialize experiment logger.

        Args:
            runs_dir: Directory to store experiment runs
        """
        self.runs_dir = Path(runs_dir)
        self.runs_dir.mkdir(parents=True, exist_ok=True)
        self.runs: list[Dict[str, Any]] = []

    def log_run(
        self,
        name: str,
        config: Dict[str, Any],
        metrics: Dict[str, Any],
        notes: Optional[str] = None,
    ) -> str:
        """Log a single experiment run.

        Args:
            name: Name of the experiment
            config: Configuration dictionary
            metrics: Metrics dictionary with results
            notes: Optional notes about the run

        Returns:
            run_id: Unique identifier for this run
        """
        run_id = f"run_{len(self.runs):04d}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        run_data = {
            "run_id": run_id,
            "name": name,
            "timestamp": datetime.now().isoformat(),
            "config": config,
            "metrics": metrics,
            "notes": notes or "",
        }
        
        self.runs.append(run_data)
        
        # Save individual run to JSON
        run_file = self.runs_dir / f"{run_id}.json"
        with open(run_file, "w") as f:
            json.dump(run_data, f, indent=2)
        
        print(f"✅ Logged run: {run_id}")
        return run_id

    def save_summary(self, output_file: str = "experiments/runs/summary.csv") -> None:
        """Save summary of all runs to CSV.

        Args:
            output_file: Path to output CSV file
        """
        if not self.runs:
            print("⚠️  No runs to save")
            return
        
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, "w", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["run_id", "name", "timestamp", "best_metric", "notes"],
            )
            writer.writeheader()
            
            for run in self.runs:
                metrics = run.get("metrics", {})
                best_metric = max(metrics.values()) if metrics else None
                
                writer.writerow({
                    "run_id": run["run_id"],
                    "name": run["name"],
                    "timestamp": run["timestamp"],
                    "best_metric": best_metric,
                    "notes": run["notes"],
                })
        
        print(f"✅ Saved summary to {output_file}")


# Example usage (for reference during development)
if __name__ == "__main__":
    logger = ExperimentLogger()
    
    # Log first run
    logger.log_run(
        name="baseline_model",
        config={"model": "linear_regression", "epochs": 10},
        metrics={"accuracy": 0.85, "loss": 0.25},
        notes="Initial baseline",
    )
    
    # Log second run with improvements
    logger.log_run(
        name="improved_model",
        config={"model": "neural_net", "layers": 3, "learning_rate": 0.001},
        metrics={"accuracy": 0.92, "loss": 0.12},
        notes="Added hidden layers",
    )
    
    logger.save_summary()
    print("✅ Experiments logged successfully")
{%- endif %}

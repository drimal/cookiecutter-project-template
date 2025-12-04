"""Experiment tracking and logging utilities.

This module provides utilities for tracking experiments, logging results,
and managing experiment configurations.
"""

import json
import csv
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional


class ExperimentLogger:
    """Log and track experiments with configurations and results."""

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
        metrics: Dict[str, float],
        notes: Optional[str] = None,
    ) -> str:
        """Log an experiment run.
        
        Args:
            name: Experiment name
            config: Experiment configuration
            metrics: Experiment metrics/results
            notes: Optional notes about the experiment
            
        Returns:
            Run ID
        """
        run_id = f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        run_data = {
            "run_id": run_id,
            "name": name,
            "timestamp": datetime.now().isoformat(),
            "config": config,
            "metrics": metrics,
            "notes": notes or "",
        }
        
        self.runs.append(run_data)
        
        # Save to JSON
        run_file = self.runs_dir / f"{run_id}.json"
        with open(run_file, "w") as f:
            json.dump(run_data, f, indent=2)
        
        return run_id

    def save_summary(self, output_file: str = "experiments/runs_summary.csv") -> None:
        """Save summary of all runs to CSV.
        
        Args:
            output_file: Path to output CSV file
        """
        if not self.runs:
            print("No runs to save")
            return
        
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, "w", newline="") as f:
            fieldnames = ["run_id", "name", "timestamp", "notes"]
            # Add metric names to fieldnames
            if self.runs and "metrics" in self.runs[0]:
                fieldnames.extend(self.runs[0]["metrics"].keys())
            
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for run in self.runs:
                row = {
                    "run_id": run["run_id"],
                    "name": run["name"],
                    "timestamp": run["timestamp"],
                    "notes": run["notes"],
                }
                row.update(run["metrics"])
                writer.writerow(row)


# Example usage
if __name__ == "__main__":
    logger = ExperimentLogger()
    
    # Log a sample run
    logger.log_run(
        name="baseline_model",
        config={"model": "linear", "learning_rate": 0.01},
        metrics={"accuracy": 0.85, "loss": 0.25},
        notes="Initial baseline",
    )
    
    logger.log_run(
        name="improved_model",
        config={"model": "neural_net", "layers": 3, "learning_rate": 0.001},
        metrics={"accuracy": 0.92, "loss": 0.12},
        notes="Added hidden layers",
    )
    
    logger.save_summary()
    print("✅ Experiments logged successfully")

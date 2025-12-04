"""CLI interface for {{ cookiecutter.project_name }}

{% if cookiecutter.include_cli == "yes" %}
This module provides command-line interface functionality.
{% endif %}
"""

import argparse
import sys


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="{{ cookiecutter.project_name }}"
    )
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")
    
    args = parser.parse_args()
    print("CLI not yet implemented")


if __name__ == "__main__":
    main()

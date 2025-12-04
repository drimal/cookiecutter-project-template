"""CLI interface for {{ cookiecutter.project_name }}

{% if cookiecutter.include_cli == "yes" %}
This module provides command-line interface functionality.
{% endif %}
"""

import argparse
import sys
from . import __version__


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        prog="{{ cookiecutter.project_slug }}",
        description="{{ cookiecutter.project_name }}",
        epilog="For more information, visit the project documentation.",
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Example subcommand
    example_parser = subparsers.add_parser("example", help="Run example command")
    example_parser.add_argument("--name", default="World", help="Name to greet")
    
    args = parser.parse_args()
    
    if args.command == "example":
        print(f"Hello, {args.name}!")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

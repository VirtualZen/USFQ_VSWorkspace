from datetime import datetime


def log_start(name: str) -> None:
    """Log a standardized start message for a module or task.

    Currently prints a blank line and a START line with an ISO timestamp.
    """
    print()
    print(f"START {name} — {datetime.now().isoformat()}")


def log_end(name: str) -> None:
    """Log a standardized end message for a module or task."""
    print()
    print(f"END {name} — {datetime.now().isoformat()}")
    print()

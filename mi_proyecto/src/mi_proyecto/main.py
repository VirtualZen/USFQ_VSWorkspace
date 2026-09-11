"""Small script that creates a pandas DataFrame and prints it."""

import sys


try:
    import pandas as pd
except ImportError:
    print("pandas is not installed. Install it with: pip install pandas")
    sys.exit(1)

from .logging_utils import log_start, log_end


def crear_dataframe():
    """Create and return the project's main DataFrame."""
    data = {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "score": [88.5, 92.0, 79.3],
    }
    return pd.DataFrame(data)

def main():
    log_start("main.py")

    df = crear_dataframe()
    print("DataFrame:\n", df)
    print("\nData types:\n", df.dtypes)
    print("\nSummary:\n", df.describe(include="all"))
    log_end("main.py")

if __name__ == "__main__":
    main()

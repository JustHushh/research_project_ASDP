import pandas as pd

def compute_mean(csv_path):
    """Compute mean of numeric columns in a CSV file."""
    df = pd.read_csv(csv_path)
    return df.mean(numeric_only=True).to_dict()

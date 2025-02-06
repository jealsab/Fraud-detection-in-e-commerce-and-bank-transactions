import pandas as pd  

def load_data(filename):
    """Load data from a CSV file into a Pandas DataFrame."""
    return pd.read_csv(filename)

def save_data(data, filename):
    """Save a Pandas DataFrame to a CSV file."""
    data.to_csv(filename, index=False)

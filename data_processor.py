import pandas as pd

def process_data(df):
    """Example function to process data"""
    if df is not None:
        df["New Column"] = df["Age"] * 2  # Example: Multiply Age by 2
    return df

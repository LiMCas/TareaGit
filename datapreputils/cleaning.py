import pandas as pd

def delete_null_values(df, axis=0):
    return df.dropna(axis=axis)


def replace_missing_values(df, method="mean", value=None):
    df = df.copy()

    if method == "mean":
        return df.fillna(df.mean(numeric_only=True))

    elif method == "median":
        return df.fillna(df.median(numeric_only=True))

    elif method == "mode":
        return df.fillna(df.mode().iloc[0])

    elif method == "constant":
        return df.fillna(value)

    else:
        raise ValueError("Unsupported method")
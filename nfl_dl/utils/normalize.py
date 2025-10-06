# nfl_dl/utils/normalize.py
import pandas as pd
import numpy as np
import re

def safe_int_cast(series: pd.Series) -> pd.Series:
    """Convert column to nullable int, handling NaN, 'nan', and float-like strings."""
    return pd.to_numeric(series, errors="coerce").astype("Int64")

def safe_text_cast(series: pd.Series) -> pd.Series:
    """Convert column to string, replacing NaN-like values with None."""
    return (
        series.astype(str)
        .replace(["nan", "NaN", "None", "NULL", "null", "N/A"], None)
        .replace("None", None)
    )

def normalize_dataframe(
    df: pd.DataFrame,
    int_cols: list[str] | None = None,
    text_cols: list[str] | None = None,
    bool_cols: list[str] | None = None,
) -> pd.DataFrame:
    """Normalize numeric/text/boolean columns in a DataFrame."""
    df = df.copy()

    if int_cols:
        for col in int_cols:
            if col in df.columns:
                df[col] = safe_int_cast(df[col])

    if text_cols:
        for col in text_cols:
            if col in df.columns:
                df[col] = safe_text_cast(df[col])

    if bool_cols:
        for col in bool_cols:
            if col in df.columns:
                df[col] = df[col].astype(bool)

    return df
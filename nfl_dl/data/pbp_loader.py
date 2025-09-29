# nfl_dl/pbp_loader.py
import nflreadpy as nfl
import pandas as pd
import datetime

def load_season(season: int) -> pd.DataFrame:
    """Fetch play-by-play for a given season as pandas DataFrame."""
    df = nfl.load_pbp([season])
    return df.to_pandas()

def load_current_season() -> tuple[pd.DataFrame, int]:
    """Fetch current season PBP."""
    season = datetime.date.today().year
    return load_season(season), season
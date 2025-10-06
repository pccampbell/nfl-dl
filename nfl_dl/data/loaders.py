# nfl_dl/data/loaders.py
import nflreadpy as nfl
import pandas as pd
from utils.normalize import normalize_dataframe


# ---------- Daily (seasonal + current) ----------

def load_pbp_season(season: int) -> pd.DataFrame:
    return nfl.load_pbp([season]).to_pandas()

def load_pbp_current_season() -> pd.DataFrame:
    """NFLReadPy defaults to current season if no season is passed."""
    return nfl.load_pbp().to_pandas()


def load_player_stats_season(season: int) -> pd.DataFrame:
    return nfl.load_player_stats([season]).to_pandas()

def load_player_stats_current_season() -> pd.DataFrame:
    return nfl.load_player_stats().to_pandas()


def load_team_stats_season(season: int) -> pd.DataFrame:
    return nfl.load_team_stats([season]).to_pandas()

def load_team_stats_current_season() -> pd.DataFrame:
    return nfl.load_team_stats().to_pandas()


def load_rosters_season(season: int) -> pd.DataFrame:
    df = nfl.load_rosters([season]).to_pandas()
    df = normalize_dataframe(
        df,
        int_cols=["jersey_number"]
    )
    return nfl.load_rosters([season]).to_pandas()

def load_rosters_current_season() -> pd.DataFrame:
    return nfl.load_rosters().to_pandas()


def load_schedules_season(season: int) -> pd.DataFrame:
    return nfl.load_schedules([season]).to_pandas()

def load_schedules_current_season() -> pd.DataFrame:
    return nfl.load_schedules().to_pandas()


def load_snap_counts_season(season: int) -> pd.DataFrame:
    return nfl.load_snap_counts([season]).to_pandas()

def load_snap_counts_current_season() -> pd.DataFrame:
    return nfl.load_snap_counts().to_pandas()


def load_nextgen_stats_season(season: int) -> pd.DataFrame:
    return nfl.load_nextgen_stats([season]).to_pandas()

def load_nextgen_stats_current_season() -> pd.DataFrame:
    return nfl.load_nextgen_stats().to_pandas()


def load_depth_charts_season(season: int) -> pd.DataFrame:
    return nfl.load_depth_charts([season]).to_pandas()

def load_depth_charts_current_season() -> pd.DataFrame:
    return nfl.load_depth_charts().to_pandas()


def load_ff_opportunity_season(season: int) -> pd.DataFrame:
    return nfl.load_ff_opportunity([season]).to_pandas()

def load_ff_opportunity_current_season() -> pd.DataFrame:
    return nfl.load_ff_opportunity().to_pandas()


def load_ftn_charting_season(season: int) -> pd.DataFrame:
    return nfl.load_ftn_charting([season]).to_pandas()

def load_ftn_charting_current_season() -> pd.DataFrame:
    return nfl.load_ftn_charting().to_pandas()


def load_officials_season(season: int) -> pd.DataFrame:
    return nfl.load_officials([season]).to_pandas()

def load_officials_current_season() -> pd.DataFrame:
    return nfl.load_officials().to_pandas()


# ---------- Other (weekly or static) ----------

def load_draft_picks_season(season: int) -> pd.DataFrame:
    return nfl.load_draft_picks([season]).to_pandas()

def load_draft_picks_current_season() -> pd.DataFrame:
    return nfl.load_draft_picks().to_pandas()


def load_combine_season(season: int) -> pd.DataFrame:
    return nfl.load_combine([season]).to_pandas()

def load_combine_current_season() -> pd.DataFrame:
    return nfl.load_combine().to_pandas()


def load_players() -> pd.DataFrame:
    return nfl.load_players().to_pandas()

def load_contracts() -> pd.DataFrame:
    return nfl.load_contracts().to_pandas()

def load_trades() -> pd.DataFrame:
    return nfl.load_trades().to_pandas()

def load_teams() -> pd.DataFrame:
    return nfl.load_teams().to_pandas()

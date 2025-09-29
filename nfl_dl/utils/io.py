import pandas as pd
from io import StringIO

def df_to_stringio(df: pd.DataFrame) -> StringIO:
    buf = StringIO()
    df.to_csv(buf, index=False, header=False)
    buf.seek(0)
    return buf
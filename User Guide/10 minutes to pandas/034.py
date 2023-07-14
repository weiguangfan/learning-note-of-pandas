import numpy as np
import pandas as pd
dates = pd.date_range("20130101", periods=6)
print(dates)
print(type(dates))
print(dates.dtype)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(type(df))
print(df.dtypes)
print(df)
print(df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"]))
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
print(df1.dtypes)
df1.loc[dates[0]:dates[1], "E"] = 1
print(df1)


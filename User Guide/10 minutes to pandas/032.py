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
print(df.loc[:, "D"])
print(np.array([5] * len(df)))
df.loc[:,"D"] = np.array([5] * len(df))
print(df)
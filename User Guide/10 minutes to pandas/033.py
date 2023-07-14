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
df2 = df.copy()
print(df2)
print(df2 > 0)
print(df2[df2 > 0])
print(-df2)
df2[df2 > 0] = -df2
print(df2)
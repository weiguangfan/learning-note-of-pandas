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
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
print(s1.dtypes)
print(type(s1))
print(s1)
df["F"] = s1
print(df)
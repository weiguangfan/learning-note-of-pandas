import numpy as np
import pandas as pd
rng = pd.date_range("1/1/2012", periods=100, freq="S")
print(rng)
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(ts)
print(ts.shape)
print(ts.resample("5Min"))
print(ts.resample("5Min").sum())
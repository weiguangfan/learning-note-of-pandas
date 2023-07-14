import numpy as np
import pandas as pd
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(type(df2))
print(df2)
print(df2.dtypes)
df2_n = df2.to_numpy()
print(df2_n)
print(type(df2_n))
print(df2.dtypes)
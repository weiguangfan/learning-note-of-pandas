import numpy as np
import pandas as pd
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

print(df.shape)
print(df.dtypes)
print(df)
print(df.groupby("A"))
print(df.groupby("A")[["C","D"]])
print(df.groupby("A")[["C", "D"]].sum())
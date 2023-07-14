import pandas as pd
import numpy as np
tuples = list(
    zip(
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    )
)
print(tuples)

index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
print(type(index))
print(index)
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
print(df)
print(df.shape)
print(type(df))
df2 = df[:4]
print(df2)
print(df2.shape)
stacked = df2.stack()
print(stacked.shape)
print(stacked)
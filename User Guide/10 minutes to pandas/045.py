import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randn(10, 4))
print(type(df))
print(df)
print(df.shape)
pieces = [df[:3], df[3:7], df[7:]]
print(type(pieces))
print(pieces)
print(pd.concat(pieces))
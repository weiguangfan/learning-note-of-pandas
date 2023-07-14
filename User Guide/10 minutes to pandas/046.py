import numpy as np
import pandas as pd
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
print(left)
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
print(right)
print(pd.merge(left, right, on="key"))
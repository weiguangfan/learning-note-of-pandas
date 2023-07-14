import numpy as np
import pandas as pd
s = pd.Series(np.random.randint(0,7,size=10))
print(s.dtypes)
print(type(s))
print(s)
print(s.value_counts())
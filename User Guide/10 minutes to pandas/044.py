import numpy as np
import pandas as pd
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
print(s)
print(s.dtypes)
print(s.str.lower())
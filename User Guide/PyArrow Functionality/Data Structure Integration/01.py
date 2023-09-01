import pandas as pd
ser = pd.Series([-1.5, 0.2, None], dtype="float32[pyarrow]")
print(ser)
idx = pd.Index([True, None], dtype="bool[pyarrow]")
print(idx)
df = pd.DataFrame([[1, 2], [3, 4]], dtype="uint64[pyarrow]")
print(df)
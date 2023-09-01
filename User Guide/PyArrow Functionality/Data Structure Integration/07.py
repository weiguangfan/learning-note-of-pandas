import pandas as pd
import pyarrow as pa
ser = pd.Series([1, 2, None], dtype="uint8[pyarrow]")
print(ser)
print(pa.array(ser))
idx = pd.Index(ser)
print(idx)
print(pa.array(idx))
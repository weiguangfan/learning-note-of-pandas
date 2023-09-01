import pandas as pd
import pyarrow as pa

ser = pd.Series([-1.545, 0.211, None], dtype="float32[pyarrow]")
print(ser)
print(ser.mean())
print(ser + ser)
print(ser > (ser + 1))
print(ser.dropna())
print(ser.isna())
print(ser.fillna(0))


import pyarrow as pa
import pandas as pd
data = list("abc")
print(data)
ser_sd = pd.Series(data, dtype="string[pyarrow]")
print(ser_sd)
ser_ad = pd.Series(data, dtype=pd.ArrowDtype(pa.string()))
print(ser_ad)
print(ser_ad.dtype == ser_sd.dtype)
print(ser_sd.str.contains("a"))
print(ser_ad.str.contains("a"))
import pandas as pd
import pyarrow as pa

ser_str = pd.Series(["a", "b", None], dtype=pd.ArrowDtype(pa.string()))
print(ser_str)
print(ser_str.str.startswith("a"))




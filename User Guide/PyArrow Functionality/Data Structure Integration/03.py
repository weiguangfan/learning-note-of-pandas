import pyarrow as pa
import pandas as pd
list_str_type = pa.list_(pa.string())
print(list_str_type)
ser = pd.Series([["hello"], ["there"]], dtype=pd.ArrowDtype(list_str_type))
print(ser)
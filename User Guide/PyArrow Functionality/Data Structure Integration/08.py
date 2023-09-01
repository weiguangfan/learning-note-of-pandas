import pandas as pd
import pyarrow as pa
table = pa.table([pa.array([1, 2, 3], type=pa.int64())], names=["a"])
print(table)
df = table.to_pandas(types_mapper=pd.ArrowDtype)
print(df)
print(df.dtypes)


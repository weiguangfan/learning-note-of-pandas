import pyarrow as pa
import pandas as pd
import io
data = io.StringIO("""a,b,c,d,e,f,g,h,i
    1,2.5,True,a,,,,,
    3,4.5,False,b,6,7.5,True,a,
""")
print(data)
df_pyarrow = pd.read_csv(data, dtype_backend="pyarrow")
print(df_pyarrow)
print(df_pyarrow.dtypes)

import pandas as pd
import pyarrow as pa
import io
data = io.StringIO("""a,b,c
   1,2.5,True
   3,4.5,False
""")

print(data)
df = pd.read_csv(data, engine="pyarrow")
print(df)





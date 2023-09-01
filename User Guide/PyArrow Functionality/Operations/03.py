import pyarrow as pa
import pandas as pd
from datetime import datetime

print(datetime(2022, 1, 1))
pa_type = pd.ArrowDtype(pa.timestamp("ns"))
print(pa_type)
ser_dt = pd.Series([datetime(2022, 1, 1), None], dtype=pa_type)
print(ser_dt)
# print(ser_dt.dt.strftime("%Y-%m"))
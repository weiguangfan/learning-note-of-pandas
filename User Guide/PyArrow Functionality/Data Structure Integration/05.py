import pyarrow as pa
import pandas as pd
from decimal import Decimal
decimal_type = pd.ArrowDtype(pa.decimal128(3, scale=2))
print(decimal_type)
data = [[Decimal("3.19"), None], [None, Decimal("-1.23")]]
print(data)
df = pd.DataFrame(data, dtype=decimal_type)
print(df)
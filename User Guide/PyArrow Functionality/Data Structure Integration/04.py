import pyarrow as pa
import pandas as pd
from datetime import time

print(time(12, 30))
idx = pd.Index([time(12, 30), None], dtype=pd.ArrowDtype(pa.time64("us")))
print(idx)
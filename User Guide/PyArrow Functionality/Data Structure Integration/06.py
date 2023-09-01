import pyarrow as pa
import pandas as pd
pa_array = pa.array(
    [{"1": "2"}, {"10": "20"}, None],
    type=pa.map_(pa.string(), pa.string()),
)
print(pa_array)
ser = pd.Series(pd.arrays.ArrowExtensionArray(pa_array))
print(ser)


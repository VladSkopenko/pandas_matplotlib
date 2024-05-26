import numpy as np
import pandas as pd

data = pd.DataFrame([[1, 2, 3], [4, np.nan, 6], [7, np.nan, np.nan]], index=["one", "two", "three"],
                    columns=["a", "b", "c"])
print("do")
print(data)
data = data.fillna({"a": data["a"].mean(), "b": data["b"].mean(), "c": data["c"].mean()})
print("-" * 20)
print(data)

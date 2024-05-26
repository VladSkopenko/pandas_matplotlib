import numpy as np
import pandas as pd

data = pd.DataFrame([[1, 2, 3], [4, np.nan, 6], [7, np.nan, np.nan]])

print(data)
data = data.dropna(how="all")
print("--" * 20)
print("Режим how=all видаляєте лише  де весь рядок NaN")
print(data)
data = data.dropna(how="any")
print("--" * 20)
print("Режим how=any видаляєте лише  де хоча б один елемент NaN")
print(data)

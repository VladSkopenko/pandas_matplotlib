import pandas as pd

date = pd.Timestamp("2024-05-26 2:54:13")

print(type(date))
print(date)
print("--" * 20)

date = pd.to_datetime("2021-09-10 2:54:13")
print(type(date))
print(date)
print("--" * 20)
date = pd.date_range(start='2021-09-01', freq='D', periods=8) #freq - частота, periods - кількість днів

temperature = pd.Series([23, 17, 17, 16, 15, 14, 17, 20], index=date)

print(temperature)
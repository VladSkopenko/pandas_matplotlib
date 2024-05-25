import pandas as pd

print("--" * 20)
print("Orien colums КЛЮЧ(дефолт):СЛОВАРЬ(цифра:значение)")
columns = pd.read_json("columns.json", orient="columns")
print(columns)

print("--" * 20)
print("Orient values  масив значень.  [['1'],['2'],['3'],['4'],['5'],]")
values = pd.read_json("values.json", orient="values")
print(values)
print("--" * 20)
print("Orien colums КЛЮЧ(ЦИФРА):СЛОВАРЬ{дефолт}")
index = pd.read_json("index.json", orient="index")
print(index)


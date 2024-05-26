import pandas as pd

data1 = {
    "name": {"1": "Michael", "2": "John"},
    "country": {"1": "Canada", "2": "USA"},
    "age": {"1": 25, "2": 32}
}

employees1 = pd.DataFrame(data1)

data2 = {
    "name": {"3": "Liza", "4": "Jhon"},
    "country": {"3": "Australia", "4": "Denmark"},
    "age": {"3": 19, "4": 23}
}

employees2 = pd.DataFrame(data2)

employees = pd.concat([employees1, employees2])

print(employees)
print("--" * 20)
data1 = {
    "name": {"1": "Michael", "2": "John", "3": "Liza", "4": "Jhon"},
    "country": {"1": "Canada", "2": "USA", "3": "Australia", "4": "Denmark"}
}
employees1 = pd.DataFrame(data1)
data2 = {
    "age": {"1": 25, "2": 32, "3": 19, "4": 23}
}
employees2 = pd.DataFrame(data2)

employees = pd.concat([employees1, employees2], axis=1)

print(employees)

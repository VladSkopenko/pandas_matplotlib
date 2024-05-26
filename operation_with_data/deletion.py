import pandas as pd


print("Видалення елементів по індексу. pd.Series.drop([index1, index2, ...])")
numbers = pd.Series([1, 2, 3, 4, 5])
numbers.drop([1, 3], inplace=True)
print(numbers)
print("--" * 20)
print("З датафрейма тоже самое можна виконувати. pd.DataFrame.drop([index1, index2, ...]),"
      " axis=0 - для строк, axis=1 - для стовпців")
data = {
    "name": {"1": "Michael", "2": "John", "3": "Liza"},
    "country": {"1": "Canada", "2": "USA", "3": "Australia"},
    "age": {"1": 25, "2": 32, "3": 19}
}

employees = pd.DataFrame(data)
employees = employees.drop(["2"], axis=0)
employees = employees.drop(["age"], axis=1)
print(employees)


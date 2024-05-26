import pandas as pd


print("Щоб додати дані до структури Series, потрібно вказати новий індекс для об'єкта та задати значення елементу.")
data = pd.Series([1, 2, 3])
data[4] = 4
data[3] = 5
print(data)
print("--" * 20)
print("В датафрейм можна додати як обьект так і цілий стовпчик даних.")
data = {
    "name": {"1": "Michael", "2": "John", "3": "Liza"},
    "country": {"1": "Canada", "2": "USA", "3": "Australia"}
}
employees = pd.DataFrame(data)
employees["age"] = [25, 32, 19]
print(employees)
print("--" * 20)
print("за допомогою _append() можна додали сириес в фрейм ")
employees = pd.DataFrame(data)

new_employee = pd.Series(["Jhon", "Denmark", 23], ["name", "country", "age"])

employees = employees._append(new_employee, ignore_index=True)
print(employees)

import pandas as pd

data = {
    "name": ["Michael", "Steve", "Liza", "Jhon", "Liza", "Jhon"],
    "country": ["Canada", "USA", "Australia", "Denmark", "Australia", "Denmark"],
    "age": [25, 32, 19, 23, 19, 23]
}

employees = pd.DataFrame(data)
print("Для удаление дупликатов есть метод drop_duplicates()")
employees = employees.drop_duplicates()
print(employees)
print("--" * 20)
print("Для изменения данных которые не  нан  используется replace()")
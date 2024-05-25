import pandas as pd

print("Что бы прочитать 1 обьект json - lines=True")
user = pd.read_json("linestrue.json", lines=True, )
print(user)
print("--" * 20)
print("Что бы прочитать полноценный json  [{},{},{}] существует метод read_json()")
users = pd.read_json("record.json")
print(users)
print("--" * 20)
print("Режим рекорд когда КЛЮЧ:ЗНАЧЕНИЕ")
users = pd.read_json("record.json", orient="records")
print(users)
print("--" * 20)
print("Режим сплит нужен когда структура КЛЮЧ:СПИСОК")
employees = pd.read_json("split.json", orient="split")
print(employees)


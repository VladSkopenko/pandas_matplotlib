import pandas as pd

print("Что бы прочитать 1 обьект json - lines=True")
user = pd.read_json("user.json", lines=True)
print(user)
print("--" * 20)
print("Что бы прочитать полноценный json  [{},{},{}] существует метод read_json()")
users = pd.read_json("users.json")
print(users)

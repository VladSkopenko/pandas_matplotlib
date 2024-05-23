import pandas as pd

mountains_height = pd.Series(
    data=[2061, 2035.8, 2028.5, 2022.5, 2016.4],
    index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"],
    name="Height, m",
    dtype=float,
)
print("Слай по індексу  працює класично ")
print(mountains_height[1:3])
print("\n--------------------------\n")
print("Слай по іменованому індексу включає і перший і останній елементи")
print(mountains_height["Brebenskyl":"Petros"])

# если индексы стандартные то  последний не входит , если как словарь то входит


print("іменовані індекси є атрибутами обьекта і до них можна звертатись як звичайно ")
print(mountains_height.Petros)
print(mountains_height.Brebenskyl)

# Можна обрашаться как к атрибуту или к индексу

print("\n--------------------------\nОперація порівняння створює новий обьект типу Series\n")
new_object_series = (mountains_height > 2030)
print(new_object_series)
print("\n--------------------------\nОперація фільтрації створює новий обьект типу Series\n")
new_object_series = mountains_height[mountains_height > 2030]
print(new_object_series)
print("\n--------------------------\n")
print("Операція на входження in  перевіряє індекси а не значення")
print("Goverla" in mountains_height)

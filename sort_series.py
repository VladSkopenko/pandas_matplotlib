import pandas as pd


print("Методи сортуванн повертають новий обьект але за допомогою inplace=True можна оновити вихідний об'єкт.\n")

mountains_height = pd.Series(
    data=[2061, 2035.8, 2028.5, 2022.5, 2016.4],
    index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"],
    name="Height, m",
    dtype=float,
)
sort_index = mountains_height.sort_index()
print("Сортування за індексом    .sort_index()")
print(sort_index)
print("\n-----------------------------------------------\n")
sort_values = mountains_height.sort_values(ascending=True)
print("Сортування за значенням .sort_values()")
print('ascending=False визначає порядок сортування "за зменшенням"')
print(sort_values)

import pandas as pd

mountain_height = pd.Series([2061, 2035.8, 2028.5, 2022.5, 2016.4])

print(mountain_height, "\n--------------------------\n")


mountains_height = pd.Series(
    data=[2061, 2035.8, 2028.5, 2022.5, 2016.4],
    index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"],
    name="Height, m",
    dtype=float,
)

print(mountains_height)
# Можно звертатись по індексу
# По умолчанию индекси 0.1.2.3. но можно и как словарь сделать
print(mountains_height["Goverla"])
print(mountain_height[0])

# можно взяти в иншому порядку
print(mountains_height[["Pip_Ivan", "Goverla", "Gutin_Tomnatik"]])

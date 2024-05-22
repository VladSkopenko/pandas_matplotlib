import pandas as pd

mountains_height = pd.Series(
    data=[2061, 2035.8, 2028.5, 2022.5, 2016.4],
    index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"],
    name="Height, m",
    dtype=float,
)

print(mountains_height[1:3])
print("\n--------------------------\n")
print(mountains_height["Brebenskyl":"Petros"])

# если индексы стандартные то  последний не входит , если как словарь то входит

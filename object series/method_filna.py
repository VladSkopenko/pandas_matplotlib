import pandas as pd

mountains_height = pd.Series(
    {
        "Goverla": 2061,
        "Brebenskyl": 2035.8,
        "Pip_Ivan": 2028.5
    }
    ,
    index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"],
    name="Height, m",
    dtype=float,
)

print(mountains_height)
print("\n-----------------------------------------------\n")
print("Метод fillna замінює значення NaN на 12.0\n")
mountains_height.fillna(12.0, inplace=True)

print(mountains_height)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

 # встановлення стилю графіку

plt.figure(figsize=(10, 5)) # создали фигуру
sns.set_style("darkgrid") # встановлення стилю графіку
data = sns.load_dataset("mpg") # это просто берем с интернета


sns.lineplot(x='model_year', y='horsepower', hue="origin", data=data)


plt.title("Залежність швидкості авто від року випуску")
plt.xlabel("Рік випуску")
plt.ylabel("Максимальна швидкість")



plt.show()

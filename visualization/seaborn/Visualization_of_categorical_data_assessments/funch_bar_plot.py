import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("mpg")

sns.barplot(x="origin", y="mpg", data=data)
"""Функція будує стовпчасту діаграму: висота бару (стовпця) визначає чисельне значення оцінки ознаки
 (математичне очікування), лінія, що перетинає верхню межу бару - довірчий інтервал."""
plt.savefig('funch_bar_plot.png')
plt.show()

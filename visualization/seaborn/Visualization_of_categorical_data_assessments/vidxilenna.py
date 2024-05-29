import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("mpg")

sns.residplot(x="horsepower", y="displacement", data=data)
"""Різниця між значеннями оцінки ознаки та значеннями оцінки ознаки відображається на графіку"""


plt.savefig('residplot.png')
plt.show()

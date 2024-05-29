import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("mpg")  # это просто берем с интернета

sns.scatterplot(x='mpg', y='displacement', data=data, hue="origin")



plt.xlabel("Витрати палива")
plt.ylabel("Дальність пробігу")
plt.title("Залежність витрат палива від дальності пробігу")

plt.show()

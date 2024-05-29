import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("mpg")  # это просто берем с интернета

sns.scatterplot(x='mpg', y='displacement', data=data)



plt.xlabel("Витрати палива")
plt.ylabel("Об'єм двигуна")
plt.title("Залежність витрат палива від об'єму двигуна")

plt.show()

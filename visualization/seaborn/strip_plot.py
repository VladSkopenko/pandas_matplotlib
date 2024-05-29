import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("mpg")
print(data.head())

#sns.stripplot(x='origin', y='mpg', hue='cylinders', data=data) #  точки перекрывают друг друга


sns.swarmplot(x='origin', y='mpg', data=data, hue='cylinders') #  точки не перекрывают друг друга
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("mpg")

sns.relplot(x='mpg', y='displacement', kind='scatter', hue='origin', col='origin', data=data)

plt.show()

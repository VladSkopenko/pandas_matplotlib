import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("mpg")

sns.countplot(x="origin", data=data)

# распределение даных
plt.show()


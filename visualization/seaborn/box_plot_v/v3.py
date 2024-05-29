from seaborn import load_dataset
import matplotlib.pyplot as plt
import seaborn as sns

data = load_dataset("mpg")

sns.boxenplot(x="origin", y="mpg", data=data)

plt.savefig('boxenplot.png')
plt.show()

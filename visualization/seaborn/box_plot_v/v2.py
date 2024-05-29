from seaborn import load_dataset
import matplotlib.pyplot as plt
import seaborn as sns

data = load_dataset("mpg")

sns.violinplot(x="origin", y="mpg", data=data)

plt.savefig('violin_plot.png')
plt.show()

from seaborn import load_dataset
import matplotlib.pyplot as plt
import seaborn as sns

data = load_dataset("mpg")

sns.boxplot(x="origin", y="mpg", hue="cylinders", data=data)

plt.show()

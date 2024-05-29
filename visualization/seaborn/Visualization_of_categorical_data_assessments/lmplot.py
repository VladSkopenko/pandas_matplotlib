import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("mpg")

sns.lmplot(x="horsepower", y="displacement", hue="origin", col="origin", data=data)

plt.savefig('lmplot.png')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
from numpy import median

data = sns.load_dataset("mpg")

sns.lmplot(x="horsepower", y="displacement", data=data, x_estimator=median)

#діаграмf з медіанною оцінкою
plt.savefig('line_regres2.png')
plt.show()

import seaborn as sns
from matplotlib import pyplot as plt

data = sns.load_dataset("mpg")


sns.pointplot(x="origin", y="mpg", data=data)
#Відображає оцінку будь-якого набору даних як точку на полі графіка та довірчий інтервал у вигляді лінії, центр якої лежить на зазначеній точці.
plt.savefig('funk_poitn_plot.png')
plt.show()



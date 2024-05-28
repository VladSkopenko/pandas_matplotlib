import matplotlib.pyplot as plt

labels = [
    "Junior Software Engineer",
    "Senior Software Engineer",
    "Software Engineer",
    "System Architect",
    "Technical Lead",
]  # Назви для секцій в діаграмі

colors_list = ['gold', 'red', 'green', 'blue', 'orange']  # цвета для секцій

data = [63, 31, 100, 2, 11]  # кількістні характеристики даних, вони  перетворюються в відсоткове відношення
explode = [0.02, 0.01, 0.02, 0.0, 0]  # можна розділити
plt.pie(
    data,
    labels=labels,
    shadow=False,
    explode=explode,
    autopct="%.2f%%",
    pctdistance=1.15,
    labeldistance=1.35,
    colors=colors_list
)
plt.title("Розподіл програмістів Python за посадами", fontsize=17, fontweight="bold",)

plt.show()

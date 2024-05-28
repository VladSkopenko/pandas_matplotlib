import matplotlib.pyplot as plt


def add_values():
    """фукнція що додає значення до бара"""
    for i, value in enumerate(number_medals):
        plt.text(i, value + 0.5, str(value), ha='center', va='bottom', fontsize=10)


list_country = ["США", "Китай", "Японія", "Велика Британія"] # Тут ось x
number_medals = [39, 38, 27, 22]  # Тут ось y

plt.bar(
    list_country,
    number_medals,
    color=["b", "r", "y", "g"],
    edgecolor='black', # Это цвет границ
    linewidth=2,  # Толщина цвета границ
)

plt.xlabel("Країна", fontsize=25, color="black")
plt.ylabel("Кількість отриманих медалей", fontsize=14, color="black")

plt.title("Золоті медалі: Літня олімпіада Токіо 2020", fontsize=15)
add_values()

plt.show()

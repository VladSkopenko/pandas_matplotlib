import matplotlib.pyplot as plt
import pandas as pd

date = pd.date_range(start='2024-05-20', freq='D', periods=8)

fig, axs = plt.subplots()  # создает несколько графиков в одной фигуре

night_temp = [15, 13, 14, 15, 12, 16, 19, 19]
day_temp = [21, 20, 22, 21, 24, 21, 25, 21]

mid_temp = [(x + y) / 2 for x, y in zip(night_temp, day_temp)]

axs.plot(date, night_temp, label="Нічна темпетатура",
         color="#061358", linestyle=":", linewidth=2, marker="D",)  # добавляет график

axs.plot(date, day_temp, label="Денна темпетатура",
         color="#FF5733", linestyle=":", linewidth=2, marker="D")  # добавляет график

axs.plot(date, mid_temp, label="Середня темпетатура",
         color="green", linestyle=":", linewidth=2, marker="D")  # добавляет график


plt.ylim(10, 30) # Лимиты вертикальные


plt.xlabel("Дата", fontsize=14,
           color="black", loc="center",
           labelpad=10, rotation=0) # настройки лейбла

plt.ylabel("Температура повітря", fontsize=14,
           color="black", loc="center",
           labelpad=10, rotation=90) # настройки лейбла

plt.title("Денна та нічна температура повітря в Одесі", fontsize=16,
          color="black", loc="center", rotation=0) # настройка названия

plt.legend() # добавляет лейбы
plt.grid() # настройка сетки
plt.show()

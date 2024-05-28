import matplotlib.pyplot as plt
import pandas as pd

date = pd.date_range(start='2024-05-20', freq='D', periods=8)

fig, axs = plt.subplots()   # создает несколько графиков в одной фигуре

axs.plot(date, [15, 18, 14, 15, 18, 16, 19, 17], label="Нічна темпетатура") # добавляет график
axs.plot(date, [21, 20, 22, 21, 24, 21, 25, 21], label="Денна темпетатура") # добавляет график


plt.xlabel("Дата", fontsize=14,
           color="black", loc="center",
           labelpad=10, rotation=0)
plt.ylabel("Температура повітря", fontsize=14,
           color="black", loc="center",
           labelpad=10, rotation=90)
plt.title("Денна та нічна температура повітря в Одесі", fontsize=16,
          color="black", loc="center", rotation=0)
plt.legend()

plt.show()

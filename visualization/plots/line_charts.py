import matplotlib.pyplot as plt
import pandas as pd

date = pd.date_range(start='2024-05-20', freq='D',
                     periods=8)  # freq - частота, periods - кількість днів первий список это х
plt.plot(date, [23, 22, 24, 21, 23, 24, 24, 20], label='day temperature')  # второй список это у # Метод plot принимает x и y
plt.xlabel('Дата', fontsize=14, color='Red', fontweight='bold')  # подпись по оси Х
plt.ylabel('Температура', fontweight='bold', fontsize=14, color='Red')  # подпись по оси У
plt.title('Денна погода у м. Одеса', fontsize=15, )  # Назва графіка
plt.text(date[3], 24, 'Весна дуже тепла', color="Black", fontsize=12)  # Добавить надпись
plt.legend()

plt.show()

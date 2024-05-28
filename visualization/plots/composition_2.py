import matplotlib.pyplot as plt
import pandas as pd

date = pd.date_range(start='2024-05-20', freq='D', periods=8)
fig, axs = plt.subplots(2, 1)

axs[0].plot(date, [21, 20, 22, 21, 24, 21, 25, 21], label='day temperature')
axs[1].plot(date, [15, 18, 14, 15, 18, 16, 19, 17], label='night temperature')

axs[0].set_title('Денна', fontsize=10)
axs[1].set_title('Нічна', fontsize=10)

fig.suptitle('Температура в м. Одеса', fontsize=15)

plt.show()

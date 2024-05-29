import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("mpg")  # Общедоступный датасет
first_data = data.head(5)

sns.set_style("whitegrid")  # встановлення стилю графіку

date = pd.date_range(start="2024-05-28", freq="D", periods=8)
day_temperature = [23, 17, 17, 16, 15, 14, 17, 20]
night_temperature = [19, 11, 16, 11, 10, 10, 11, 16]

df = pd.DataFrame({'Дата': date, 'Денна температура': day_temperature, 'Нічна темпетарура': night_temperature})

plt.figure(figsize=(10, 5))
sns.lineplot(data=df)

plt.xlabel('Дата', fontsize=14, color='black', fontweight='bold')
plt.ylabel('Температура', fontweight='bold', fontsize=14, color='black')
plt.title('Денна та нічна температура повітря в Одесі', fontsize=15,
          color="black", loc="center", rotation=0, fontweight="bold")
plt.show()







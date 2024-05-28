import pandas as pd
import seaborn as sns

data = sns.load_dataset("mpg")  # Общедоступный датасет
first_data = data.head(5)

sns.set_style("whitegrid")  # встановлення стилю графіку

date = pd.date_range(start="2024-05-28", freq="D", periods=8)
day_temperature = [23, 17, 17, 16, 15, 14, 17, 20]
night_temperature = [19, 11, 16, 11, 10, 10, 11, 16]

dataframe = pd.DataFrame({'date': date, 'day_temperature': day_temperature, 'night_temperature': night_temperature})



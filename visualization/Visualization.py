import pandas as pd
import matplotlib.pyplot as plt

date = pd.date_range(start='2021-09-01', freq='D', periods=8)

temperature = pd.Series([23, 17, 17, 16, 15, 14, 17, 20], index=date)

temperature.plot()
plt.show()


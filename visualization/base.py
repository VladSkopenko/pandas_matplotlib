import matplotlib.pyplot as plt
import pandas as pd

date = pd.date_range(start='2000-01-01', freq='D', periods=8)#freq - частота, periods - кількість днів первий список это х
plt.plot(date, [23, 17, 17, 16, 15, 14, 17, 20]) #второй список это у
plt.show()

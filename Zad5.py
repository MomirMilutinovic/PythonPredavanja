import pandas as pd
import matplotlib.pyplot as plt
orders = pd.read_csv('orders.csv')
days = orders.groupby('order_dow').count()
days = days.sort_values('order_id',ascending = False)
print(days.head()['order_id'])

days.plot()
plt.show()
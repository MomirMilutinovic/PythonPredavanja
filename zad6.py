import pandas as pd
import matplotlib.pyplot as plt
orders = pd.read_csv('orders.csv')
days = orders.groupby('days_since_prior_order')
days = days['order_id']
print(days)

days.plot()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

orders = pd.DataFrame.from_csv('orders_products__prior.csv')
broj_narudzbina_po_korisniku = orders.groupby('user_id').count()

print(broj_narudzbina_po_korisniku.mean()['order_id'])

brpbn = broj_narudzbina_po_korisniku.groupby('order_id')['eval_set']
brpbn.plot()
plt.show()
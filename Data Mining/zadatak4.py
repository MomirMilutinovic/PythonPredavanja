import pandas as pd

orders = pd.read_csv('order_products__train.csv')
products = orders.groupby('product_id').count()
products = products.sort_values('reordered',ascending = False)
print(products.head()['order_id'])

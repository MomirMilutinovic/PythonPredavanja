import pandas as pd

data = pd.DataFrame.from_csv('orders.csv')
user_data = data['user_id']
product_data = pd.DataFrame.from_csv('products.csv')
productNumber_data = product_data['product_name']
order_data = data['order_number']
print("Korisnici: ",end = '')
print(user_data.count())
print("Porudzbine: ",end = '')
print(order_data.count())
print("Proizvodi: ",end = '')
print(productNumber_data.count())

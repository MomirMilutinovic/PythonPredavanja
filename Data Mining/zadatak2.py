import pandas as pd

data = pd.DataFrame.from_csv('order_products__train.csv')
data.groupby('order_id').count()
print('Porudzbina\tBroj proizvoda')
print(data.groupby('order_id').count()['product_id'])
broj_proizvoda_po_narudzbini = data.groupby('order_id').count()['product_id']
print(broj_proizvoda_po_narudzbini.mean())

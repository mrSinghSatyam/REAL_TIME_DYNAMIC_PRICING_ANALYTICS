#import library
import pandas as pd

#file loaded

#csv file loaded
orders = pd.read_csv("raw_data/orders.csv")
customers = pd.read_csv("raw_data/customers.csv")
order_items = pd.read_csv("raw_data/order_items.csv")
payments = pd.read_csv("raw_data/payments.csv")
products = pd.read_csv("raw_data/products.csv")
category_translation = pd.read_csv("raw_data/category_translation.csv")
reviews = pd.read_csv("raw_data/reviews.csv")
sellers = pd.read_csv("raw_data/sellers.csv")
geoloation = pd.read_csv("raw_data/geolocation.csv")


#print the file is loded successfully
print("All files loaded successfully")

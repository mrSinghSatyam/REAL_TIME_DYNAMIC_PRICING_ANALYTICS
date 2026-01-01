#import library
import pandas as pd

#File loaded
orders = pd.read_csv("raw_data/orders.csv")
customers = pd.read_csv("raw_data/customers.csv")
order_items = pd.read_csv("raw_data/order_items.csv")
payments = pd.read_csv("raw_data/payments.csv")
products = pd.read_csv("raw_data/products.csv")
category_translation = pd.read_csv("raw_data/category_translation.csv")
reviews = pd.read_csv("raw_data/reviews.csv")
sellers = pd.read_csv("raw_data/sellers.csv")
geoloation = pd.read_csv("raw_data/geolocation.csv")

# Orders
orders.drop_duplicates(inplace=True)

date_cols = {
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_customer_date',
    'order_estimated_delivered_date'
    }

for col in date_cols:
    if col in orders.columns:
        orders[col] = pd.to_datetime(orders[col],errors='coerce')
        
# customers
customers.drop_duplicates(inplace=True)
customers = customers.dropna(subset=["customer_id"])

# Order Items
order_items.drop_duplicates(inplace=True)
invalid_items = order_items[(order_items["price"] <= 0) | (order_items['freight_value'] < 0)]

order_items = order_items.drop(invalid_items.index)

# Payments
payments.drop_duplicates(inplace=True)
payments = payments[payments["payment_value"] >= 0]

# products
products.drop_duplicates(inplace=True)

# category Translation
category_translation.drop_duplicates(inplace=True)

# Reviews
reviews.drop_duplicates(inplace=True)
reviews["review_creation_date"] = pd.to_datetime(reviews["review_creation_date"], errors='coerce')

# sellers
sellers.drop_duplicates(inplace= True)

# geolocation
geoloation.drop_duplicates(inplace= True)


# Save clean file
orders.to_csv("cleaned_data/orders.csv", index= False)
customers.to_csv("cleaned_data/customers.csv", index= False)
order_items.to_csv("cleaned_data/order_items.csv", index= False)
payments.to_csv("cleaned_data/payments.csv", index= False)
products.to_csv("cleaned_data/products.csv", index = False)
category_translation.to_csv("cleaned_data/category_translation.csv", index= False)
reviews.to_csv("cleaned_data/reviews.csv", index= False)
sellers.to_csv("cleaned_data/sellers.csv", index= False)
geoloation.to_csv("cleaned_data/geoloation.csv", index= False)



#print all files clean and saved
print("All file cleaned and saved!")

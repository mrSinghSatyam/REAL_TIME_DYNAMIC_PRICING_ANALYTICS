#import library
import pandas as pd

#Load clean + feature-engineering files
orders = pd.read_csv("cleaned_data/orders.csv")
customers = pd.read_csv("cleaned_data/customers.csv")
order_items = pd.read_csv("cleaned_data/order_items.csv")
payments = pd.read_csv("cleaned_data/payments.csv")
products = pd.read_csv("cleaned_data/products.csv")
category_translation = pd.read_csv("cleaned_data/category_translation.csv")
reviews = pd.read_csv("cleaned_data/reviews.csv")
sellers = pd.read_csv("cleaned_data/sellers.csv")

# Cors merge
df = orders.merge(customers, on="customer_id",how="left")
df = df.merge(order_items,on="order_id",how="left")
df = df.merge(payments, on="order_id", how= "left")
df = df.merge(products, on= "product_id", how="left")
df = df.merge(category_translation, on="product_category_name",how="left")
df = df.merge(reviews[["order_id","review_score"]], on="order_id",how="left")
df = df.merge(sellers[["seller_id", "seller_city","seller_state"]],on="seller_id",how="left")

#Save merge file
df.to_csv("cleaned_data/merge_data.csv",index=False)



print("Valid dataset merged successfully")

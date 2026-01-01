import pandas as pd

df = pd.read_csv("cleaned_data/featured_data.csv")

def dynamic_price(row):
    price = row['price']
    
    if 18 <= row["order_hour"] <= 22:
        price *= 1.15  
        
    if row["rating_category"] == "High":
        price *= 1.05
    elif row["rating_category"] == "Medium":
        price *= 1.02
    elif row["rating_category"] == "Low":
        price *= 0.95
        
    return round(price,2)

df["dynamic_price"] = df.apply(dynamic_price,axis=1)

df["dynamic_revenue"] = df["dynamic_price"] + df["freight_value"]

df.to_csv("cleaned_data/final_business_data.csv",index=False)

print("Dynamic price logic applied")

#import library
import pandas as pd

#load data
df = pd.read_csv("cleaned_data/merge_data.csv")

df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])

df["order_hour"] = df["order_purchase_timestamp"].dt.hour
df["order_day"]  = df["order_purchase_timestamp"].dt.day
df["order_month"] = df["order_purchase_timestamp"].dt.month


df["revenue"] = df["price"] + df["freight_value"]


def rating_category(score):
    if pd.isna(score):
        return "Unknown"
    elif score >= 4:
        return "High"
    elif score == 3:
        return "Medium"
    else:
        return "Low"
    
df["rating_category"] = df["review_score"].apply(rating_category)

state_map = {
    "AC": "Acre", "AL": "Alagoas", "AP": "Amapá", "AM": "Amazonas",
    "BA": "Bahia", "CE": "Ceará", "DF": "Distrito Federal",
    "ES": "Espírito Santo", "GO": "Goiás", "MA": "Maranhão",
    "MT": "Mato Grosso", "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais", "PA": "Pará", "PB": "Paraíba",
    "PR": "Paraná", "PE": "Pernambuco", "PI": "Piauí",
    "RJ": "Rio de Janeiro", "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul", "RO": "Rondônia", "RR": "Roraima",
    "SC": "Santa Catarina", "SP": "São Paulo",
    "SE": "Sergipe", "TO": "Tocantins"
}

if 'customer_state' in df.columns:
    df["customer_state"] = df["customer_state"].map(state_map)

if 'seller_state' in df.columns:
    df["seller_state"] = df["seller_state"].map(state_map)
    
df.to_csv("cleaned_data/featured_data.csv",index=False)
    
#print 
print("Feature engineering done!")

import pandas as pd
from sqlalchemy import create_engine

# Load CSV
df = pd.read_csv("data/online_retail_II.csv", encoding="ISO-8859-1")

# Clean data
df = df.dropna(subset=["Customer ID"])  # Remove null customers
df["Customer ID"] = df["Customer ID"].astype(str)

# Connect to PostgreSQL
engine = create_engine("postgresql+psycopg2://ecommerce_user:ecommerce_pass@localhost:5432/ecommerce_db")

# Upload
df.to_sql("raw_transactions", con=engine, if_exists="replace", index=False)

print("✅ Data loaded to PostgreSQL successfully!")

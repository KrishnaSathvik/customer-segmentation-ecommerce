import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# ✅ Step 1: Connect to PostgreSQL & Load RFM Features
print("🔗 Connecting to PostgreSQL and loading RFM features...")
engine = create_engine("postgresql+psycopg2://ecommerce_user:ecommerce_pass@localhost:5432/ecommerce_db")
df = pd.read_sql("SELECT * FROM customer_rfm", con=engine)
df.dropna(inplace=True)
print(f"✅ Loaded {len(df)} rows.")

# ✅ Step 2: Feature Scaling
print("⚖️ Scaling RFM features...")
X = df[['recency_days', 'frequency', 'monetary']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ✅ Optional: Elbow Method to determine best k
# sse = []
# for k in range(1, 11):
#     kmeans = KMeans(n_clusters=k, random_state=42)
#     kmeans.fit(X_scaled)
#     sse.append(kmeans.inertia_)
#
# plt.plot(range(1, 11), sse, marker='o')
# plt.xlabel("Number of Clusters (k)")
# plt.ylabel("SSE")
# plt.title("Elbow Method")
# plt.grid(True)
# plt.show()

# ✅ Step 3: Apply KMeans
k = 4  # You can change this based on elbow method
print(f"🔀 Applying KMeans with k={k}...")
kmeans = KMeans(n_clusters=k, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)
print("✅ Clusters assigned.")

# ✅ Step 4: Label Clusters Before Profiling
cluster_labels = {
    0: "Dormant Customers",
    1: "Regular Shoppers",
    2: "High-Value Loyalists",
    3: "Elite VIPs"
}
df['cluster_label'] = df['cluster'].map(cluster_labels)

# ✅ Step 5: Profile the Clusters (with labels)
profile = df.groupby(["cluster", "cluster_label"]).agg({
    "recency_days": "mean",
    "frequency": "mean",
    "monetary": "mean",
    "customer_id": "count"
}).rename(columns={"customer_id": "num_customers"}).reset_index()

print("\n📊 Cluster Profiles with Labels:")
print(profile)

# ✅ Step 6: Export to PostgreSQL and CSV
print("\n💾 Saving enhanced customer clusters to PostgreSQL and CSV...")
df.to_sql("customer_clusters", con=engine, if_exists="replace", index=False)
df.to_csv("data/customer_clusters.csv", index=False)
print("✅ Done. Results saved successfully!")

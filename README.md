# 🛒 Customer Segmentation for E-Commerce

Cluster customers based on transaction behavior using RFM metrics and KMeans to power targeted marketing. End-to-end project using PostgreSQL, DBT, Python, and Tableau.

---

## 🚀 Project Overview

This project analyzes customer behavior by:
- Extracting e-commerce data from PostgreSQL
- Transforming it into Recency, Frequency, and Monetary (RFM) features using **DBT**
- Clustering customers using **KMeans** in **Python**
- Visualizing insights in **Tableau**

---

## 🧰 Tech Stack

| Tool         | Purpose                                  |
|--------------|------------------------------------------|
| PostgreSQL   | Data storage for transaction history     |
| DBT          | Data transformation + modeling (RFM)     |
| Python       | Feature scaling + KMeans clustering      |
| Tableau      | Interactive dashboarding & reporting     |
| Pandas, Sklearn, SQLAlchemy | Data processing + modeling |

---

## 📁 Project Structure

```
customer-segmentation-ecommerce/
├── data/
│   └── customer_clusters.csv
├── dbt_project/
│   └── ecommerce_segmentation/
│       └── models/customer_rfm.sql
├── notebooks/
│   └── segmentation.py
├── scripts/
│   └── load_to_postgres.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 RFM Feature Engineering (DBT)

SQL transformation in `customer_rfm.sql`:

- **Recency**: Days since last purchase
- **Frequency**: Number of unique invoices
- **Monetary**: Total spend

Run with:

```bash
cd dbt_project/ecommerce_segmentation
dbt run
```

---

## 🤖 KMeans Clustering (Python)

Script: `notebooks/segmentation.py`

- Scales RFM features
- Finds optimal clusters (Elbow method)
- Applies KMeans (`k=4`)
- Adds human-readable `cluster_label`

```bash
python notebooks/segmentation.py
```

Example cluster profiles:

| Cluster | Label                  | Recency ↓ | Frequency ↑ | Monetary ↑ |
|---------|------------------------|-----------|--------------|-------------|
| 0       | Dormant Customers      | High      | Low          | Low         |
| 1       | Regular Shoppers       | Medium    | Medium       | Medium      |
| 2       | High-Value Loyalists   | Medium    | High         | High        |
| 3       | Elite VIPs             | Low       | Very High    | Very High   |

---

## 📊 Tableau Dashboard

**Data source**: `data/customer_clusters.csv`

Recommended dashboards:
1. **Pie Chart** – Customer count by `cluster_label`
2. **Recency vs Frequency** – Size = `monetary`, Color = `cluster_label`
3. **Frequency vs Monetary** – High-spenders & frequent buyers
4. (Optional) Map by country if location exists

---

## 🛠️ How to Run Locally

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run DBT to build RFM view:

```bash
dbt run
```

3. Run clustering and export results:

```bash
python notebooks/segmentation.py
```

4. Open Tableau → Load `data/customer_clusters.csv`

---

## 📌 Requirements

```
pandas
scikit-learn
sqlalchemy
psycopg2-binary
matplotlib
dbt-postgres
```
Save with: `pip freeze > requirements.txt`

---

## 🧠 Insights & Use Cases

- 🎯 Target high-value loyalists with VIP perks
- 💸 Re-engage dormant customers with discounts
- 🛍️ Upsell to regular shoppers

---

## 📄 License

MIT © 2025 Krishna Sathvik

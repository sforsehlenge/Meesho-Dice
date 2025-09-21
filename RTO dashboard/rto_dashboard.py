# Install dependencies if not installed:
# pip install streamlit pandas plotly

import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# Step 1: Load dataset
# -------------------------------
data = pd.read_csv("/Users/sumankumar/Desktop/Meesho/RTO dashboard/rto_orders_india.csv")


# -------------------------------
# Step 2: Dashboard title
# -------------------------------
st.title("📊 RTO Monitoring Dashboard (Indian Cities)")

# -------------------------------
# Step 3: RTO hotspots by city
# -------------------------------
city_summary = data.groupby('city')['is_rto'].mean().reset_index()
fig_city = px.bar(city_summary.sort_values("is_rto", ascending=False).head(15),
                  x='city', y='is_rto',
                  title="Top 15 Cities by RTO Rate",
                  labels={'is_rto':'RTO Rate', 'city':'City'})
st.plotly_chart(fig_city)

# -------------------------------
# Step 4: RTO hotspots by product
# -------------------------------
product_summary = data.groupby('product')['is_rto'].mean().reset_index()
fig_product = px.bar(product_summary, x='product', y='is_rto',
                     title="RTO Rate by Product", labels={'is_rto':'RTO Rate'})
st.plotly_chart(fig_product)

# -------------------------------
# Step 5: RTO hotspots by seller
# -------------------------------
seller_summary = data.groupby('seller')['is_rto'].mean().reset_index()
fig_seller = px.bar(seller_summary, x='seller', y='is_rto',
                    title="RTO Rate by Seller", labels={'is_rto':'RTO Rate'})
st.plotly_chart(fig_seller)

# -------------------------------
# Step 6: Alerts
# -------------------------------
st.subheader("⚠️ Automated Alerts")

threshold = 0.4  # e.g., 40% RTO is considered high risk
high_rto_cities = city_summary[city_summary['is_rto'] > threshold]['city'].tolist()

if high_rto_cities:
    st.error(f"High RTO detected in cities: {', '.join(high_rto_cities)}")
else:
    st.success("No high RTO cities detected ✅")


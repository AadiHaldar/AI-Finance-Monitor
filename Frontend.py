import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Flask API URL
API_URL = "http://127.0.0.1:5000"

# App Title
st.title("💰 Budget Forecasting & Anomaly Detection")

# 📌 Fetch Financial Transactions
st.subheader("📊 Financial Transactions")
response = requests.get(f"{API_URL}/financial_data")

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    
    # Convert 'date' column to datetime and extract just the date part
    df['date'] = pd.to_datetime(df['date'], errors='coerce', utc=True).dt.date
    
    st.write(df)  # Display transactions
else:
    st.error("Failed to fetch financial data")

# 📌 Budget Forecasting with Fenwick Tree
st.subheader("📈 Budget Forecasting")

# User selects a date to check cumulative budget
date_query = st.date_input("Select a date for budget forecast")
if st.button("Get Budget Forecast"):
    response = requests.get(f"{API_URL}/budget_query?date={date_query}")
    if response.status_code == 200:
        budget_data = response.json()
        st.success(f"💰 Total Budget up to {date_query}: ${budget_data['total_budget']}")
    else:
        st.error("Failed to fetch budget forecast")

# 📌 Budget Trend Visualization (Plotly)
st.subheader("📊 Budget Trend Visualization")
if not df.empty:
    df_sorted = df.sort_values("date")
    fig = px.line(df_sorted, x="date", y="amount", title="Budget Over Time", markers=True)
    st.plotly_chart(fig)

# 📌 Budget Between Two Dates
st.subheader("📊 Budget Between Two Dates")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

if st.button("Get Budget Range"):
    response = requests.get(f"{API_URL}/budget_range_query?start_date={start_date}&end_date={end_date}")
    if response.status_code == 200:
        range_data = response.json()
        st.success(f"🔍 Budget from {start_date} to {end_date}: ${range_data['range_budget']}")
    else:
        st.error("Failed to fetch range budget")

# 📌 Add a New Transaction
st.subheader("➕ Add a Transaction")
date = st.date_input("Transaction Date")
amount = st.number_input("Amount", step=0.01)
category = st.text_input("Category")
transaction_type = st.selectbox("Transaction Type", ["Income", "Expense"])
payment_method = st.selectbox("Payment Method", ["Cash", "Credit Card", "UPI", "Net Banking"])

if st.button("Submit Transaction"):
    payload = {
        "date": str(date),
        "amount": amount,
        "category": category,
        "transaction_type": transaction_type,
        "payment_method": payment_method
    }
    response = requests.post(f"{API_URL}/add_transaction", json=payload)

    if response.status_code == 200:
        st.success("Transaction added successfully!")
    else:
        st.error("Failed to add transaction")

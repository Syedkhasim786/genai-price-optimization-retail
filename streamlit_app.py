import streamlit as st
import requests

st.title("🧠 AI Price Optimization Assistant")

product = st.text_input("Product Name")
cost = st.number_input("Cost Price", value=1000)
competitor = st.number_input("Competitor Price", value=1500)
demand = st.selectbox("Demand", ["low", "medium", "high"])
stock = st.selectbox("Stock", ["low", "medium", "high"])

if st.button("Optimize Price"):
    
    https://genai-price-optimization-retail.onrender.com/
    
    params = {
        "product": product,
        "cost": cost,
        "competitor": competitor,
        "demand": demand,
        "stock": stock
    }

    response = requests.post(url, params=params)

    if response.status_code == 200:
        data = response.json()
        st.success(f"Recommended Price: ₹{data['recommended_price']}")
        st.write(data["explanation"])
    else:
        st.error("Error fetching result")

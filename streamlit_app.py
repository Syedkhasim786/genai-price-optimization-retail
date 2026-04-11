import streamlit as st
import requests

st.title("🧠 AI Price Optimization Assistant")

product = st.text_input("Product Name")
cost = st.number_input("Cost Price", value=1000)
competitor = st.number_input("Competitor Price", value=1500)
demand = st.selectbox("Demand", ["low", "medium", "high"])
stock = st.selectbox("Stock", ["low", "medium", "high"])

if st.button("Optimize Price"):

    url = "https://genai-price-optimization-retail.onrender.com/optimize-price"

    params = {
        "product": product,
        "cost": float(cost),
        "competitor": float(competitor),
        "demand": demand,
        "stock": stock
    }

    try:
        response = requests.post(url, params=params, timeout=30)

        # 🔍 Debug info (keep this for now)
        st.write("Status Code:", response.status_code)
        st.write("Response:", response.text)

        if response.status_code == 200:
            data = response.json()
            st.success(f"Recommended Price: ₹{data['recommended_price']}")
            st.write(data["explanation"])
        else:
            st.error("Backend error. Check response above.")

    except requests.exceptions.RequestException as e:
        st.error(f"Connection error: {e}")

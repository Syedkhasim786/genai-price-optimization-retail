import streamlit as st
import requests

st.set_page_config(page_title="AI Price Optimizer", page_icon="🧠")

st.title("🧠 AI Price Optimization Assistant")

# Inputs
product = st.text_input("Product Name", placeholder="e.g. Running Shoes")
cost = st.number_input("Cost Price", min_value=0.0, value=1000.0)
competitor = st.number_input("Competitor Price", min_value=0.0, value=1500.0)
demand = st.selectbox("Demand", ["low", "medium", "high"])
stock = st.selectbox("Stock", ["low", "medium", "high"])

# Button
if st.button("Optimize Price"):

    if not product:
        st.warning("Please enter product name")
    else:
        url = "https://genai-price-optimization-retail.onrender.com/optimize-price"

        params = {
            "product": product,
            "cost": float(cost),
            "competitor": float(competitor),
            "demand": demand,
            "stock": stock
        }

        with st.spinner("Optimizing price..."):

            try:
                response = requests.post(url, params=params, timeout=30)

                # Debug (keep for now)
                st.write("Status Code:", response.status_code)
                st.write("Response:", response.text)

                if response.status_code == 200:
                    data = response.json()

                    st.success(f"💰 Recommended Price: ₹{data['recommended_price']}")
                    st.info(f"🤖 AI Insight: {data['explanation']}")

                else:
                    st.error("❌ Backend error. Check debug response above.")

            except requests.exceptions.RequestException as e:
                st.error(f"⚠️ Connection error: {e}")

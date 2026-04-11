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
        "cost": cost,
        "competitor": competitor,
        "demand": demand,
        "stock": stock
    }

    try:
        response = requests.post(url, params=params, timeout=30)

        st.write(f"Status Code: `{response.status_code}`")

        if response.status_code == 200:
            data = response.json()
            st.success(f"✅ Recommended Price: ₹{data['recommended_price']}")
            st.write("**Strategy Explanation:**")
            st.info(data["explanation"])
        else:
            st.error(f"❌ Backend error: {response.text}")

    except requests.exceptions.Timeout:
        st.warning("⏳ Request timed out. Render free tier may be sleeping — wait 30 seconds and try again.")
    except requests.exceptions.ConnectionError:
        st.error("🔌 Cannot connect to backend. Check if your Render service is running.")
    except Exception as e:
        st.error(f"Unexpected error: {e}")

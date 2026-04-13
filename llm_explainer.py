import os
import google.generativeai as genai

# API key is loaded from environment variable GEMINI_API_KEY
# Set this in Render dashboard → Environment → Add Variable
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_explanation(product, cost, comp, demand, stock, price):
    prompt = f"""
    Product: {product}
    Cost Price: {cost}
    Competitor Price: {comp}
    Demand: {demand}
    Stock: {stock}
    Suggested Price: {price}
    Explain the pricing strategy in simple business terms in 3-4 sentences.
    """
    response = model.generate_content(prompt)
    return response.text

import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

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

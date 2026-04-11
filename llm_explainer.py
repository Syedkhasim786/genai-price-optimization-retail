import os
from openai import OpenAI

# API key is loaded from environment variable OPENAI_API_KEY
# Set this in Render dashboard → Environment → Add Variable
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

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

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

from openai import OpenAI

client = OpenAI()

def generate_explanation(product, cost, comp, demand, stock, price):
    prompt = f"""
    Product: {product}
    Cost Price: {cost}
    Competitor Price: {comp}
    Demand: {demand}
    Stock: {stock}
    Suggested Price: {price}

    Explain the pricing strategy in simple business terms.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

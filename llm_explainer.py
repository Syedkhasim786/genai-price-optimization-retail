import anthropic

client = anthropic.Anthropic()  # uses ANTHROPIC_API_KEY env var

def generate_explanation(product, cost, comp, demand, stock, price):
    prompt = f"""
    Product: {product}, Cost: {cost}, Competitor: {comp}
    Demand: {demand}, Stock: {stock}, Suggested Price: {price}
    Explain the pricing strategy in simple business terms.
    """
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text

def calculate_price(cost_price, competitor_price, demand, stock):
    price = cost_price * 1.3

    if demand == "high":
        price *= 1.2
    elif demand == "low":
        price *= 0.9

    if stock == "high":
        price *= 0.85
    elif stock == "low":
        price *= 1.1

    if competitor_price:
        price = min(price, competitor_price * 0.95)

    return round(price, 2)

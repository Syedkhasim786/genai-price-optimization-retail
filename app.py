from fastapi import FastAPI
from pricing_logic import calculate_price
from llm_explainer import generate_explanation

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GenAI Price Optimization API 🚀"}

@app.post("/optimize-price")
def optimize_price(product: str, cost: float, competitor: float, demand: str, stock: str):
    
    price = calculate_price(cost, competitor, demand, stock)
    
    explanation = generate_explanation(
        product, cost, competitor, demand, stock, price
    )

    return {
        "product": product,
        "recommended_price": price,
        "explanation": explanation
    }

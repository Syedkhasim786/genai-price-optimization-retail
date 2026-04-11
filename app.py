from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pricing_logic import calculate_price
from llm_explainer import generate_explanation
import os

app = FastAPI(title="GenAI Price Optimization API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "GenAI Price Optimization API 🚀", "status": "running"}

@app.post("/optimize-price")
def optimize_price(product: str, cost: float, competitor: float, demand: str, stock: str):
    try:
        price = calculate_price(cost, competitor, demand, stock)
        explanation = generate_explanation(product, cost, competitor, demand, stock, price)
        return {
            "product": product,
            "recommended_price": price,
            "explanation": explanation
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

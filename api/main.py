# main.py

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import customers, reviews, orders
from .dependencies.database import engine
from .models import model_loader
from .dependencies.config import conf

# FastAPI app instance
app = FastAPI()

# CORS settings
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database models
model_loader.index()

# Include routers
app.include_router(customers.router)
app.include_router(reviews.router)
app.include_router(orders.router)  # Ensure orders is defined properly

if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)

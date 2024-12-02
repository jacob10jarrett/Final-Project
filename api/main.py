import uvicorn
import schemas
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import index as indexRoute
from .models import model_loader
from .controllers import customers
from .dependencies.config import conf
from .dependencies.database import engine, get_db


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader.index()
indexRoute.load_routes(app)

@app.post("/customers/", response_model=schemas.Customer, tags=["Customers"])
def create_customer(customer: schemas.OrderCreate, db: Session = Depends(get_db)):
    return customers.create(db=db, customer=customer)


@app.get("/customers/", response_model=list[schemas.Customer], tags=["Customers"])
def read_customers(db: Session = Depends(get_db)):
    return customers.read_all(db)


@app.get("/customers/{customer_id}", response_model=schemas.Customer, tags=["Customers"])
def read_one_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = customers.read_one(db, customer_id=customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="User not found")
    return customer


@app.put("/customers/{customer_id}", response_model=schemas.Customer, tags=["Customers"])
def update_one_customer(customer_id: int, customer: schemas.OrderUpdate, db: Session = Depends(get_db)):
    customer_db = customers.read_one(db, customer_id=customer_id)
    if customer_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return customers.update(db=db, customer=customer, customer_id=customer_id)


@app.delete("/customers/{customer_id}", tags=["Customers"])
def delete_one_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = customers.read_one(db, customer_id=customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="User not found")
    return customers.delete(db=db, customer_id=customer_id)


if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)
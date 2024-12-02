import uvicorn
import schemas
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import index as indexRoute
from .models import model_loader
from .controllers import customers, reviews
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
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
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
def update_one_customer(customer_id: int, customer: schemas.CustomerUpdate, db: Session = Depends(get_db)):
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

@app.post("/reviews/", response_model=schemas.Review, tags=["Reviews"])
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return reviews.create(db=db, review=review)


@app.get("/reviews/", response_model=list[schemas.Review], tags=["Reviews"])
def read_reviews(db: Session = Depends(get_db)):
    return reviews.read_all(db)


@app.get("/reviews/{review_id}", response_model=schemas.Review, tags=["Reviews"])
def read_one_review(review_id: int, db: Session = Depends(get_db)):
    review = reviews.read_one(db, review_id=review_id)
    if review is None:
        raise HTTPException(status_code=404, detail="User not found")
    return review


@app.put("/reviews/{review_id}", response_model=schemas.Review, tags=["Reviews"])
def update_one_review(review_id: int, review: schemas.ReviewUpdate, db: Session = Depends(get_db)):
    review_db = reviews.read_one(db, review_id=review_id)
    if review_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return reviews.update(db=db, review=review, review_id=review_id)


@app.delete("/reviews/{review_id}", tags=["Reviews"])
def delete_one_review(review_id: int, db: Session = Depends(get_db)):
    review = reviews.read_one(db, review_id=review_id)
    if review is None:
        raise HTTPException(status_code=404, detail="User not found")
    return reviews.delete(db=db, review_id=review_id)


if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)
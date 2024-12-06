from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import customers as controller
from ..schemas.customers import CustomerCreate, CustomerUpdate, Customer
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Customers'],
    prefix="/customers"
)

@router.post("/", response_model=Customer)
def create_customer(request: CustomerCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[Customer])
def read_all_customers(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=Customer)
def read_one_customer(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=Customer)
def update_customer(item_id: int, request: CustomerUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)

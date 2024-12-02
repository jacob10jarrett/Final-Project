from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..controllers import promotion as controller
from ..schemas import promotion as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Promotions'],
    prefix="/promotions"
)

@router.post("/", response_model=schema.Promotion, status_code=status.HTTP_201_CREATED)
def create(request: schema.PromotionCreate, db: Session = Depends(get_db)) -> schema.Promotion:
    return controller.create(db=db, request=request)

@router.get("/", response_model=List[schema.Promotion])
def read_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> List[schema.Promotion]:
    return controller.read_all(db=db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=schema.Promotion)
def read_one(item_id: int, db: Session = Depends(get_db)) -> schema.Promotion:
    return controller.read_one(db=db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.Promotion, status_code=status.HTTP_200_OK)
def update(item_id: int, request: schema.PromotionUpdate, db: Session = Depends(get_db)) -> schema.Promotion:
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, db: Session = Depends(get_db)) -> None:
    controller.delete(db=db, item_id=item_id)

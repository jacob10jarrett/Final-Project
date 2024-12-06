from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import reviews as controller
from ..schemas.reviews import ReviewCreate, ReviewUpdate, Review
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Reviews'],
    prefix="/reviews"
)

@router.post("/", response_model=Review)
def create_review(request: ReviewCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[Review])
def read_all_reviews(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=Review)
def read_one_review(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=Review)
def update_review(item_id: int, request: ReviewUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_review(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)

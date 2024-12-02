from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.ingredients import Ingredient
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_ingredient = Ingredient(
        Name=request.Name,
        Unit=request.Unit,
        Amount=request.Amount
    )
    try:
        db.add(new_ingredient)
        db.commit()
        db.refresh(new_ingredient)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_ingredient


def read_all(db: Session):
    return db.query(Ingredient).all()


def read_one(db: Session, ingredient_id: int):
    ingredient = db.query(Ingredient).filter(Ingredient.IngredientID == ingredient_id).first()
    if not ingredient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ingredient not found")
    return ingredient


def update(db: Session, ingredient_id: int, request):
    ingredient = db.query(Ingredient).filter(Ingredient.IngredientID == ingredient_id)
    if not ingredient.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ingredient not found")
    ingredient.update(request.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return ingredient.first()


def delete(db: Session, ingredient_id: int):
    ingredient = db.query(Ingredient).filter(Ingredient.IngredientID == ingredient_id)
    if not ingredient.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ingredient not found")
    ingredient.delete(synchronize_session=False)
    db.commit()
    return {"message": "Ingredient deleted"}

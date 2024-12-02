from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.menu_items import MenuItem
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_menu_item = MenuItem(
        dishes=request.dishes,
        category=request.category,
        calories=request.calories,
        price=request.price
    )
    try:
        db.add(new_menu_item)
        db.commit()
        db.refresh(new_menu_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_menu_item

def read_all(db: Session):
    return db.query(MenuItem).all()

def read_one(db: Session, menu_item_id: int):
    menu_item = db.query(MenuItem).filter(MenuItem.id == menu_item_id).first()
    if not menu_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found")
    return menu_item

def update(db: Session, menu_item_id: int, request):
    menu_item = db.query(MenuItem).filter(MenuItem.id == menu_item_id)
    if not menu_item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found")
    menu_item.update(request.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return menu_item.first()

def delete(db: Session, menu_item_id: int):
    menu_item = db.query(MenuItem).filter(MenuItem.id == menu_item_id)
    if not menu_item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found")
    menu_item.delete(synchronize_session=False)
    db.commit()
    return {"message": "Menu item deleted"}

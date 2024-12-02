from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import menu_items as controller
from ..schemas.menu_items import MenuItemCreate, MenuItem, MenuItemUpdate
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/menu_items",
    tags=["Menu Items"]
)

@router.post("/", response_model=MenuItem)
def create_menu_item(request: MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[MenuItem])
def read_menu_items(db: Session = Depends(get_db)):
    return controller.read_all(db=db)

@router.get("/{menu_item_id}", response_model=MenuItem)
def read_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db=db, menu_item_id=menu_item_id)

@router.put("/{menu_item_id}", response_model=MenuItem)
def update_menu_item(menu_item_id: int, request: MenuItemUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, menu_item_id=menu_item_id, request=request)

@router.delete("/{menu_item_id}")
def delete_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, menu_item_id=menu_item_id)

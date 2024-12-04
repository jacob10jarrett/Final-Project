from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import order_details as model, orders, menu_items
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.OrderDetail(
        order_id=request.order_id,
        menu_item_id=request.menu_item_id,
        quantity=request.quantity,
        price=request.price
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item



def read_all(db: Session):
    try:
        result = db.query(model.OrderDetail).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.OrderDetail).filter(model.OrderDetail.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    # Validate the existence of order_id if it is being updated
    if request.order_id:
        order = db.query(orders.Order).filter(orders.Order.id == request.order_id).first()
        if not order:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Order with id {request.order_id} does not exist."
            )

    # Validate the existence of menu_item_id if it is being updated
    if request.menu_item_id:
        menu_item = db.query(menu_items.MenuItem).filter(menu_items.MenuItem.menuItemID == request.menu_item_id).first()
        if not menu_item:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Menu item with id {request.menu_item_id} does not exist."
            )

    try:
        item = db.query(model.OrderDetail).filter(model.OrderDetail.id == item_id)
        if not item.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="OrderDetail with the given id does not exist."
            )
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error_message = str(e.__dict__.get('orig', e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Database error: {error_message}"
        )
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.OrderDetail).filter(model.OrderDetail.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

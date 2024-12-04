from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import orders as model
from ..models.orders import Order
from ..models.order_details import OrderDetail
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload

def create(db: Session, request):
    new_item = model.Order(
        customer_id=request.customer_id,  # Using customer_id as per the diagram
        total_price=request.total_price,
        status=request.status,
        tracking_number=request.tracking_number
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(Order).options(
            joinedload(Order.order_details).joinedload(Order.order_details.property.mapper.class_.menu_item)
        ).all()
        return result
    except SQLAlchemyError as e:
        error_message = str(e)
        if hasattr(e, 'orig') and e.orig:
            error_message = str(e.orig)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Database error: {error_message}"
        )


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id: int):
    try:
        db.query(OrderDetail).filter(OrderDetail.order_id == item_id).delete(synchronize_session=False)
        order = db.query(model.Order).filter(model.Order.id == item_id).first()
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found!")
        db.delete(order)
        db.commit()
    except SQLAlchemyError as e:
        error_message = str(e)
        if hasattr(e, 'orig') and e.orig:
            error_message = str(e.orig)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Database error: {error_message}"
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)

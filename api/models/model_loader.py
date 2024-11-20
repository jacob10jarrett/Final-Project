from . import (
    orders,
    order_details,
    recipes,
    sandwiches,
    resources,
    ingredients,
    menu_items,
    promotion,
    payment,
    customers,
    reviews
)

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    ingredients.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    promotion.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)
    customers.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)

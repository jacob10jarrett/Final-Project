from . import orders, order_details, ingredients, menu_items, payment, promotion


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(ingredients.router)
    app.include_router(menu_items.router)
    app.include_router(payment.router)
    app.include_router(promotion.router)



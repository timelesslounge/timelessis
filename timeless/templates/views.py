def order_by(query, params):
    return query.order_by(*[param.replace(":", " ") for param in params])
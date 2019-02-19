
def order_by(query, params):
    return query.order_by(*[param.replace(":", " ") for param in params])


def filter_by(query, params):
    return query.filter_by(**(dict(param.split("=", maxsplit=1) for param in params)))


def order_by(query, params):
    return query.order_by(*[param.replace(":", " ") for param in params])

# @todo #260:30min Define GenericFilter and subclasses per entity.
#  Change client code to pass instances of a GenericFilter(or subclasses)
#  in order to build final filter depending on specific entity,
#  making it possible for example to filter by id using equality
#  and description using like operator. For more details see
#  https://github.com/timelesslounge/timelessis/pull/302#discussion_r258021696


def filter_by(query, params):
    return query.filter_by(**(dict(p.split("=", maxsplit=1) for p in params)))

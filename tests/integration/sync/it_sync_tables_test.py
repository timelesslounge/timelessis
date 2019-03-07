import pytest

from datetime import date

from tests.poster_mock import free_port, start_server
from timeless.restaurants.models import Table

from tests import factories

"""Integration tests for Table Sync with database"""

def test_sync_table(db_session):
    'Created info in tables for test'
    factories.FloorFactory.create_batch(size=10)
    factories.TableShapeFactory.create_batch(size=10)
    factories.SchemeTypeFactory.create_batch(size=10)

    port = free_port()
    poster_table_id=10
    poster_table_name="Table test"
    poster_table_floor_id=5
    poster_table_x=800
    poster_table_y=640
    poster_table_width=200
    poster_table_height=200
    poster_table_status="2"
    poster_table_max_capacity=5
    poster_table_min_capacity=5
    poster_table_multiple=False
    poster_table_playstation=True
    poster_table_shape_id=3
    poster_table_deposit_hour=5
    poster_table_created_on=date.today()
    poster_table_updated_on=date.today()
    start_server(port,
        tables= [
            {
                "id": poster_table_id,
                "name": poster_table_name,
                "floor_id": poster_table_floor_id,
                "x": poster_table_x,
                "y": poster_table_y,
                "width": poster_table_width,
                "height": poster_table_height,
                "status": poster_table_status,
                "max_capacity": poster_table_max_capacity,
                "min_capacity": poster_table_min_capacity,
                "multiple": poster_table_multiple,
                "playstation": poster_table_playstation,
                "shape_id": poster_table_shape_id,
                "deposit_hour": poster_table_deposit_hour,
                "created_on": poster_table_created_on,
                "updated_on": poster_table_updated_on
            }
        ]
    )
    table_in_database = Table(
        id=10,
        name="Table test",
        floor_id=5,
        x=800,
        y=640,
        width=200,
        height=200,
        status="2",
        max_capacity=5,
        min_capacity=5,
        multiple=False,
        playstation=True,
        shape_id=3,
        deposit_hour=5,
        created_on=date.today(),
        updated_on=date.today()
    )
    db_session.add(table_in_database)
    db_session.commit()

    row = Table.query.filter_by(id=10).one()
    assert row.id == poster_table_id
    assert row.name == poster_table_name
    assert row.floor_id == poster_table_floor_id
    assert row.x == poster_table_x
    assert row.y == poster_table_y
    assert row.width == poster_table_width
    assert row.height == poster_table_height
    assert row.status == poster_table_status
    assert row.max_capacity == poster_table_max_capacity
    assert row.min_capacity == poster_table_min_capacity
    assert row.multiple == poster_table_multiple
    assert row.playstation == poster_table_playstation
    assert row.shape_id == poster_table_shape_id
    assert row.created_on == poster_table_created_on
    assert row.updated_on == poster_table_updated_on
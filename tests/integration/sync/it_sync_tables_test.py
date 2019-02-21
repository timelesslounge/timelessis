import pytest

from datetime import date, timedelta, datetime

from tests.poster_mock import free_port, start_server
from timeless.restaurants.models import Table
from timeless.sync.synced_table import SyncedTable
from timeless.poster.api import Poster

"""Integration tests for Table Sync with database"""
"""
    @todo #187:30min Implement integration tests for this periodic task.
     Create fixture and mock response from poster, and check how it will be
     saved in DB. API docs - https://dev.joinposter.com/en/docs/api
"""


@pytest.mark.skip("sync for table not implemented yet")
def test_sync_table(db_session):
    port = free_port()
    poster_table_id=10
    poster_table_name="Round Table of The Knights"
    poster_table_floor_id=5
    poster_table_x=640
    poster_table_y=480
    poster_table_width=200
    poster_table_height=200
    poster_table_status="active"
    poster_table_max_capacity=5
    poster_table_multiple=False
    poster_table_playstation=True
    poster_table_shape_id=1
    poster_table_min_capacity=1
    poster_table_created=datetime.utcnow
    poster_table_updated=datetime.utcnow
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
                "multiple": poster_table_multiple,
                "playstation": poster_table_playstation,
                "shape_id": poster_table_shape_id,
                "min_capacity": poster_table_min_capacity,
                "created": poster_table_created,
                "updated": poster_table_updated
            }
        ]
    )
    table_in_database = Table(
        id=10,
        name="Table for Knights that Are Round",
        floor_id=6,
        x=800,
        y=600,
        width=400,
        height=400,
        status="inactive",
        max_capacity=4,
        multiple=True,
        playstation=False,
        shape_id=3,
        min_capacity=2,
        created=date.today() - timedelta(5),
        updated=date.today() - timedelta(5)
    )
    db_session.add(table_in_database)
    db_session.commit()
    synced_table = SyncedTable(table_in_database).sync(
        Poster(
            url=f"http://localhost:{port}"
        )
    )
    row = db_session.query(Table).get(synced_table.id)
    assert row.id == poster_table_id 
    assert row.name == poster_table_name 
    assert row.floor_id == poster_table_floor_id 
    assert row.x == poster_table_x 
    assert row.y == poster_table_y 
    assert row.width == poster_table_width 
    assert row.height == poster_table_height 
    assert row.status == poster_table_status 
    assert row.max_capacity == poster_table_max_capacity 
    assert row.multiple == poster_table_multiple 
    assert row.playstation == poster_table_playstation 
    assert row.shape_id == poster_table_shape_id 
    assert row.min_capacity == poster_table_min_capacity 
    assert row.created == poster_table_created 
    assert row.updated == poster_table_updated



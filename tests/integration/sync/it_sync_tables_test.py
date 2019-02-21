import pytest

from timeless.poster import tasks


@pytest.mark.skip
def test_sync_location():
    """
    @todo #187:30min Implement integration tests for this periodic task.
     Create fixture and mock response from poster, and check how it will be
     saved in DB. API docs - https://dev.joinposter.com/en/docs/api
    """
    tasks.sync_tables()

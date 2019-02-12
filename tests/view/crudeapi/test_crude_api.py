from timeless.views import CrudAPIView
"""
    Tests for CrudeAPIView.

"""

def test_get():
    apiview = CrudAPIView
    assert apiview.get(url_lookup="something")

def test_post():
    apiview = CrudAPIView

def test_delete():
    apiview = CrudAPIView

def test_put():
    apiview = CrudAPIView
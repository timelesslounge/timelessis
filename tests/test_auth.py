from datetime import datetime

from timeless import DB
from timeless.auth.auth import login
from timeless.employees.models import Employee


def test_incorrect_username(app):
    with app.app_context():
        assert (login("unknown", "unknown") == "Incorrect username.")


def test_incorrect_password(app):
    with app.test_request_context():
        employee = Employee(first_name="Alice", last_name="Cooper",
                            username="vgv", phone_number="1",
                            birth_date=datetime.utcnow(),
                            registration_date=datetime.utcnow(),
                            email="test@test.com", password="pass")
        DB.session.add(employee)
        DB.session.commit()
        error = login("vgv", "unknown")
        DB.session.delete(employee)
        DB.session.commit()
        DB.session.remove()
        assert ( error == "Incorrect password.")


def test_authenticated(app):
    with app.test_request_context():
        employee = Employee(first_name="Alice", last_name="Cooper",
                            username="vgv", phone_number="1",
                            birth_date=datetime.utcnow(),
                            registration_date=datetime.utcnow(),
                            email="test@test.com", password="pass")
        DB.session.add(employee)
        DB.session.commit()
        error = login("vgv", "pass")
        DB.session.delete(employee)
        DB.session.commit()
        DB.session.remove()
        assert ( error is None)
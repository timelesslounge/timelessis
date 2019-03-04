""" Authentication methods are implemented here. """
import random
import string


from flask import session
from passlib.handlers.bcrypt import bcrypt_sha256

from timeless.employees.models import Employee
from timeless.mail import MAIL
from flask_mail import Message


PASS_LENGTH = 8

def login(username="", password=""):
    """Login user

    """
    user = Employee.query.filter_by(username=username).first()
    error = None
    if user is None or not verify(password, user.password):
        error = "login.failed"
    if error is None:
        session.clear()
        session["user_id"] = user.id
    return error


def forgot_password(email=""):
    """ Handle the forgot password routine. """
    user = Employee.query.filter_by(email=email).first()    
    if not user:
        return "failed"

    password = "".join(random.choice(
            string.ascii_uppercase + string.digits
        ) for _ in range(PASS_LENGTH))
    user.password = bcrypt_sha256.hash(password)
    session.commit()
    MAIL.send(
        Message(
            f"Hello! your new password is {password}, please change it!",
            recipients=[email]
        )
    )
    session.clear()


def verify(password, hash):
    """
    Verifies password against hash
    :param password: Password to check
    :param hash: Hash to check password against
    :return: True in case of successful password verification
    """
    return bcrypt_sha256.verify(password, hash)


def hash(password):
    """
    Hash password
    :param password: Password to hash
    :return: Hashed password
    """
    return bcrypt_sha256.hash(password)

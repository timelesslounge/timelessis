""" MAIL module """
from flask_mail import Mail


"""
    @todo #388:30min mail sending should be disabled
     for development and testing as required by @vladarefiev.
     however should be enabled for staging and deployment.
     few extra words for PDD not to complain.
"""

MAIL = Mail()

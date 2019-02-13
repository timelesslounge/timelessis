""" Application Main module """
import os
from timeless import create_app


app = create_app(
    os.environ.get("TIMELESSIS_CONFIG", "config.DevelopmentConfig")
    )

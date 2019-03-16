""" Message resource for internationalization based on a property file """

from configparser import ConfigParser

from timeless.message.message_resource import MessageResource

import os

from main import app


class PropertyResource(MessageResource):
    """ Resources read from a property file. Reads the properties using config
        file formatting, so it reads keys and values from "[MESSAGES]" title.
    """

    directory = None
    locale = None

    def __init__(self, **kwargs):
        self.directory = kwargs.get("directory")
        self.locale = kwargs.get("locale")

    def get(self, key):
        path = os.path.join(app.root_path, self.directory)
        config = ConfigParser()
        config.read(f"{path}message_{self.locale}.properties")
        return config.get("MESSAGES", key)

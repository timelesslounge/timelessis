""" Message resource for internationalization based on a property file """


from timeless.message.message_resource import MessageResource

import re
import os

from main import app


class PropertyResource(MessageResource):
    """ Resources read from a property file.
        @todo #269:30min Implement FileResource. FileResource should read a
         property file and return the value according to the keys. Locale
         should be used to define from which locale the file belongs. The
         locale is defined in the fine name, for example,
         messages_en_US.properties. An exception must be raised if some
         resource is not found on property file. Then remove the skip
         annotations from it_test_property_resource.py

    """

    directory = None
    locale = None

    def __init__(self, **kwargs):
        self.directory = kwargs.get("directory")
        self.locale = kwargs.get("locale")

    def get(self, key):
        path = os.path.join(app.root_path, self.directory)
        file = open(f"{path}message_{self.locale}.properties")
        content = file.read()
        file.close()
        print(key)
        print(content)
        print(f"^{key}=*$")
        regex = r"^{key}=.*$"
        matches = re.findall(rf"^{key}=.*$", content)
        print("matches")
        print(matches)
        print(matches.split("="))
        return
        #raise Exception("PropertyResources not implement yet!")

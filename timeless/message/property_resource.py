""" Message resource for internationalization based on a property file """

from timeless.message.message_resource import MessageResource


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

    def get(self, key, locale):
        raise Exception("PropertyResources not implement yet!")

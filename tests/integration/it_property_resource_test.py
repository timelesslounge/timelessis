""" Tests for PropertyResource, resource for internationalization based on a
property file

"""
import pytest

from timeless.message.property_resource import PropertyResource


class TestPropertyResource():

    directory = "../tests/integration/resources/messages/"

    def test_property_found(self):
        """ Test if PropertyResource can return a value that exists"""
        assert PropertyResource(
            directory=self.directory, locale="en_US"
        ).get("foundkey") == "thevalue"

    def test_get_not_found(self):
        """ Test if PropertyResource returns exception when value does not
        exist
        """
        with pytest.raises(Exception) as ex:
            PropertyResource(
                directory=self.directory,
                locale="en_US"
            ).get("notfoundkey",)

    def test_get_found(self):
        """ Test if PropertyResource can return a value that exists from
        localised file
        """
        assert (
            PropertyResource(
                directory=self.directory,
                locale="pt_BR"
            ).get("foundkey") == "ovalor"
        )

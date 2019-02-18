""" Tests for PropertyResource, resource for internationalization based on a
property file

"""
import pytest

from timeless.message.property_resource import PropertyResource


class TestPropertyResource():

    directory = "resources/messages/"

    @pytest.mark.skip(reason="PropertyResource not implemented yet")
    def test_get_found(self):
        """ Test if PropertyResource can return a value that exists"""
        assert (
            PropertyResource(
                 directory=self.directory,
                 locale="en_US"
            ).get(self, "foundkey") == "thevalue"
        )

    @pytest.mark.skip(reason="PropertyResource not implemented yet")
    def test_get_not_found(self):
        """ Test if PropertyResource returns exception when value does not
        exist
        """
        with pytest.raises(Exception, "Value not found for key"):
            PropertyResource(
                directory=self.directory,
                locale="en_US"
            ).get(self, "notfoundkey",)

    @pytest.mark.skip(reason="PropertyResource not implemented yet")
    def test_get_found(self):
        """ Test if PropertyResource can return a value that exists from
        localised file
        """
        assert (
            PropertyResource(
                directory=self.directory,
                locale="pt_BR"
            ).get(self, "foundkey") == "ovalor"
        )

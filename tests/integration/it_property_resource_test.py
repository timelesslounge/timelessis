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
                 directory=self.directory
            ).get(self, "foundkey", "en_US") == "thevalue"
        )

    @pytest.mark.skip(reason="PropertyResource not implemented yet")
    def test_get_not_found(self):
        """ Test if PropertyResource returns exception when value does not
        exist
        """
        with pytest.raises(Exception, "Value not found for key"):
            PropertyResource(
                directory=self.directory
            ).get(self, "notfoundkey", "en_US")

    @pytest.mark.skip(reason="PropertyResource not implemented yet")
    def test_get_found(self):
        """ Test if PropertyResource can return a value that exists from
        localised file
        """
        assert (
            PropertyResource(
                directory=self.directory
            ).get(self, "foundkey", "pt_BR") == "ovalor"
        )

""" Message resource for internationalization """


class MessageResource:
    """ Interface that defines behavior """

    def get(self, key):
        raise Exception("Message Resource does not implement methods!")

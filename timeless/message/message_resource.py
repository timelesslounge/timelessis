""" Message resource for internationalization """


class MessageResource:
    """ Interface that defines behavior """

    def get(self, key, locale):
        raise Exception("Message Resource does not implement methods!")

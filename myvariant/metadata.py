""" Models the metadata results of the MyVariant API. """


import json
from requests import get


class MetaData(object):
    """ Models the MyVariant metadata API results,
    and associated methods.
    """

    def __init__(self, **entries):
        self.__dict__update(entries)

    @staticmethod
    def get_metadata():
        """ Retrieves the metadata from the MyVariant API.
        :returns metadata:
        """


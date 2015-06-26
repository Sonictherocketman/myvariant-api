""" Represents a variant and it's data.
For more information about fields and what they mean
see: http://myvariant.info/

author: Brian Schrader
since: 2015-06-26
"""


from api import endpoints, get, post


class Variant(object):
    """ A model of the variant object returned by MyVariant APIs. """

    def __init__(self, entries):
        self.__dict__.update(entries)

    @staticmethod
    def find_by(**kwargs):
        """ Given a set of key-value pairs, or kwargs, search for the
        desired variant(s).
        :returns variants: list of matches for the query provided.
        """
        results = get(endpoints['get-query'], params=kwargs)
        variants = []
        for r in results.get('hits'):
            variants.append(Variant(r))
        return variants

    @staticmethod
    def find_multiple_by(**kwargs):
        """ Given a list of queries and key-value params.
        Find all of the variants that match any of the given criteria.
        :returns variants: list of matches for hte queries provieded.
        """
        results = post(endpoints['post-query'], params=kwargs)
        variants = []
        for r in results:
            variants.append(Variant(r))
        return variants

    @staticmethod
    def get(variant_id, **kwargs):
        """ Given a variant ID (as per the MyVariant documentation)
        retrieve the given variant.
        :returns variant: a single variant object.
        """
        endpoint = endpoints['get-variant'].format(variant_id=variant_id)
        return Variant(get(endpoint, params=kwargs))

    @staticmethod
    def get_multiple(**kwargs):
        """ Given multiple variant IDs, retrieve all variants.
        :returns variants: list of variants with the IDs specified.
        """
        results = post(endpoints['post-variant'], params=kwargs)
        variants = []
        for r in results:
            variants.append(Variant(r))
        return variants

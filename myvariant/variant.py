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
    def find_by(query, **params):
        """ Given a set of key-value pairs, or kwargs, search for the
        desired variant(s).
        :returns variants: list of matches for the query provided.
        """
        params['q'] = query
        results = get(endpoints['get-query'], params=params)
        variants = []
        for r in results.get('hits'):
            variants.append(Variant(r))
        return variants

    @staticmethod
    def find_multiple_by(queries, *params_list):
        """ Given a list of queries and key-value params.
        Find all of the variants that match any of the given criteria.
        :returns variants: list of matches for hte queries provieded.
        """
        q = ','.join(queries)
        params = {}
        for p in params_list:
            for key in p.keys():
                if params.get(key) is not None:
                    params[key] += ',{}'.format(p[key])
                else:
                    params[key] = str(p[key])
        params['q'] = q
        results = post(endpoints['post-query'], params=params)
        variants = []
        for r in results:
            variants.append(Variant(r))
        return variants

    @staticmethod
    def get(variant_id):
        """ Given a variant ID (as per the MyVariant documentation)
        retrieve the given variant.
        :returns variant: a single variant object.
        """
        endpoint = endpoints['get-variant'].format(variant_id=variant_id)
        return Variant(get(endpoint))

    @staticmethod
    def get_multiple(variant_ids):
        """ Given multiple variant IDs, retrieve all variants.
        :returns variants: list of variants with the IDs specified.
        """
        pass





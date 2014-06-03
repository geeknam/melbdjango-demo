#
# MelbDjango - QuerySet Example
# Powerful syntax
#

import requests
from urllib import urlencode

class QuerySet(object):

    def __init__(self, limit=None):
        self.base_url = 'http://www.kogan.com/au/api/product/'
        self.limit = limit if limit else 24

        self._filters = {}
        self._cache = None

        self._index = -1

    ### Iterable ####
    def __iter__(self):
        return self

    def next(self):
        if self._index < len(self._objects) - 1:
            self._index += 1
            return self._objects[self._index]
        else:
            self._index = -1
            raise StopIteration

    ### Django ORM-like methods ###
    def filter(self, *args, **kwargs):
        self._filters.update(**kwargs)
        return self

    def order_by(self, field):
        self._filters.update({
            'order_by': field
        })
        return self

    def values_list(self, *args, **kwargs):
        flat = kwargs.get('flat', False)
        return [
            getattr(obj, args[0]) if flat else tuple([getattr(obj, attr) for attr in args])
            for obj in self._objects
        ]

    def _fetch(self):
        """
        Fetches data, makes network call, caches response
        """
        if self._cache:
            return self._cache

        query_string = urlencode(self._filters)
        url = '%s?%s' % (self.base_url, query_string)
        self._cache = requests.get(url).json()
        return self._cache

    @property
    def _objects(self):
        return [
            Product(**product_detail)
            for product_detail in self._fetch()['objects']
        ]

class Product(object):

    objects = QuerySet()

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return self.__dict__['title']



qset = Product.objects.filter(department='televisions', category='led-tv').order_by('-price').values_list('title', 'price')
print qset

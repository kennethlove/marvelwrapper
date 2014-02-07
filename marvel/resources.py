import requests

from . import models


class Resource(object):
    url_stub = None
    item = None
    item_end_points = []
    model = None
    queryset = []

    def __init__(self, cerebro, prefill=True):
        self.cerebro = cerebro
        if prefill:
            self.get()

    def __iter__(self):
        for item in self.queryset:
            yield resource

    def __len__(self):
        return len(self.queryset)

    def __getitem__(self, key):
        try:
            return self.queryset[key]
        except (KeyError, IndexError):
            raise IndexError

    def _get_url(self, item_endpoint=None, item=None):
        url = '{0.cerebro.BASE_URL}{0.url_stub}'.format(self)
        return url

    def get(self):
        req = requests.get(self._get_url(), params=self.cerebro.params)
        json = req.json()
        if 'data' in json and 'results' in json['data']:
            for result in json['data']['results']:
                id = result.pop('id')
                name = result.pop('name')
                self.add(id, name, **result)

    def add(self, id, name, **details):
        item = self.model(id, name, **details)
        self.queryset.append(item)


class CharacterResource(Resource):
    url_stub = 'characters'
    item_end_point = ['comics', 'events', 'series', 'stories']
    model = models.Character

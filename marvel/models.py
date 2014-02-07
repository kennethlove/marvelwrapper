class Character(object):
    def __init__(self, id, name, **details):
        self._id = id
        self._details = details
        self.name = name.strip()
        self.fill(**self._details)

    def fill(self, **details):
        self.url = details['resourceURI']
        self.description = details['description']
        self.detail_url = [url for url in details['urls'] if url['type'] == 'detail']
        self.comics = [Comic(comic['name']) for comic in details['comics']['items']]
        self.series = []
        self.stories = []
        self.events = []


class Comic(object):
    def __init__(self, title):
        self.title = title

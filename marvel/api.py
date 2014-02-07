import hashlib
import time


class Cerebro(object):
    BASE_URL = 'http://gateway.marvel.com/v1/public/'
    PUBLIC_KEY = None
    PRIVATE_KEY = None

    def __init__(self, public_key, private_key):
        self.PUBLIC_KEY = public_key
        self.PRIVATE_KEY = private_key

    @property
    def params(self):
        ts = str(time.time())
        hsh = hashlib.md5('{0}{1.PRIVATE_KEY}{1.PUBLIC_KEY}'.format(ts, self))
        return {
            'apikey': self.PUBLIC_KEY,
            'ts': ts,
            'hash': hsh.hexdigest()
        }

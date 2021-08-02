class DB(object):
    _instance = None
    _data = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._data = {}
        return cls._instance

    def get(self, key):
        return self._data.get(key, None)

    def set(self, key, value):
        self._data[key] = value

    def delete(self, key):
        try:
            del self._data[key]
        except KeyError:
            pass

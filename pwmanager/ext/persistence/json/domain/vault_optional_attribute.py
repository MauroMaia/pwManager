class OptionalAttribute(object):
    def __init__(self, key, value):
        assert key is not None, 'key should not be None'
        assert key != '', 'key should not be empty'
        assert type(key) == str, 'key type need to be string'

        assert value is not None, 'value should not be None'

        self.key = key
        self.value = value

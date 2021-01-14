from datetime import datetime


class OptionalAttribute(object):
    def __init__(
            self,
            key,
            value,
            last_update_at: datetime,
            created_at: datetime
    ):
        """ TODO """

        assert key is not None, 'key should not be None'
        assert key != '', 'key should not be empty'
        assert type(key) == str, 'key type need to be string'

        assert value is not None, 'value should not be None'

        self.key = key
        self.value = value
        self.last_update_at = last_update_at

        if created_at is not None:
            self.created_at = created_at

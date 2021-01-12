# Thirdparty
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Local
from .db_models import Base


class SQLiteConnection(object):
    # The connection object
    _conn = None

    def __init__(self, connstring):
        """
        Creates an instance of the SQLiteConnection class.

        Args:
            connstring (str): The connection string.
        """
        self._conn = create_engine(connstring)
        self._session = sessionmaker(bind=self._conn)

    def sync_schema(self):
        """
        Synchronizes the database schema.

        Raises:
            OperationalError: When the connection to the database fails.
        """
        Base.metadata.create_all(self._conn)

    def session(self):
        """
        Creates and returns a session to the database.

        Returns:
            object: Session from the sessionmaker method in sqlalchemy.
        """
        return self._session()

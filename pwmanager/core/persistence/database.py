from .db_models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError


class Database(object):

    @classmethod
    def connect_to_database(cls, app, path_to_database):
        engine = create_engine(
            'sqlite:///' + path_to_database,
            echo=False
        )

        app.log.debug('Connecting to database and creating schema')
        engine.connect()  # connect to the database

        try:
            Base.metadata.create_all(engine)
        except OperationalError as e:
            app.log.error('Operational Error - Code: {} - Message: {}'.format(e.orig.args[0], e.orig.args[1]))
            print('Operational Error\nCode: {}\nMessage: {}'.format(e.orig.args[0], e.orig.args[1]))
            exit(1)

        session = sessionmaker()
        session.configure(bind=engine)

        return Database(engine, session)

    def __init__(self, engine, session):
        self.engine = engine
        self.Session = session

    def new_session(self):
        return self.Session()

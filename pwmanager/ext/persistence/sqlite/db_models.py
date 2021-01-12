# Third party
import json

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, Boolean, func, ForeignKey

# Declare the Base class for the models
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class AppUsers(Base):
    __tablename__ = 'app_users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password_hash = Column(String(250), nullable=False)
    readonly = Column(Boolean, nullable=False, default=False)
    created_on = Column(DateTime, server_default=func.now())
    updated_on = Column(DateTime, server_default=func.now(), server_onupdate=func.now())

    def __str__(self):
        return json.dumps({c.name: getattr(self, c.name) for c in self.__table__.columns})


class VaultEntry(Base):
    __tablename__ = 'vault_entries'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    description = Column(String(250), nullable=True)
    username = Column(String(250), nullable=True)
    password = Column(String(250), nullable=False)
    created_on = Column(DateTime, server_default=func.now())
    updated_on = Column(DateTime, server_default=func.now(), server_onupdate=func.now())
    requester_id = Column(Integer, ForeignKey('app_users.id'))
    requester = relationship("AppUsers", backref=backref("app_users", uselist=False))

    # To store the password
    # import hashlib
    # dk = hashlib.pbkdf2_hmac('sha256', bytes(master_password), bytes(os.urandom(32)), 100000).hex()

    def __str__(self):
        return json.dumps({c.name: getattr(self, c.name) for c in self.__table__.columns})

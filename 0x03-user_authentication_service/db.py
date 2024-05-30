#!/usr/bin/env python3
"""DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from typing import Dict, Union
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Implements the add_user method
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, *args, **kwargs) -> Union[User, None]:
        """Searches for a user by the provided keyword arguments."""

        if not kwargs:
            raise NoResultFound("No search criteria provided.")

        valid_keys = {'email', 'id', 'hashed_password', 'session_id', 'reset_token'}
        invalid_keys = set(kwargs.keys()) - valid_keys
        if invalid_keys:
            raise InvalidRequestError(f"Invalid search keys provided: {', '.join(invalid_keys)}")

        query = self._session.query(User)
        for key in kwargs:
            if key == 'email':
                query = query.filter(User.email == kwargs[key])
            elif key == 'id':
                query = query.filter(User.id == kwargs[key])
            elif key == 'hashed_password':
                query = query.filter(User.hashed_password == kwargs[key])
            elif key == 'session_id':
                query = query.filter(User.session_id == kwargs[key])
            elif key == 'reset_token':
                query = query.filter(User.reset_token == kwargs[key])

        try:
            user = query.first()
            if user is None:
                raise NoResultFound("No user found matching the search criteria.")
            return user
        except NoResultFound:
            raise NoResultFound("No user found matching the search criteria.")

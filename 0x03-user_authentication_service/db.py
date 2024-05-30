#!/usr/bin/env python3
"""DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound, InvalidRequestError

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

        try:
            query = self._session.query(User).filter_by(**kwargs)
            user = query.first()
            if user is None:
                raise NoResultFound("No user found.")
            return user
        except NoResultFound:
            raise NoResultFound("No user found matching the search criteria.")
        except InvalidRequestError as e:
            raise InvalidRequestError(f"Invalid query arguments: {e}")

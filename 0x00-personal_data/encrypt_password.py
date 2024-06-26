#!/usr/bin/env python3
""" User passwords should NEVER be stored in plain text in a database
"""
import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password
    """
    b = password.encode()
    hashed = hashpw(b, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Check whether a password is valid
    """
    return bcrypt.checkpw(password.encode(), hashed_password)

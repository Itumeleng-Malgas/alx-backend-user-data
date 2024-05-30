#!/usr/bin/env python3
"""
Create a class BasicAuth that inherits from Auth
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extracts the Base64 part of a Basic Authorization header."""

        if isinstance(authorization_header,
                      str) and authorization_header.startswith('Basic '):
            return authorization_header.split(' ', 1)[1]
        return None

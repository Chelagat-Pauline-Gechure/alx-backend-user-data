#!/usr/bin/env python3
""" Modules required
"""
from flask import request

class Auth:
    def require_auth(self, path: str, exclude_paths: List[str]) -> bool:
        """ Check if authentication is required."""
        return False

    def authorization_header(self, request=None) -> str:
        """ Return authorization header."""

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrun the current user."""
        return None

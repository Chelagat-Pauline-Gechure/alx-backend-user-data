#!/usr/bin/env python3
""" Authentication Module
"""
from typing import List, TypeVar
from flask import request
import fnmatch


class Auth:
    """ Class to manage API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if authentication is required.
        Args:
            paths(str): Path being accessed.
            excluded_paths (List[str]): List of paths not to be autheniticated.
        Returns:
            bool: True if authentication is required, false otherwise.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Method to retrieve authorization header from Flask request object.
        Args:
            request(flask.request): Flask request object.
        Returns:
            str: Authorization header, or None if not found.
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method to retrieve current user based on Flask request object.
        Args:
            request(flask.request): Flask request object.
        Returns:
            TypeVar('User'): Current user or None if not found.
        """
        return None

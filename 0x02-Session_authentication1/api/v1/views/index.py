#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


# unauthorized access
@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """ GET /api/v1/unauthorized

    Returns:
        str: 401 error
    """
    abort(401, description='Unauthorized')


# forbidden access
@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """ GET /api/v1/forbidden

    Returns:
        str: 403 error
    """
    abort(403, description='Forbidden')


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)

#!/usr/bin/python3
"""index file
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', strict_slashes=False)
def service_status():
    """returns service status"""
    return jsonify({'status': 'OK'})

@app_views.route('/stats', strict_slashes=False)
def objects_stats():
   """returns the number of each object type"""
    classes = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    for k, v in classes.items():
        classes[k] = storage.count(v)
    return jsonify(classes)

#!/usr/bin/python3
"""index file
"""

from api.v1.views import app_views

@app_views.route('/status', strict_slashes=False)
def service_status():
    """returns service status"""
    return jsonify({'status': 'OK'})

@app_views.route('/api/v1/stats', strict_slashes=False)
def objects_stats():
   """returns the number of each object type"""
    classes = {
        "amenities": 47,
        "cities": 36,
        "places": 154,
        "reviews": 718,
        "states": 27,
        "users": 31
    }
    for k, v in classes.items():
        classes[k] = storage.count(v)
    return jsonify(classes)

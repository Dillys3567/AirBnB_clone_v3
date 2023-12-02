#!/usr/bin/python3
"""index file
"""

from api.v1.views import app_views

@app_views.route('/status', strict_slashes=False)
def service_status():
    """returns service status"""
    return jsonify({'status': 'OK'})

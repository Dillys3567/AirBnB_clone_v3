#!/usr/bin/python3
"""api with endpoints to return status of api
"""

from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)

def page_not_found():
    """return page not found error"""
    return jsonify({"error": "Not found"}), 404
@app.teardown_appcontext
def teardown_appcontext(exec=None):
    """calls a tear down"""
    storage.close()


if __name__ == "__main__":
    """run the app if script not imported
    """
    if my_host is None:
        my_host = '0.0.0.0'
    if my_port is None:
        my_port = 5000:
    app.run(host=my_host, port===my_port, threaded=True)

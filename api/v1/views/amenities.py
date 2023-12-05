#!/usr/bin/python3
"""view for Amenity objects that handles all API actions
"""

from flask import jsonify, Flask, abort, request
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views

@app_views.route('/amenities', methods=['GET', 'POST'],
        strict_slashes=False)
def amenity():
    """get amenities"""
    if request.method == 'GET':
        return jsonify([obj.to_dict() for obj in storage.all("Amenity").values()])
    if request.method == 'POST':
        post = request.get_json()
        if post is None or type(post) != dict:
            return ({'error': 'Not a JSON'}), 400
        name = post.get("name")
        if name is None:
            return ({'error': 'Missing name'}), 400
        amenity = Amenity(**post)
        amenity.save()
        return jsonify(amenity.to_dict()), 201


@app_views.routes('/amenities/<string:amenity_id>',
        methods=['GET', 'DELETE', 'PUT'], strict_slashes=False)
def amenity_with_id(amenity_id):
    """get amenity by id"""
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    if request.method == 'GET':
        return jsonify(amenity.to_dict())
    if request.method == 'DELETE':
        storage.delete(amenity)
        storage.save()
        return jsonify({}), 200
    if request.method == 'PUT':
        data = request.get_json()
        if data is None or type(data) != dict:
            return ({'error': 'Not a JSON'})
        ignore = ['id', 'created_at', 'updated_at']
        amenity.update(ignore, **data)
        return jsonify(amenity.to_dict()), 200




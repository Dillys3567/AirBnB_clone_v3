#!/usr/bin/python3
"""create a new view for City objects that handles all API actions
"""

from flask import jsonify, request, abort, Flask
from app.v1.views import app_views
from models import storage
from models.city import City

@app_views.route('/api/v1/states/<string:state_id>/cities',
        methods=['GET','POST'], strict_slashes=False)
def states_cities(state_id):
    """Retrieves the list of all City objects of a State"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    if request.method == 'GET':
        return jsonify([obj.to_dict() for obj in state.cities])
    if request.method == 'POST':
        post = request.get_json()
        if post is None or type(post) != dict:
            return ({'error': 'Not a JSON'}), 400
        name = post.get("name")
        if name is None:
            return ({'error': 'Missing name'}), 400
        city = City(state_id=state_id, **post)
        city.save()
        return jsonify(city.to_dict()), 201

@app_views.route('/api/v1/cities/<string:ity_id>',
        methods=['GET', 'DELETE', 'PUT'], strict_slashes=False)
def city_with_id(city_id):
    """Retrieves a city with id"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404):
    if request.method == 'GET':
        return jsonify(city.to_dict())
    if request.method == 'DELETE':
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    if request.method == 'PUT':
        put_data = request.get_json()
        if put_data is None or type(put_data) != dict:
            return ({'error': 'Not a JSON'}), 400
        ignore = ['id','state_id', 'created_at', 'updated_at']
        city.update(ignore, **put_data)
        return (city.to_dict()), 200

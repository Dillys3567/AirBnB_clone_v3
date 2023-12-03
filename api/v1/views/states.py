#!/usr/bin/python3
"""view for State objects that handles all default RESTFul API actions
"""

from flask import jsonify
from api.v1.views import app_views
from flask import Flask, request, abort
from models import storage
from models.state import State

@app.views('/states', methods=['GET', 'POST'], strict_slashes=False)
def state():
    """retrieve state"""
    if request.method == 'GET':
        return jsonify(obj.to_dict() for obj in storage.all("State").values())
    if request.method == 'POST':
        post = request.get_json()
        if post is None or type(post) != dict:
            return ({'error': 'Not a JSON' }), 400
        name = post.get('name')
        if name is None:
            return ({'error': 'Missing name'}), 400
        state = State(**post)
        state.save()
        return jsonify(state.to_dict()), 201

@app.views('/states/<string:state_id>', methods=['GET', 'DELETE', 'PUT'],
        strict_slashes=False)
def state_with_id(state_id):
    """retrieve states with id"""
    state = storage.get("State", state_id)
    if state_id is None:
        abort(404)
    if request.method == 'GET':
        return jsonify(state.to_dict())
    if request.method == 'DELETE':
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    if request.method == 'PUT':
        state_dict = request.get_json()
        if state_dict is None or type(state_dict) != dict:
            return ({'error': 'Not a JSON'}), 400
        ignore = ['id', 'created_at', 'updated_at')
        state.update(ignore, **state_dict)
        return jsonify(state.to_dict()), 200




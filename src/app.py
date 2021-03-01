"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person
#CORS me permite hacer un cruce de origen, sin importar donde este el fetch
app = Flask(__name__)
#Que no sea estricto con los slashes
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
#decoradores
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }
    return jsonify(response_body), 200


@app.route('/members', methods=['POST'])
def add_member():
    new_member = request.get_json()
    if isinstance(new_member, dict):
        members = jackson_family.add_member(new_member)
        response_body = {
            "family": members
        }
        return jsonify(response_body), 200
    else:
        return jsonify({"msg":"400 Bad Request"}), 400


@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id=None):
    eliminado = jackson_family.delete_member(id)
    if eliminado:
        return jsonify({"msg": "El miembro fue removido"}), 200
    else:
        return jsonify({"msg":"Id no se reconoce"}), 404


@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id=None):
    updatemem = request.get_json()
    modificado = jackson_family.update_member(id, updatemem)
    if modificado:
        return jsonify({"msg": "El miembro se ha actualizado"}), 200
    else:
        return jsonify({"msg":"400 Bad Request"}), 400


@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):

    member = jackson_family.get_member(id)
    if member != None:
        # response_body = {
        #     "family": member
        # }
        return jsonify(member), 200
    else: 
        
        return jsonify({"msg":"El id es inexistente"}), 404


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)

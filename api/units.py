from flask_restful import Resource
from flask_jwt import jwt_required
import json

with open('../feed_exports/index.json', 'r') as f:
    feh_units = json.load(f)

def search_for_attribute(self, attribute, name):
    total = []
    for feh_unit in feh_units:
        if feh_unit[attribute] == name:
            total.append(feh_unit)
    return total

class Unit(Resource):

    def get(self, name):
        return {'unit': next(filter(lambda x: x['Name'] == name, feh_units), None)}
    
    @jwt_required()
    def delete(self, name):
        global feh_units
        feh_units = list(filter(lambda x: x["Name"] != name, feh_units))
        return {'message': 'Unit deleted'}


class Tier(Resource):
    def get(self, name):
        return {'units': search_for_attribute(self, "Tier Rating", name)}

class Movement(Resource):
    def get(self, name):
        return {'units': search_for_attribute(self, "Movement Type", name)}

class Weapon(Resource):
    def get(self, name):
        return {'units': search_for_attribute(self, "Weapon", name)}

class BST(Resource):
    def get(self, name):
        return {'units': search_for_attribute(self, "Total Stats", name)}

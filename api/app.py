from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from user import Registration
from units import Unit, Tier, Movement, Weapon, BST

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jacob'
api = Api(app)  

jwt = JWT(app, authenticate, identity)

api.add_resource(Unit, '/unit/<string:name>')
api.add_resource(Tier, '/tier/<string:name>')
api.add_resource(Movement, '/movement/<string:name>')
api.add_resource(Weapon, '/weapon/<string:name>')
api.add_resource(BST, '/bst/<string:name>')

#api.add_resource(ItemList, '/items')
api.add_resource(Registration, '/register')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask_restful import Api, Resource, abort, reqparse

from controller.building import Building
from controller.area_code import AreaCode

app = Flask(__name__)
api = Api(app)

api.add_resource(Building, '/api/buildings')
api.add_resource(AreaCode, '/api/codes')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
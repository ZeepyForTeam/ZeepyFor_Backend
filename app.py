from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource
from building.controller.building import Building
from areacode.controller.area_code import AreaCode

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api.add_resource(Building, '/api/buildings')
api.add_resource(AreaCode, '/api/codes')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
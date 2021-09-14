 #-*- coding: utf-8 -*- 
from flask import jsonify
from repository.buidling_db_handler import BuildingDBHandler
from helper.mongo_data_parser import MongoDataParser
from bson.objectid import ObjectId

class BuildingService:
    def __init__(self):
        self.building_repository = BuildingDBHandler()
        self.parse = MongoDataParser()

    def get_all(self):
        data = self.building_repository.find_item()
        response = jsonify(self.parse.parse_many(data))
        response.status_code = 200
        return response

    def create(self, args):
        _id = self.building_repository.insert_item_one(args)
        response = jsonify()
        response.status_code = 201
        response.headers['location'] = f"/api/building/{str(_id)}"
        response.autocorrect_location_header = False
        return response
    
    def delete_by_id(self, args):
        self.building_repository.delete_item_one({"_id" : ObjectId(args._id)})
        response = jsonify()
        response.status_code = 204
        return response
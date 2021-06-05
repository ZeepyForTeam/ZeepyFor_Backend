 #-*- coding: utf-8 -*- 
from flask_restful import Resource, reqparse
from service.building_service import BuildingService

class Building(Resource):
    def __init__(self):
        self.building_service = BuildingService()

    def get(self):
        return self.building_service.get_all()

    def post(self):
        args = self.make_post_arg()
        return self.building_service.create(args)
    
    def delete(self):
        args = self.make_delete_arg()
        return self.building_service.delete_by_id(args)

    def make_post_arg(self):
        parser = reqparse.RequestParser()
        parser.add_argument('build_year', type=int, required=False)
        parser.add_argument('deal_year', type=int, required=True)
        parser.add_argument('dong', type=str, required=True)
        parser.add_argument('deposit', type=float, required=True)
        parser.add_argument('apartment', type=str, required=True)
        parser.add_argument('sigungu', type=str, required=False)
        parser.add_argument('deal_month', type=int, required=True)
        parser.add_argument('monthly_rent', type=int, required=True)
        parser.add_argument('deal_day', type=int, required=True)
        parser.add_argument('using_area', type=float, required=True)
        parser.add_argument('jibun', type=str, required=True)
        parser.add_argument('area_code', type=int, required=True)
        parser.add_argument('floor', type=int, required=True)
        parser.add_argument('latitude', type=float, required=False)
        parser.add_argument('longitude', type=float, required=False)
        parser.add_argument('full_address', type=str, required=False)
        parser.add_argument('type', type=str, required=True)
        return parser.parse_args()

    def make_get_arg(self):
        parser = reqparse.RequestParser()
        return parser.parse_args()

    def make_delete_arg(self):
        parser = reqparse.RequestParser()
        parser.add_argument('_id', type=str, required=True)
        return parser.parse_args()
 #-*- coding: utf-8 -*- 

import requests
import json

class zeepy_for_server_helper:
    def __init__(self):
        self.zeepy_for_server_url = "http://localhost:8080"

    def upload_building(self, data):
        url = self.zeepy_for_server_url + "/api/building"
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response

    def upload_building_deal(self, data):
        url = self.zeepy_for_server_url + "/api/deal"
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response
    
    def update_building_deal(self, data, _id):
        url = self.zeepy_for_server_url + "/api/deal/" + str(_id)
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.put(url, data=json.dumps(data), headers=headers)
        return response

    def get_building_deal(self, _id, floor):
        url = self.zeepy_for_server_url + "/api/deal/floor/" + str(floor) + "/building/" + str(_id) 
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.get(url, headers=headers)
        return response

 #-*- coding: utf-8 -*- 

import requests
import json

class ZeepyForServerHelper:
    def __init__(self):
        # self.zeepy_for_server_url = "http://13.125.168.182:8080"
        self.token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ6eDY0ODZAZ21haWwuY29tIiwiaWF0IjoxNjMyNDYxNDIyLCJleHAiOjE2MzI1NDc4MjJ9.j8sW5oX1pUUJXPxQNJo0FUiAOLVl9iYz6CdN8sSpJIY"
        self.zeepy_for_server_url = "http://localhost:8080"

    def upload_building(self, data):
        url = self.zeepy_for_server_url + "/api/buildings"
        headers = {'Content-Type': 'application/json; charset=utf-8', "X-AUTH-TOKEN": self.token}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response

    def batch_insert_building(self, data):
        url = self.zeepy_for_server_url + "/api/buildings/batch"
        headers = {'Content-Type': 'application/json; charset=utf-8', "X-AUTH-TOKEN": self.token}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response

    def batch_insert_building_deal(self, data):
        url = self.zeepy_for_server_url + "/api/deals/batch"
        headers = {'Content-Type': 'application/json; charset=utf-8', "X-AUTH-TOKEN": self.token}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response

    def upload_building_deal(self, data):
        url = self.zeepy_for_server_url + "/api/deals"
        headers = {'Content-Type': 'application/json; charset=utf-8', "X-AUTH-TOKEN": self.token}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response
    
    def update_building_deal(self, data, _id):
        url = self.zeepy_for_server_url + "/api/deals/" + str(_id)
        headers = {'Content-Type': 'application/json; charset=utf-8', "X-AUTH-TOKEN": self.token}
        response = requests.put(url, data=json.dumps(data), headers=headers)
        return response

    def get_building(self, address):
        url = self.zeepy_for_server_url + "/api/buildings/address" + "?address=" + address 
        headers = {'Content-Type': 'application/json; charset=utf-8', "X-AUTH-TOKEN": self.token}
        response = requests.get(url, headers=headers)
        return response

    def get_buildings(self):
        url = self.zeepy_for_server_url + "/api/buildings/all" 
        headers = {'Content-Type': 'application/json; charset=utf-8', "X-AUTH-TOKEN": self.token}
        response = requests.get(url, headers=headers)
        return response

    def get_building_deal(self, _id, floor):
        url = self.zeepy_for_server_url + "/api/deals/floors" + "?floor=" + str(floor) + "&id=" + str(_id) 
        headers = {'Content-Type': 'application/json; charset=utf-8', "X-AUTH-TOKEN": self.token}
        response = requests.get(url, headers=headers)
        return response

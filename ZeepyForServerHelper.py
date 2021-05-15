 #-*- coding: utf-8 -*- 

import requests
import json

class zeepy_for_server_helper:
    def __init__(self):
        self.zeepy_for_server_url = "http://localhost:8080"

    def update_building(self, data):
        url = self.zeepy_for_server_url + "/api/building"
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        requests.post(url, data=json.dumps(data), headers=headers)

    def update_building_deal(self, data):
        url = self.zeepy_for_server_url + "/api/deal"
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        requests.post(url, data=json.dumps(data), headers=headers)

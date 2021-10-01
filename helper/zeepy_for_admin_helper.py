 #-*- coding: utf-8 -*- 

import requests
import json

class ZeepyForAdminHelper:
    def __init__(self):
        # self.zeepy_for_admin_url = "http://localhost:5002"
        self.zeepy_for_admin_url = "http://13.125.214.60:5000"
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzMjk5NTYwOCwianRpIjoiOWE5NjhlZmQtZmZiZi00NjY2LWIyNjYtYzVlNTk0NWU5MGM3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3RAdGVzdC5jb20iLCJuYmYiOjE2MzI5OTU2MDgsImV4cCI6MTYzMzAwNjQwOH0.kr3qvEc0X3wgleuF5Mqlk93Z0l8WAWHpRFbw2fQmJcc"

    def upload_building(self, data):
        url = self.zeepy_for_admin_url + "/api/buildings"
        headers = {'Content-Type': 'application/json; charset=utf-8', "Authorization": "Bearer " + self.token}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response

    def batch_insert_building(self, data):
        url = self.zeepy_for_admin_url + "/api/buildings/batch"
        headers = {'Content-Type': 'application/json; charset=utf-8', "Authorization": "Bearer " + self.token}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response

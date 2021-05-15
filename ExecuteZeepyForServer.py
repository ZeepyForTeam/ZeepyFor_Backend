 #-*- coding: utf-8 -*- 

from MolitApi import molit_api # MOLIT API 클래스
from Scheduler import scheduler # 스케줄러 클래스
from XmlParserHelper import xml_parse_helper # XML 파싱 클래스
from AreaCodeHelper import area_code_helper # 지역코드 제작 클래스
from GeocoderApi import geocoder_api # GEOCODER API 클래스
from ZeepyForServerHelper import zeepy_for_server_helper

from datetime import datetime
import os
import json
import datetime

def upload_json_data_in_one_directory(directory, filename):
    zeepy = zeepy_for_server_helper()
    print(f"json_data_add_location/{directory}/{filename}")
    f = open(f"json_data_add_location/{directory}/{filename}", "r", encoding="UTF8")
    json_data_list = json.load(f)

    if "다가구" in filename:
        return
    
    sie = "서울특별시"

    if "세종특별자치시" in filename: 
        sie = "세종특별자치시"

    split_filename = filename[:-5].split("_")

    for json_data in json_data_list:
        location_string = ""

        gue = split_filename[-1].replace(" ", "")
        dong = json_data['dong'].replace(" ", "") 
        bunji = json_data['jibun'].replace(" ", "")
        apart = json_data['apartment'].replace(" ", "")

        area_code = int(json_data['area_code'])

        build_year = 0

        if json_data['build_year'] != '':
            build_year = int(json_data['build_year'])

        using_area = float(json_data['using_area'])

        if 'latitude' not in json_data or 'longitude' not in json_data:
            continue
        
        latitude = float(json_data['latitude'])
        longitude = float(json_data['longitude'])

        deal_year = int(json_data['deal_year'])
        deal_month = int(json_data['deal_month'])
        deal_day = int(json_data['deal_day'])

        deal_date = f"{deal_year}-{deal_month}-{deal_day}"
        floor = int(json_data['floor'])
        monthly_rent = int(json_data['monthly_rent'])
        deposit = int(json_data['deposit'].replace(",", ""))

        if sie != "세종특별자치시":
            location_string = f"{sie} {gue} {dong} {bunji} {apart}"
        else:
            location_string = f"{sie} {dong} {bunji} {apart}"

        building_data = {
            'buildYear' : build_year,
            'address' : location_string,
            'exclusivePrivateArea' : using_area,
            'areaCode' : area_code,
            'latitude' : latitude,
            'longitude' : longitude,
        }

        building_deal_data = {
            'dealDate' : deal_date,
            'deposit' : deposit,
            'monthlyRent' : monthly_rent,
            'floor' : floor
        }

        zeepy.update_building(building_data)
        zeepy.update_building_deal(building_deal_data)
        

def upload_all_in_directory_json_data():
    directoies_about_molit_json = os.listdir("json_data_add_location")
    for directory in directoies_about_molit_json:
        print(directory)
        molit_jsons_name = os.listdir(f"json_data_add_location/{directory}")

        for molit_json_name in molit_jsons_name:
            upload_json_data_in_one_directory(directory, molit_json_name)

def main(): # 매인 함수
    upload_all_in_directory_json_data()
    
if __name__ == "__main__":
	main()
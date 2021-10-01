 #-*- coding: utf-8 -*- 

from helper.zeepy_for_admin_helper import ZeepyForAdminHelper
from datetime import datetime
import os
import json
import time
import re
from datetime import datetime

'''
관리자 페이지 배치용
배치 인서트 방식
- 빌딩 인서트
- API 호출 한번
- 배포용 용 익스큐터
'''

def upload_json_data_in_one_directory(directory, filename):
    building_list = []

    print(f"json_data_add_location3/{directory}/{filename}")

    f = open(f"json_data_add_location3/{directory}/{filename}", "r", encoding="UTF8")
    json_data_list = json.load(f)
    building_type = ""

    if "다가구" in filename:
        return

    if "오피스텔" in filename:
        building_type = "OFFICETEL"
    elif "연립다세대" in filename:
        building_type = "ROWHOUSE"
    else:
        building_type = "UNKNOWN"

    sie = "서울특별시"

    if "세종특별자치시" in filename: 
        sie = "세종특별자치시"

    split_filename = filename[:-5].split("_")
    regex = "\(.*\)|\s-\s.*"

    for json_data in json_data_list:
        full_number_address = ""
        short_number_address = ""

        gue = split_filename[-1].replace(" ", "")
        dong = json_data['dong'].replace(" ", "") 
        bunji = json_data['jibun'].replace(" ", "")
        apart = json_data['apartment'].replace(" ", "")

        shortAddress = f"{sie} {gue}"

        if sie == "세종특별자치시":
            shortAddress = f"{sie}"

        if sie != "세종특별자치시":
            full_number_address = f"{sie} {gue} {dong} {bunji} {apart}"
            short_number_address = f"{dong} {bunji} {apart}"
        else:
            full_number_address = f"{sie} {dong} {bunji} {apart}"
            short_number_address = f"{dong} {bunji} {apart}"
        
        full_number_address = full_number_address.replace("  ", " ")
        short_number_address = short_number_address.replace("  ", " ")

        full_number_address = full_number_address.replace("  ", " ")
        short_number_address = short_number_address.replace("  ", " ")

        full_number_address = full_number_address.replace("  ", " ")
        short_number_address = short_number_address.replace("  ", " ")

        json_data["type"] = building_type
        if "build_year" in json_data and json_data["build_year"] != "":
            json_data["build_year"] = int(json_data["build_year"].replace(",",""))
        json_data["deal_year"] = int(json_data["deal_year"].replace(",",""))
        json_data["deposit"] = float(json_data["deposit"].replace(",",""))
        json_data["deal_month"] = int(json_data["deal_month"].replace(",",""))
        json_data["monthly_rent"] = int(json_data["monthly_rent"].replace(",",""))
        json_data["deal_day"] = int(json_data["deal_day"].replace(",",""))
        json_data["using_area"] = float(json_data["using_area"].replace(",",""))
        json_data["area_code"] = int(json_data["area_code"].replace(",",""))
        json_data["full_number_address"] = full_number_address
        json_data["short_number_address"] = short_number_address
        json_data["short_address"] = shortAddress
        json_data["floor"] = int(json_data["floor"].replace(",",""))
        if "latitude" in json_data:
            json_data["latitude"] = float(json_data["latitude"].replace(",",""))
        if "longitude" in json_data:
            json_data["longitude"] = float(json_data["longitude"].replace(",",""))
        building_list.append(json_data)

    return building_list
        

def bulk_building_in_directory_json_data():
    zeepy = ZeepyForAdminHelper()
    directoies_about_molit_json = os.listdir("json_data_add_location3")
    building_list = []
    for directory in directoies_about_molit_json:
        print(directory)

        if directory == "error":
            break

        molit_jsons_name = os.listdir(f"json_data_add_location3/{directory}")

        for molit_json_name in molit_jsons_name:
            building_list += upload_json_data_in_one_directory(directory, molit_json_name)
    
    cache_list = []

    for building in building_list:
        cache_list.append(building)
        if len(cache_list) == 100:
            response_batch_insert_building = zeepy.batch_insert_building(cache_list)
            response_batch_insert_building.close()
            cache_list = []
            time.sleep(1)

def main(): # 매인 함수
    bulk_building_in_directory_json_data()
    
if __name__ == "__main__":
	main()
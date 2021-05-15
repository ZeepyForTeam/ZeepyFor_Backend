 #-*- coding: utf-8 -*- 

from MolitApi import molit_api # MOLIT API 클래스
from Scheduler import scheduler # 스케줄러 클래스
from XmlParserHelper import xml_parse_helper # XML 파싱 클래스
from AreaCodeHelper import area_code_helper # 지역코드 제작 클래스
from GeocoderApi import geocoder_api # GEOCODER API 클래스

from datetime import datetime
import os
import json

def edit_molit_json_use_geocoder_api(directory, filename):
    geocoder = geocoder_api()
    print(f"json_data/{directory}/{filename}")
    f = open(f"json_data/{directory}/{filename}", "r", encoding="UTF8")
    json_data_list = json.load(f)
    
    sie = "서울특별시"

    if "세종특별자치시" in filename: 
        sie = "세종특별자치시"

    split_filename = filename[:-5].split("_")
    before_location_string = ""
    location = {}
    for json_data in json_data_list:
        location_string = ""
        if sie != "세종특별자치시":
            if "다가구" in filename:
                location_string = f"{sie} {split_filename[-1]} {json_data['dong']}"
            elif "오피스텔" in filename:
                location_string = f"{sie} {split_filename[-1]} {json_data['dong']} {json_data['apartment']}"
        else:
            if "다가구" in filename:
                location_string = f"{sie} {json_data['dong']}"
            elif "오피스텔" in filename:
                location_string = f"{sie} {json_data['dong']} {json_data['apartment']}"

        if location_string != before_location_string:
            location = geocoder.get_geocoder_api_address_to_location(location_string)
            before_location_string = location_string
        
        if location == False:
            continue

        json_data["latitude"] = location["y"]
        json_data["longitude"] = location["x"]

    f = open(f"json_data_add_location/{directory}/{filename}", "w", encoding="UTF8")
    f.write(json.dumps(json_data_list, indent=2, ensure_ascii=False))
    f.close()

def edit_molit_json_add_location_data_used_geocoder_api_and_save_files(): # GEOCODER API 사용 함수
    directoies_about_molit_json = os.listdir("json_data")
    for directory in directoies_about_molit_json:
        print(directory)

        if os.path.isdir(f"json_data_add_location/{directory}") == False: # 디렉토리 체크
            os.mkdir(f"json_data_add_location/{directory}")

        molit_jsons_name = os.listdir(f"json_data/{directory}")

        for molit_json_name in molit_jsons_name:
            edit_molit_json_use_geocoder_api(directory, molit_json_name)

def main(): # 매인 함수
    edit_molit_json_add_location_data_used_geocoder_api_and_save_files()
    
if __name__ == "__main__":
	main()
 #-*- coding: utf-8 -*- 

from helper.molit_api import MolitApi # MOLIT API 클래스
from helper.xml_parse_helper import XmlParseHelper # XML 파싱 클래스
from helper.area_code_helper import AreaCodeHelper # 지역코드 제작 클래스
from datetime import datetime
import os
import json

def is_pass_my_date_to_current_date(my_date_year, my_date_month): # 현재 날짜 비교 함수
    current_date_year = datetime.today().year
    current_date_month = datetime.today().month
    if current_date_year > my_date_year:
        return True
    elif current_date_month > my_date_month:
        return True
    else:
        return False

def make_my_date_string(my_date_year, my_date_month): # 날짜 스트링 변환 함수
    my_date_string = str(my_date_year)
    if my_date_month < 10:
        my_date_string += "0" + str(my_date_month)
    else:
        my_date_string += str(my_date_month)
    return my_date_string

def make_file(json_data, area_code_json, my_date_string, tag): # 파일 작성 함수
    # 파일 작성
    f = open(f"json_data2/{my_date_string}/{tag}_{area_code_json['SIDO_CODE']}_{area_code_json['SIGUNGU_CODE']}_{area_code_json['ADDRESS_NAME']}.json", "w", encoding="UTF8")
    f.write(json.dumps(json_data, indent=2, ensure_ascii=False))
    f.close()

def make_area_code_json_to_file(): # 지역코드 json 파일 제작 함수
    molit = MolitApi() # API HELPER
    area_code_json = molit.get_area_code_to_json()

    f = open(f"area_code.json", "w", encoding="UTF8")
    f.write(json.dumps(area_code_json, indent=2, ensure_ascii=False))
    f.close()

def save_to_file_setting_date_to_current_date_of_molit_data(): # 부동산 API 사용 함수
    molit = MolitApi() # API HELPER
    xml_parser = XmlParseHelper() # XML PARSER HELPER
    area_code = AreaCodeHelper() # AREA CODE HELPER

    area_code_json = area_code.get_setting_area_code_from_json()
    my_date_year = 2018
    my_date_month = 1

    while is_pass_my_date_to_current_date(my_date_year, my_date_month):
        my_date_string= make_my_date_string(my_date_year, my_date_month)
        print(my_date_string)

        if os.path.isdir(f"json_data2/{my_date_string}") == False: # 디렉토리 체크
            os.mkdir(f"json_data2/{my_date_string}")
        
        for area_code in area_code_json:
            # # 오피스텔 API CALL
            # officetels_data = molit.get_molit_api_officetels_data(area_code, my_date_string)
            # officetels_json = xml_parser.parse_molit_api_officetels_xml(officetels_data)
            # make_file(officetels_json, area_code, my_date_string, xml_parser.type[1])

            # # 단독/다가구 API CALL
            # family_data = molit.get_molit_api_family_data(area_code, my_date_string)
            # family_json = xml_parser.parse_molit_api_family_xml(family_data)
            # make_file(family_json, area_code, my_date_string, xml_parser.type[2])

            # 연립다세대 전월세 API CALL
            alliance_data = molit.get_molit_api_alliance_data(area_code, my_date_string)
            alliance_json = xml_parser.parse_molit_api_alliance_xml(alliance_data)
            make_file(alliance_json, area_code, my_date_string, xml_parser.type[3])
        
        if my_date_month >= 12:
            my_date_year += 1
            my_date_month = 1
        else:
            my_date_month += 1

def main(): # 매인 함수
    save_to_file_setting_date_to_current_date_of_molit_data()
    
if __name__ == "__main__":
	main()
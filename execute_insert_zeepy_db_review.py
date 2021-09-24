 #-*- coding: utf-8 -*- 

from helper.zeepy_for_server_helper import ZeepyForServerHelper
from helper.excel_parser_helper import ExcelParseHelper
from datetime import datetime
import os
import json
import time
import re
from datetime import datetime

'''
배치 인서트 방식
- 빌딩 거래 내역 인서트
- API 호출 한번
- 배포용 용 익스큐터
- 주의 무조건 빌딩 배치 익스큐터 사전에 실행 후 사용할 것
'''

def make_buidings_dict():
    result = {}
    zeepy = ZeepyForServerHelper()
    response_get_building = zeepy.get_buildings()
    building_list = json.loads(response_get_building.content)
    for building in building_list:
        result[building["fullNumberAddress"]] = building["id"]
    return result

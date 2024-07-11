import requests
import json
from statistics import stdev
import pandas as pd
from air_korea_api import air_condition_period_only_seoul

def calculate_item_variation(locations, req_item, init, end):
    variations = {}
    for loc in locations:
        data = air_condition_period_only_seoul(loc, init, end)
        pm10_values = [int(item[req_item]) for item in data if item[req_item] != '-']
        if pm10_values:
            variation = stdev(pm10_values)
            variations[loc] = variation
    return variations

def main():
    # 사용자로부터 시작일과 종료일 입력받기
    req_item = input("원하는 항목을 입력하세요 (so2, co, o3, no2, pm10, pm2.5): ")
    if req_item == "pm2.5" :
        req_item = "pm25Value"
    else :
        req_item = req_item + "value"
    init_date = input("시작일을 입력하세요 (예: 20240701): ")
    end_date = input("종료일을 입력하세요 (예: 20240709): ")

    # 서울시 구 리스트
    seoul_districts = ["강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중구", "중랑구"]

    # 각 구의 PM10 변동성 계산
    item_variations = calculate_item_variation(seoul_districts, req_item, init_date, end_date)

    # PM10 변동성에 따라 구를 내림차순으로 정렬하고 상위 5개 구 출력
    sorted_variations = sorted(item_variations.items(), key=lambda item: item[1], reverse=True)
    top_5_districts = sorted_variations[:5]

    # pandas DataFrame으로 변환
    df = pd.DataFrame(top_5_districts, columns=['구', 'item 변동성'])
    
    print("미세먼지(PM10) 변동성이 가장 큰 상위 5개 구:")
    print(df)

if __name__ == "__main__":
    main()

import requests
import json
from statistics import stdev
import pandas as pd

def air_condition_period_only_seoul(loc, init, end):
    url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getMsrstnAcctoRDyrg'
    params = {
        'serviceKey': 'R+8s9BHhcob1+/0e3PKTTRN7mTgLkVRHoS/rKZ2fRHhgQcvrffI0TvaHzh/406d2oF1iEU16aGKK5MJmimE9PA==',
        'returnType': 'json',
        'numOfRows': '100',
        'pageNo': '1',
        'inqBginDt': init,
        'inqEndDt': end,
        'msrstnName': loc
    }
    response = requests.get(url, params=params)
    result = json.loads(response.content)["response"]["body"]['items']
    return result

def calculate_pm10_variation(locations, init, end):
    variations = {}
    for loc in locations:
        data = air_condition_period_only_seoul(loc, init, end)
        pm10_values = [int(item['pm10Value']) for item in data if item['pm10Value'] != '-']
        if pm10_values:
            variation = stdev(pm10_values)
            variations[loc] = variation
    return variations

def main():
    # 사용자로부터 시작일과 종료일 입력받기
    init_date = input("시작일을 입력하세요 (예: 20240701): ")
    end_date = input("종료일을 입력하세요 (예: 20240709): ")

    # 서울시 구 리스트
    seoul_districts = ["강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중구", "중랑구"]

    # 각 구의 PM10 변동성 계산
    pm10_variations = calculate_pm10_variation(seoul_districts, init_date, end_date)

    # PM10 변동성에 따라 구를 내림차순으로 정렬하고 상위 5개 구 출력
    sorted_variations = sorted(pm10_variations.items(), key=lambda item: item[1], reverse=True)
    top_5_districts = sorted_variations[:5]

    # pandas DataFrame으로 변환
    df = pd.DataFrame(top_5_districts, columns=['구', 'PM10 변동성'])
    
    print("미세먼지(PM10) 변동성이 가장 큰 상위 5개 구:")
    print(df)

if __name__ == "__main__":
    main()

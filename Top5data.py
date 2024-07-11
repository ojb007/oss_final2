import requests
import json

class Get_data:
    def air_condition_period_only_seoul(self, loc, init, end):
        url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getMsrstnAcctoRDyrg'
        params = {
            'serviceKey': "key",
            'returnType': 'json',
            'numOfRows': '100',
            'pageNo': '1',
            'inqBginDt': init,
            'inqEndDt': end,
            'msrstnName': loc
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # HTTP 에러 발생 시 예외를 발생시킵니다.
            return response.json()       # JSON 형태로 데이터를 파싱하여 반환합니다.
        except requests.exceptions.HTTPError as err:
            print(f"HTTP 에러 발생: {err}")
        except requests.exceptions.RequestException as err:
            print(f"요청 에러 발생: {err}")

    def air_condition_city_realtime(self, loc):
        url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureSidoLIst'
        params = {
            'serviceKey': 'key',
            'returnType': 'json',
            'numOfRows': '100',
            'pageNo': '1',
            'sidoName': loc,
            'searchCondition': 'DAILY'
        }
        response = requests.get(url, params=params)
        result = json.loads(response.content)["response"]["body"]['items']
        return result

    def air_condition_except_seoul_realtime(self, item):
        url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureLIst'
        params = {
            'serviceKey': 'key',
            'returnType': 'json',
            'numOfRows': '100',
            'pageNo': '1',
            'itemCode': item,
            'dataGubun': 'HOUR',
            'searchCondition': 'WEEK'
        }
        response = requests.get(url, params=params)
        result = json.loads(response.content)["response"]["body"]['items']
        return result

def find_worst_air_quality_regions(init, end):
    seoul_districts = [
        '강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', 
        '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', 
        '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', 
        '은평구', '종로구', '중구', '중랑구'
    ]
    
    get = Get_data()
    district_averages = []
    
    for district in seoul_districts:
        district_data = get.air_condition_period_only_seoul(district, init, end)
        if district_data and 'response' in district_data and 'body' in district_data['response'] and 'items' in district_data['response']['body']:
            pm10_values = [int(item['pm10Value']) for item in district_data['response']['body']['items'] if item['pm10Value'] != '-']
            if pm10_values:
                average_pm10 = sum(pm10_values) / len(pm10_values)
                district_averages.append({'district': district, 'average_pm10': average_pm10})
    
    # Sort districts by average PM10 values and get the top 5 worst
    district_averages_sorted = sorted(district_averages, key=lambda x: x['average_pm10'], reverse=True)
    top_5_worst = district_averages_sorted[:5]
    
    return top_5_worst

# 사용 예
init_date = '20240701'
end_date = '20240709'
worst_regions = find_worst_air_quality_regions(init_date, end_date)

for region in worst_regions:
    print(f"지역: {region['district']}, 평균 PM10 농도: {region['average_pm10']:.2f}")


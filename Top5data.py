import requests
import json
#from air_korea_api import air_condition_realtime, air_condition_city_realtime, air_condition_period_only_seoul


def air_condition_period_only_seoul(loc, init, end) :
    #params : 구(서울에 속한 구만 가능), 시작일, 종료일 (ex: '강남구', '20240701', '20240709') 
    #return : 해당 구의 시작일부터 종료일까지의 모든 항목의 농도 dictionary 
        url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getMsrstnAcctoRDyrg'
        params ={'serviceKey' : 'R+8s9BHhcob1+/0e3PKTTRN7mTgLkVRHoS/rKZ2fRHhgQcvrffI0TvaHzh/406d2oF1iEU16aGKK5MJmimE9PA==', 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'inqBginDt' : init, 'inqEndDt' : end, 'msrstnName' : loc}
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()  # HTTP 에러 발생 시 예외를 발생시킵니다.
            result = json.loads(response.content)["response"]["body"]['items']
            return result       # JSON 형태로 데이터를 파싱하여 반환합니다.
        except requests.exceptions.HTTPError as err:
            print(f"HTTP 에러 발생: {err}")
        except requests.exceptions.RequestException as err:
            print(f"요청 에러 발생: {err}")

def find_worst_air_quality_regions(init, end):




    seoul_districts = [
        '강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', 
        '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', 
        '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', 
        '은평구', '종로구', '중구', '중랑구'
    ]
    
    district_averages = []
    
    for district in seoul_districts:
        district_data = air_condition_period_only_seoul(district, init, end)
        
        if district_data:
            pm10_values = [int(item['pm10Value']) for item in district_data if item['pm10Value'] != '-']
            if pm10_values:
                average_pm10 = sum(pm10_values) / len(pm10_values)
                district_averages.append({'district': district, 'average_pm10': average_pm10})
    
    # Sort districts by average PM10 values and get the top 5 worst
    district_averages_sorted = sorted(district_averages, key=lambda x: x['average_pm10'], reverse=True)
    top_5_worst = district_averages_sorted[:5]
    
    return top_5_worst

# 사용 예


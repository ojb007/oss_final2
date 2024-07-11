import requests
from air_korea_api import air_condition_realtime

def fetch_data():
    url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureLIst'
    params ={
        'serviceKey' : 'R+8s9BHhcob1+/0e3PKTTRN7mTgLkVRHoS/rKZ2fRHhgQcvrffI0TvaHzh/406d2oF1iEU16aGKK5MJmimE9PA==',
        'returnType' : 'json',
        'numOfRows' : '100',
        'pageNo' : '1',
        'itemCode' : 'PM10',
        'dataGubun' : 'DAILY',
        'searchCondition' : 'MONTH'
        }
    try:
        response = requests.get(url, params)
        response.raise_for_status()  # HTTP 에러 발생 시 예외를 발생시킵니다.
        return response.json()       # JSON 형태로 데이터를 파싱하여 반환합니다.
    except requests.exceptions.HTTPError as err:
        print(f"HTTP 에러 발생: {err}")
    except requests.exceptions.RequestException as err:
        print(f"요청 에러 발생: {err}")

# fullData = fetch_data()
# print(fullData)

def filter_data_by_date(data, date):
    """
    API에서 받은 데이터 중 특정 날짜에 해당하는 데이터만 필터링하는 함수.

    Args:
    data (dict): API로부터 받은 전체 데이터.
    date (str): 필터링할 날짜 (예: '2024-07-09').

    Returns:
    list: 특정 날짜에 해당하는 데이터 목록.
    """
    items = data
    return [item for item in items if item['dataTime'].startswith(date)]

def filter_data_by_date_and_region(data, date, region):
    """
    API에서 받은 데이터 중 특정 날짜와 지역에 해당하는 데이터만 필터링하는 함수.

    Args:
    data (dict): API로부터 받은 전체 데이터.
    date (str): 필터링할 날짜 (예: '2024-07-09').
    region (str): 필터링할 지역 (예: 'seoul').

    Returns:
    dict: 특정 날짜와 지역에 해당하는 데이터.
    """
    filtered_by_date = filter_data_by_date(data, date)
    region_data = [{region: item[region], 'dataTime': item['dataTime']} for item in filtered_by_date if region in item]
    return region_data

def assess_air_quality(data, region):
    """
    특정 지역의 미세먼지 농도에 따라 공기의 질을 평가하는 함수.

    Args:
    data (list of dict): 필터링된 데이터.
    region (str): 평가할 지역.

    Returns:
    str: 공기의 질 평가 결과.
    """
    if not data:
        return "데이터가 없습니다."
    try:
        pm10_value = int(data[0][region])  # 최신 데이터의 PM10 값을 추출
        if pm10_value <= 30:
            return "맑음"
        elif 31 <= pm10_value <= 80:
            return "보통"
        else:
            return "나쁨"
    except KeyError:
        return "지역 정보가 없습니다."
    except ValueError:
        return "미세먼지 수치를 확인할 수 없습니다."

# 사용 예
full_data = air_condition_realtime('PM10', 'DAILY')
specific_date = '2024-06-10'
specific_region = 'seoul'
filtered_data = filter_data_by_date_and_region(full_data, specific_date, specific_region)
air_quality = assess_air_quality(filtered_data, specific_region)
print(f"{specific_date} {specific_region}의 공기질: {air_quality}")
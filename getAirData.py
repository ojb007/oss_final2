import requests

def fetch_data():
    url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureLIst'
    params ={
        'serviceKey' : 'MQrOmcyT4jVjtpceKVFlzVAV7g2Aec3Wh1hvr2gw086NcElfzKtX93eY/qT9UG4dsTB/J/VnqjOS0RzSrnLdag==',
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
    items = data['response']['body']['items']
    return [item for item in items if item['dataTime'].startswith(date)]

full_data = fetch_data()  # 전체 데이터 가져오기
specific_date = '2024-06-10'  # 필터링할 날짜 최근 한달까지 가능
filtered_data = filter_data_by_date(full_data, specific_date)  # 특정 날짜 데이터 필터링
print(filtered_data)
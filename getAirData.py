import requests

def fetch_data():
    url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureLIst'
    params ={
        'serviceKey' : 'API_KEY',
        'returnType' : 'json',
        'numOfRows' : '100',
        'pageNo' : '1',
        'itemCode' : 'PM10',
        'dataGubun' : 'DAILY',
        'searchCondition' : 'WEEK'
        }
    try:
        response = requests.get(url, params)
        response.raise_for_status()  # HTTP 에러 발생 시 예외를 발생시킵니다.
        return response.json()       # JSON 형태로 데이터를 파싱하여 반환합니다.
    except requests.exceptions.HTTPError as err:
        print(f"HTTP 에러 발생: {err}")
    except requests.exceptions.RequestException as err:
        print(f"요청 에러 발생: {err}")

fullData = fetch_data()
print(fullData)

import requests
import json

def air_condition_period_only_seoul(loc, init, end) :
    #params : 구(서울에 속한 구만 가능), 시작일, 종료일 (ex: '강남구', '20240701', '20240709') 
    #return : 해당 구의 시작일부터 종료일까지의 모든 항목의 농도 dictionary 
    url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getMsrstnAcctoRDyrg'
    params ={'serviceKey' : 'R+8s9BHhcob1+/0e3PKTTRN7mTgLkVRHoS/rKZ2fRHhgQcvrffI0TvaHzh/406d2oF1iEU16aGKK5MJmimE9PA==', 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'inqBginDt' : init, 'inqEndDt' : end, 'msrstnName' : loc}
    response = requests.get(url, params=params)
    result = json.loads(response.content)["response"]["body"]['items']
    return result

def air_condition_city_realtime(loc) :
    #params : 시 이름 (ex:'서울')
    #return : 실시간(현재부터 24시간 전까지) 해당 시에 속한 모든 구의 모든 항목의 농도 dictionary

    url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureSidoLIst'
    params ={'serviceKey' : 'R+8s9BHhcob1+/0e3PKTTRN7mTgLkVRHoS/rKZ2fRHhgQcvrffI0TvaHzh/406d2oF1iEU16aGKK5MJmimE9PA==', 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : loc, 'searchCondition' : 'DAILY' }

    response = requests.get(url, params=params)
    result = json.loads(response.content)["response"]["body"]['items']
    return result

def air_condition_except_seoul_realtime(item) :
    #params : 필요한 항목 (ex: 'SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM2.5')
    #return : 실시간(현재부터 24시간 전까지) 모든 시도(서울 제외)의 해당 항목의 농도 dictionary
    url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureLIst'
    params ={'serviceKey' : 'R+8s9BHhcob1+/0e3PKTTRN7mTgLkVRHoS/rKZ2fRHhgQcvrffI0TvaHzh/406d2oF1iEU16aGKK5MJmimE9PA==', 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'itemCode' : item, 'dataGubun' : 'HOUR', 'searchCondition' : 'WEEK' }

    response = requests.get(url, params=params)
    result = json.loads(response.content)["response"]["body"]['items']
    return result

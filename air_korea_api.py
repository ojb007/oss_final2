
import requests


def showRange(loc, init, end) :
    url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getMsrstnAcctoRDyrg'
    params ={'serviceKey' : 'R+8s9BHhcob1+/0e3PKTTRN7mTgLkVRHoS/rKZ2fRHhgQcvrffI0TvaHzh/406d2oF1iEU16aGKK5MJmimE9PA==', 'returnType' : 'json', 'numOfRows' : '1', 'pageNo' : '1', 'inqBginDt' : init, 'inqEndDt' : end, 'msrstnName' : loc}
    response = requests.get(url, params=params)
    return response.content



def showLive(loc) :
    import requests

    url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureSidoLIst'
    params ={'serviceKey' : 'R+8s9BHhcob1+/0e3PKTTRN7mTgLkVRHoS/rKZ2fRHhgQcvrffI0TvaHzh/406d2oF1iEU16aGKK5MJmimE9PA==', 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : loc, 'searchCondition' : 'DAILY' }

    response = requests.get(url, params=params)
    print(response.content)
    
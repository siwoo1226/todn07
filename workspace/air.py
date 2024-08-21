import requests
#serviceKey='kSO2RngDT7nkh3eief3p9qtVbQJL3%2FvoXxPukP3AYWiRBHMkHCRMeuTuv8c1H%2FnkJ9A3lmESjag8Ahiwdd1GOA%3D%3D'
serviceKey='kSO2RngDT7nkh3eief3p9qtVbQJL3/voXxPukP3AYWiRBHMkHCRMeuTuv8c1H/nkJ9A3lmESjag8Ahiwdd1GOA=='
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={'serviceKey' : serviceKey, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : '울산', 'ver' : '1.0' }

response = requests.get(url, params=params)
air=response.text
print(air['response']['items'])

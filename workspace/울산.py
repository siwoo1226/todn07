import requests
serviceKey='kSO2RngDT7nkh3eief3p9qtVbQJL3/voXxPukP3AYWiRBHMkHCRMeuTuv8c1H/nkJ9A3lmESjag8Ahiwdd1GOA=='
url = 'http://apis.data.go.kr/6310000/citsapi/service/tim/vms'
params ={'serviceKey' : serviceKey, 'linkId' : '1920174600' }

response = requests.get(url, params=params)
print(response.content)
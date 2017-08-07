
# 클라이언트로 HTTP서비스와 통신


from urllib import request, parse


url = 'http://httpbin.org/get'

parms = {
    'name1':'value1',
    'name2':'value2',
}


header = {
    'user-agent' : 'name/ofyourbusiness'

}
querySting = parse.urlencode(parms)

# get요청후 응답 읽기

u = request.urlopen(url + '?' + querySting)
response = u.read()


# Post 요청후 응답 읽기

u = request.urlopen(url, querySting.encode('ascii'), header=header)
response = u.read()



import requests

response  = requests.post(url, data=parms, header=header)
text = response.text  # 요청 디코드한 텍스트가 들어있음
row = response.content # raw바이너리
json = response.json() # json으로 된 응답


import requests
import json
from bs4 import BeautifulSoup

##########################Get请求#######################

# 发送无参数的get请求
baiDu_response = requests.get('http://www.youxiake.com')
# print(baiDu_response.text)

bf = BeautifulSoup(baiDu_response.text,'lxml')
print(bf.find_all(content="155324732761750113563757"))
#发送无参数的get请求，设置超时时间timeout
baiDu_response = requests.get('http://www.baidu.com', timeout=0.1)

#查看请求的url地址
print('无参数的get请求地址是：'+baiDu_response.url)

#查看当前返回状态码
print('当前返回状态码是：'+str(baiDu_response.status_code))

#查看当前返回内容
print('当前返回内容是：'+baiDu_response.text)

#查看当前返回内容字节流
print('当前返回内容是：'+str(baiDu_response.content))

#带参数的请求
sendDictParams = {'keys':'alex','age':18}
baiDu_dictParams_response = requests.get('http://www.baidu.com',params=sendDictParams)
print('当前返回内容json：'+str(baiDu_dictParams_response.content))

#查看发送请求的url
print(baiDu_dictParams_response.url)
print(baiDu_dictParams_response.headers.get('Connection'))

#############cookies####################
cookies_response = requests.get('http://www.baidu.com')
print(str(cookies_response.cookies))

cookies = {'user-cookies': 'myCookies'}
custom_cookies_response = requests.get('http://www.baidu.com',cookies=cookies)
print(str(custom_cookies_response.cookies))
with open("百度.html","wb") as html:
    html.write(custom_cookies_response.content)
html.close()

import json
import os
import requests

# url = 'http://httpbin.org/post'
# d = {'key1':'value1','key2':'value2'}
# r = requests.post(url,data=d)
# print(r.text)

url = 'http://httpbin.org/post'
s = json.dumps({'key1':'value1','key2':'value2'})
r = requests.post(url,data=s)
print(r.text)

url = 'http://httpbin.org/post'
files = {'file':open('report.txt', 'rb')}
r = requests.post(url,files=files)
print(r.text)

file_name = '1.txt'
file_path = os.path.join(os.path.split(os.getcwd())[0], 'testfile', 'img', file_name)
print(file_path)
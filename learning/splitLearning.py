import os

str = 'adsd/123/jimmy'
print(str.split())
print(str.split("/"))
print(str.split("/",0))
print(str.split("/",1))
print(str.split("/",1)[1])
str1,str2,str3 = str.split("/",2)
print(str1+"\n"+str2+"\n"+str3)

str_www = "hello boy<[www.doiido.com]>byebye"

print(str_www.split("[",1)[1].split("]")[0].split("."))


import json

data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}

json_str = json.dumps(data)
json_loads = json.loads(json_str)
print(data)
print(json_str)
print(type(data))
print(type(json_str))
print(type(json_loads))
print(json_loads)

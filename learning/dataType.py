# -*- encoding:UTF-8 -*-
print("----------list-----------")
list = ['a','b','c']
list.append('d')
print(list.insert(0,'k'))
print(list.count('a'))
print(list)

print('----------tuple----------')
tuple = ("1",2,3)
print(tuple.index('2'))
print("----------dict-----------")
dict = {'michal': 12,"alex": 33}
print(dict.keys())
print(dict.get("alex"))
print(dict.values())
dict["cherry"]= 11
print(dict)
print("------------set----------")
s = set([1,2,2,2,4,5,3])
print(s)
s.add(6)
print(s)
print(s)
import os
def power(x,n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s * x
    return s

def person(name,age,*args,**kw):
    print("name=",name,"age=",age,"args=",args,"other=",kw)

result = power(6,3)
print(result)
print(person("alex",12))
print([x*x for x in range(1,11)])
print([x+1 for x in range(10,21)])
print([x + y for x in 'abc' for y in 'xyz'])
print([d for d in os.path.realpath("__init__")])
print( os.path.realpath("a"))
L = ['Hello','World','IBM','Apple']
print([s.lower() for s in L])
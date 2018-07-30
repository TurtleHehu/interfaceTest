import glob
import json
import os

pro_Dir = os.path.split(os.path.realpath(__file__))[0]
rpo_Dir = os.path.split(os.path.realpath(__file__))[0]
data = {'url':'http://www.youxiake.com','no':1, 'name':'wildTurtle'}

json_data = json.dumps(data)
print(data)
print(json_data)
print("1111")
data2 = json.loads(json_data)
print(data2)
print(data2['name'])

father_dir = os.path.dirname(os.getcwd())
print(os.getcwd())
print(father_dir)


class Glob():
    files = glob.glob(pro_Dir+'\*')
    for file in files:
        dir = os.path.dirname (file)
        file = os.path.basename(file)
        print(file)
    print (dir)

# if __name__ == '__main__':
#     Glob()
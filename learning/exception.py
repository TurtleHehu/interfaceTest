# -*- coding: UTF-8 -*-
#
# a = 10
# b = 0
#
#
# class exceptionTest():
#     try:
#         c = a / b
#         print(c)
#     except ZeroDivisionError as e:
#         print(e)
#     else:
#         print("no error happen")
#     finally:
#         print("do lastly")
# print("done")

# class MyException(Exception):
#     def __init__(self,message):
#         Exception.__init__(self)
#         self.message = message11
#
#
# a = input("please input a num:")
# if int(a) < 10:
#     try:
#         raise MyException("My exception is raised")
#     except MyException as e:
#         print(e.message)

try :
    num = int(input("input a number:"))
    print(100/num)
except ZeroDivisionError as e:
    print("不能为0")
    print(e)
else:
    print("congratulation!")
finally:
    print("ok!")
# -*- coding:UTF-8 -*-
import random

secret = random.randint(1, 10)
print("------game starting-------")
temp = input("请猜测下我心里的数字是多少：")
guess = int(temp)
i = 0

while guess != int(secret):
    while (i < 2):
        temp = input("请重新输入吧：")
        guess = int(temp)
        if guess == int(secret):
            print("你好柳陂啊！")
            print("真是够厉害的呀！")
        elif guess > int(secret):
            print("输入的值比我心里数字大")
        else:
            print("输入的值比我心里数字小")
        i = i+1

print("game over！")

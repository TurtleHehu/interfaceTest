from time import sleep

from selenium import webdriver

req_url = "http://www.haosou.com/s?ie=utf-8&shb=1&src=360sou_newhome&q=%E9%B2%9C%E8%8A%B1"

browser = webdriver.Chrome()

browser.get(req_url)
print(browser.current_url)
print(browser.get_cookies())
browser.back()
sleep(1)
browser.forward()
sleep(3)
browser.close()
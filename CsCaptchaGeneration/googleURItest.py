import time
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
import pyautogui
import base64
import math
import numpy as np
from PIL import Image
from skimage import measure
# storing the size of the screen


size = pyautogui.size()
print(size)
print(size.width)

from selenium.common import exceptions as EX
chrome_driver = r"C:/Users/Dero/anaconda3/envs/zy/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_driver)  # 声明一个浏览器对象
keyword = "cat"
url = "https://www.google.com/search?q={}&tbm=isch&ved=2ahUKEwi_5rTow8b6AhUTUN4KHRgDCXIQ2-cCegQIABAA&oq=cat+dog&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBggAEB4QDDIECAAQHjIECAAQHjIGCAAQHhAMMgYIABAeEAwyBAgAEB5QgwJY6AtgyBhoAHAAeACAAZ0BiAG8BZIBAzAuNZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=5yA8Y__WAZOg-QaYhqSQBw&bih=880&biw=929"
url = url.format(keyword)
browser.get(url)
time.sleep(0.5)
num = 3
urllist = []
for i in range(1, num+1):
    image1 = browser.find_element_by_xpath("//div[contains(@id, 'islrg')]/div/div[{}]/a/div/img".format(i))
    imaUrl1 = image1.get_attribute('src')
    urllist.append(imaUrl1)

print(urllist)
print(len(urllist))

# ir = base64.b64decode(imaUrl.split(',')[1])
# path = "D:/Desktop/"
# img = open(path + keyword + str(0) + '.jpg', 'wb')
# img.write(ir)


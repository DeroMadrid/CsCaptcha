"""
Title: New CsCaptcha Generation
Date: 2022-9-27
Author：Wang Long

Description:
---12宫格，一个问题对多个答案，
---保存TXT文档记录问题与答案，以及每张图片是文本还是图像（小图标题为(000)__keyword__text/image__(i).jpg
---并且记录每张CAPTCHA对应几个答案

revision:
---增加comet和commonsenseQA问题文本生成
---增加百度和谷歌爬图函数

"""

from __future__ import division
import json
import requests
import base64
from selenium import webdriver
from selenium.webdriver import ActionChains
import pyautogui
from PIL import Image
import os
import re
import random
import time
import shutil
from CsCaptchaTextObject import *


allimages = 'D:/Desktop/allimage/'  # 保存所有关键词对应的图片
imgPath = 'D:/Desktop/CaptchaImage2/'

# 所有大类
allClasses = ['comet', 'commonsense']
# weapon和vehicle不能同时出现


comelList = []
commonsenceList = []

# 记录所有问题 for 每个类别
# wanglong: 记录了每个大类别中的所有小类
allKeywords = {
    'comet': comelList,
    'commonsense': commonsenceList
}

allQuestion = {
    'comet': {},
    'commonsense': {}
}


# 判断是否合法路径
def jugePathMakeDir(path):
    if os.path.exists(path) == False:
        os.makedirs(path)
    return path + '/'


# 得到补充上的Comet和CommonsenseQA的所有关键词
def getAllKeyword():

    print("load keyword and question data ...")
    filepath = './extend'
    for file in os.listdir(filepath):  # comet and commonsense
        txtpath = filepath + '/' + file
        name = file.split('.')[0]
        with open(txtpath, encoding='utf-8') as fr:
            questionList = fr.readlines()
        for line in questionList:
            keyword = line.split('\t')[0]
            question = line.split('\t')[1]
            if keyword not in allKeywords.get(name):
                allKeywords.get(name).append(keyword)
                tmplist = [question.replace('\n', '')]
                allQuestion.get(name)[keyword] = tmplist
            else:
                allQuestion.get(name).get(keyword).append(question.replace('\n', ''))

    print("load data successfully!!")


# 得到目标关键词
def get_keyword_for_object(objectclass):
    keyindex = random.randint(0, len(allKeywords.get(objectclass)) - 1)  # 从该类别中选择一个小类作为关键词
    objectkeyword = allKeywords.get(objectclass)[keyindex]
    return objectkeyword


# 获取问题, 返回问题格式是(question, keyword)
def produceQuestion(objectkeyword, classname):
    questionIndex = random.randint(0, len(allQuestion.get(classname).get(objectkeyword)) - 1)
    objectquestion = allQuestion.get(classname).get(objectkeyword)[questionIndex]

    tmpKeyword = objectkeyword.replace('_', ' ').replace('*', '').lower()
    tmpQuestion = objectquestion.lower()

    return tmpQuestion, tmpKeyword


# 给关键词爬图，数量为num
def getImageGoogle(keyword, path, num):
    option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    chrome_driver = r"C:/Users/Dero/anaconda3/envs/zy/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe"
    browser = webdriver.Chrome(executable_path=chrome_driver, chrome_options=option)  # 声明一个浏览器对象

    url = "https://www.google.com/search?q={}&tbm=isch&ved=2ahUKEwi_5rTow8b6AhUTUN4KHRgDCXIQ2-cCegQIABAA&oq=cat+dog&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBggAEB4QDDIECAAQHjIECAAQHjIGCAAQHhAMMgYIABAeEAwyBAgAEB5QgwJY6AtgyBhoAHAAeACAAZ0BiAG8BZIBAzAuNZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=5yA8Y__WAZOg-QaYhqSQBw&bih=880&biw=929"
    url = url.format(keyword)
    browser.get(url)
    # time.sleep(1)
    for i in range(1, num+1):
        image1 = browser.find_element_by_xpath("//div[contains(@id, 'islrg')]/div/div[{}]/a/div/img".format(i))
        imaUrl = image1.get_attribute('src')
        print('1正在下载：%s' % imaUrl)
        try:
            if "https://" in imaUrl:
                print("https")
                ir = requests.get(imaUrl, timeout=(6.05, 12.05))
                img = open(path + keyword + str(i) + '.jpg', 'wb')
                img.write(ir.content)
            else:
                ir = base64.b64decode(imaUrl.split(',')[1])
                img = open(path + keyword + str(i) + '.jpg', 'wb')
                img.write(ir)
        except Exception:
            print("下载失败")
            # ir = requests.get(imaUrl, timeout=(6.05, 12.05))
            # img = open(path + keyword + str(i) + '.jpg', 'wb')
            # img.write(ir.content)
    browser.close()


# 给关键词爬图，数量为1
def getImage(keyword, path):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    params = {
        'tn': 'resultjson_com',
        'logid': 10287795170650392256,
        'ipn': 'rj',
        'ct': 201326592,
        'is': '',
        'fp': 'result',
        'fr': '',
        'word': keyword,
        'queryWord': keyword,
        'cl': 2,
        'lm': -1,
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': -1,
        'z': '',
        'ic': 0,
        'hd': '',
        'latest': '',
        'copyright': '',
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': 0,
        'istype': 2,
        'qc': '',
        'nc': 1,
        'expermode': '',
        'nojc': '',
        'isAsync': '',
        'pn': 0,
        'rn': 30,
        'gsm': '1e',
        '1664435415912': '',
    }
    # 只爬一张图片
    url = 'https://image.baidu.com/search/acjson'
    print(keyword)
    result = requests.get(url, headers=header, params=params)

    urls = re.findall('"thumbURL":"(.*?)"', result.text)
    finalurl = ''
    for url in urls:
        if "img" in url:
            finalurl = url
            break
        else:
            finalurl = urls[0]
    print('正在下载：%s' % finalurl)
    try:
        ir = requests.get(finalurl, timeout=(6.05, 12.05))
        img = open(path + keyword + str(0) + '.jpg', 'wb')
        img.write(ir.content)
    except Exception:
        print("下载未成功，重新爬取尝试")


# 选择多个目标图片并保存
def savePicFormore(keyword, queryKey, picpath, savepath, num):
    objectfiles = []  # 保存目标图片列表
    filelist = []  # 此关键词下所有图片列表
    ansfiles = []  # 保存图片save name

    jugePathMakeDir(picpath)
    getImageGoogle(keyword, picpath, num)
    for file in os.listdir(picpath):
        filelist.append(file)
    # 当场爬图
    i = 0
    while (i < num):
        picindex = random.randint(0, len(filelist) - 1)
        if filelist[picindex] not in objectfiles:  # 图片不能重复
            objectfiles.append(filelist[picindex])
            i += 1
        else:
            continue
    print(str(objectfiles))  # 所有目标图片

    for idx in range(len(objectfiles)):  # 复制/移动
        shutil.copy(picpath + '/' + objectfiles[idx],
                    savepath + "000__" + keyword.replace('_', ' ').replace('-', ' ') + '__image__' + str(idx) + '.jpg')
        ansfiles.append("000__" + keyword.replace('_', ' ').replace('-', ' ') + '__image__' + str(idx) + '.jpg')

    return ansfiles


# 选择干扰图片
def getOtherKeywords(keyword, num, picpath, savepath):
    otherkeywordlist = []  # 干扰关键词

    otherpicpathlist = []  # 其他干扰项的图片地址
    otherkeywordnum = []  # 其他干扰项的图片数目

    othernum = 12 - num

    while (othernum > 0):  # 选取干扰项
        tmpkey = keyword
        while tmpkey == keyword or tmpkey in otherkeywordlist:
            tmpnum = random.randint(0, len(allKeywords.get('comet')) - 1)
            tmpkey = allKeywords.get('comet')[tmpnum]
        otherkeywordlist.append(tmpkey)
        picpath1 = picpath + tmpkey + "/"
        jugePathMakeDir(picpath1)
        getImageGoogle(tmpkey, picpath1, 1)
        for file in os.listdir(picpath1):
            otherpicpathlist.append(file)

            shutil.copy(picpath1 + file,
                        savepath + tmpkey + '__image__' + str(12 - othernum) + '.jpg')

        othernum -= 1

    return otherkeywordlist


# 重置图片大小
def resizePic(savepath):
    for file in os.listdir(savepath):
        bgimg = Image.new('RGB', (150, 150), 'white')
        img = Image.open(savepath + file, 'r')
        if (img.width > img.height):
            randWidth = 150
            img2 = img.resize((randWidth, int(img.height / (img.width / (randWidth * 1.0)))), Image.ANTIALIAS)
        else:
            randHeight = 150
            img2 = img.resize((int(img.width / (img.height / (randHeight * 1.0))), randHeight), Image.ANTIALIAS)
        bgimg.paste(img2, (int((bgimg.width - img2.width) / 2), int((bgimg.height - img2.height) / 2)))
        bgimg.save(savepath + file, quality=95)


# 生成文本图片
def getTextPic(keyword, savepath, i, isAns):  # keyword若有‘_’，用‘ ’替代
    text_bg = getBackground()
    style = random.choice([True, False])
    if style == True:  # 整个单词是同一风格，label的部分如果是有空格的如'happy newyear'，则用'\n'代替' '
        textcaptcha = GenerateTextCaptcha(text_bg, keyword.replace(' ', '\n'), entire=style)
    else:  # 整个单词五颜六色
        textcaptcha = GenerateTextCaptcha(text_bg, keyword, entire=style)

    if isAns:
        textcaptcha.save(savepath + '000__' + keyword + '__text__' + str(i) + '.jpg', 'JPEG')  # 路径
        return '000__' + keyword + '__text__' + str(i) + '.jpg'
    else:
        textcaptcha.save(savepath + keyword + '__text__' + str(i) + '.jpg', 'JPEG')  # 路径
        return keyword + '__text__' + str(i) + '.jpg'


# main function
if __name__ == '__main__':
    getAllKeyword()
    index = 823
    tmpclasses = allClasses  # 其他类别
    while index < 1000:
        print('index: ', str(index))
        picNum = 0
        savepath = jugePathMakeDir(imgPath + 'Challenge' + str(index))  # 第index张图片暂存，12张
        while picNum != 12:
            if os.path.exists(savepath):
                shutil.rmtree(savepath)
            savepath = jugePathMakeDir(imgPath + 'Challenge' + str(index))
            classindex_A = random.randint(0, len(allClasses) - 1)  # 从所有大类中选一个类别
            objectclass_A = allClasses[classindex_A]  # comet or commonsense
            objectkeyword_A = get_keyword_for_object(objectclass_A)  # 目标关键词---object A， 该值要保存
            print('class_A:', objectclass_A, '  object_A:', objectkeyword_A)

            # 生成问题和查询关键词
            question_A, queryKey_A = produceQuestion(objectkeyword_A, objectclass_A)

            # 共有几张目标图片, 该值要保存
            ans_num = random.randint(1, 3)
            print('ans_num: ', ans_num)
            ansPath = []  # 此列表保存所有答案图片名

            picpath_A = "D:/allimage/" + objectclass_A + '/challenge' + str(index) + '/' + objectkeyword_A + '/'
            tmplist = savePicFormore(objectkeyword_A, queryKey_A, picpath_A, savepath, ans_num)

            print(tmplist)
            for k in range(len(tmplist)):
                ansPath.append(tmplist[k])
            print('ansPath: ', str(len(ansPath)))
            print('Question_A:', question_A, '  Query_A:', queryKey_A)


            otherKeywordlist = getOtherKeywords(objectkeyword_A, ans_num, "D:/allimage/" + objectclass_A + '/challenge'
                                                + str(index) + '/', savepath)

            resizePic(savepath)
            imgNum = len(os.listdir(savepath))
            picNum = imgNum
            ansQuestion = [question_A]
            ansQuery = [queryKey_A]
            ansKeyword = [objectkeyword_A]

        with open('./question_text/question-2022-10-08.txt', 'a', encoding='utf-8') as fw:
            strline = str(index) + '.\t' + str(ansQuestion) + '\t' + str(ansPath) + '\t' + str(ansKeyword) + '\t' + str(
                ansKeyword * ans_num + otherKeywordlist) + '\t' + str(ans_num) + '\n'
            fw.write(strline)

        index += 1

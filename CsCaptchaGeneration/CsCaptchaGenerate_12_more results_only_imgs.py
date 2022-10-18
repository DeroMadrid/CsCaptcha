"""
Title: CsCAPTCHA for uncertain answers
Date: 2019-8-17
Author：Gao Yipeng

Description:
---12宫格，一个问题对多个答案，
---保存TXT文档记录问题与答案，以及每张图片是文本还是图像（小图标题为(000)__keyword__text/image__(i).jpg
---并且记录每张CAPTCHA对应几个答案

second revision : wanglong
fix download function

"""

from __future__ import division
from PIL import Image
import os
import re
import random
import time
import shutil
from CsCaptchaTextObject import *

alltxt = './alltxt/'  # 保存所有问题文本
allimages = 'D:/Desktop/allimage/'  # 保存所有关键词对应的图片
imgPath = 'D:/Desktop/genimage/'

# 所有大类
allClasses = ['animal', 'appliance', 'clothes', 'drink', 'furniture', 'fruit', 'plant',
              'tableware', 'instrument', 'job', 'sport', 'vehicle', 'weapon']
# weapon和vehicle不能同时出现
no_weapon_and_vehicle = ['animal', 'appliance', 'clothes', 'drink', 'furniture', 'plant',
                         'fruit', 'tableware', 'instrument', 'job', 'sport']

animalList = []
applianceList = []
clothesList = []
drinkList = []
fruitList = []
furnitureList = []
instrumentList = []
jobList = []
plantList = []
scenesList = []
sportList = []
tablewareList = []
toolsList = []
vehicleList = []
vegetableList = []
waterList = []
weaponList = []

# 记录所有问题 for 每个类别
# wanglong: 记录了每个大类别中的所有小类
allKeywords = {
    'animal': animalList,
    'appliance': applianceList,
    'clothes': clothesList,
    'drink': drinkList,
    'fruit': fruitList,
    'furniture': furnitureList,
    'instrument': instrumentList,
    'job': jobList,
    'plant': plantList,
    # 'scenes': scenesList,
    'sport': sportList,
    'tableware': tablewareList,
    # 'tools': toolsList,
    'vehicle': vehicleList,
    # 'water': waterList,
    'weapon': weaponList
}


# 判断是否合法路径
def jugePathMakeDir(path):
    if os.path.exists(path) == False:
        os.makedirs(path)
    return path + '/'


# 得到所有关键词
def getAllKeyword():
    for tmpclass in allClasses:
        filepath = './alltxt/' + tmpclass
        for file in os.listdir(filepath):
            allKeywords.get(tmpclass).append(file.split('.')[0])
        # print(str(allKeywords.get(tmpclass)))


# 得到目标关键词
def get_keyword_for_object(objectclass):
    keyindex = random.randint(0, len(allKeywords.get(objectclass)) - 1)  # 从该类别中选择一个小类作为关键词
    objectkeyword = allKeywords.get(objectclass)[keyindex]
    return objectkeyword


# 获取问题
def produceQuestion(objectkeyword, txtpath):
    with open(txtpath, encoding='utf-8') as fr:
        questionList = fr.readlines()
    questionIndex = random.randint(0, len(questionList) - 1)
    if (questionList[questionIndex].find('@') != -1):
        objectquestion = questionList[questionIndex].strip().split('@')[0].split('\t')[1]
        queryKey = questionList[questionIndex].strip().split('@')[1]
    else:
        objectquestion = questionList[questionIndex].strip().split('\t')[1]
        queryKey = questionList[questionIndex].strip().split('\t')[0]
    tmpKeyword = objectkeyword.replace('_', ' ').replace('*', '').lower()
    tmpQuestion = objectquestion.lower()

    # 正则表达式 替换关键词 re.sub 生成问题文本(判断冠词a/an/theo以及定语your)
    # question = tmpQuestion.replace(('[[a ' or '[[an ' or '[[the ' or '[[your ') + tmpKeyword + ']]', 'which one').replace('[[' + tmpKeyword + ']]', 'which one').replace('[', '').replace(']', '')
    if (tmpQuestion.find('[[a ' + tmpKeyword + ']]') != -1):
        question = tmpQuestion.replace('[[a ' + tmpKeyword + ']]', 'which one').replace('[[', '').replace(']]',
                                                                                                          '').replace(
            '[', '').replace(']', '')
    elif (tmpQuestion.find('[[an ' + tmpKeyword + ']]') != -1):
        question = tmpQuestion.replace('[[an ' + tmpKeyword + ']]', 'which one').replace('[[', '').replace(']]',
                                                                                                           '').replace(
            '[', '').replace(']', '')
    elif (tmpQuestion.find('[[the ' + tmpKeyword + ']]') != -1):
        question = tmpQuestion.replace('[[the ' + tmpKeyword + ']]', 'which one').replace('[[', '').replace(']]',
                                                                                                            '').replace(
            '[', '').replace(']', '')
    elif (tmpQuestion.find('[[your ' + tmpKeyword + ']]') != -1):
        question = tmpQuestion.replace('[[your ' + tmpKeyword + ']]', 'which one').replace('[[', '').replace(']]',
                                                                                                             '').replace(
            '[', '').replace(']', '')
    else:
        question = tmpQuestion.replace('[[' + tmpKeyword + ']]', 'which one').replace('[[', '').replace(']]',
                                                                                                        '').replace('[',
                                                                                                                    '').replace(
            ']', '')
    return question, queryKey


# 选择多个目标图片并保存
def savePicFormore(keyword, queryKey, picpath, savepath, num):
    objectfiles = []  # 保存目标图片列表
    filelist = []  # 此关键词下所有图片列表
    ansfiles = []  # 保存图片save name
    for file in os.listdir(picpath):
        filelist.append(file)
    i = 0
    while (i < num):
        # 原来部分如下：wanglong 2022/9/29 修改，删掉了下面的while循环的检测代码
        # tmpkey = 'error'
        # while (tmpkey.find(queryKey) == -1):
        #     picindex = random.randint(0, len(filelist) - 1)
        #     tmpkey = filelist[picindex].split('.')[0]

        # 现部分如下：
        picindex = random.randint(0, len(filelist) - 1)
        tmpkey = filelist[picindex].split('.')[0]
        if (filelist[picindex] not in objectfiles):  # 图片不能重复
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
def getOtherKeywords(class_A, num, imagepath):
    otherclasses = list(set(allClasses) - set([class_A]))
    if 'vehicle' in [class_A] or 'weapon' in [class_A]:
        otherclasses = list(set(no_weapon_and_vehicle) - set([class_A]))
    otherkeywordlist = []  # 干扰关键词
    otherpicpathlist = []  # 其他干扰项的图片地址
    otherkeywordnum = []  # 其他干扰项的图片数目

    othernum = 12 - num
    while (othernum > 0):  # 选取干扰项
        tmpnum = random.randint(1, min(3, othernum))
        # tmpnum = 1
        otherkeywordnum.append(tmpnum)
        othernum -= tmpnum

    for i in range(len(otherkeywordnum)):  # 共有几个干扰类别
        otherclass = class_A
        while (class_A == otherclass):
            classindex = random.randint(0, len(tmpclasses) - 1)  # 选一个类别
            otherclass = tmpclasses[classindex]
        keyindex = random.randint(0, len(allKeywords.get(otherclass)) - 1)
        otherclasskeyword = allKeywords.get(otherclass)[keyindex]
        if otherkeywordnum[i] > 1:
            # tmp = getTextPic(otherclasskeyword, savepath, 0, False)
            # otherkeywordlist.append(otherclasskeyword)  # 多了一个keyword被记录，这一行注释掉
            j = 0
            while (j < otherkeywordnum[i]):  # 每个干扰类别有几张图
                otherkeywordlist.append(otherclasskeyword)
                # print(str(otherkeywordlist))
                filelist = []
                otherclasspath = os.path.join(allimages, otherclass, otherclasskeyword)
                # 选择几张文本图片

                for file in os.listdir(otherclasspath):
                    filelist.append(file)
                picindex = random.randint(0, len(filelist) - 1)
                if (filelist[picindex] not in otherpicpathlist):  # 图片不能重复
                    otherpicpathlist.append(otherclasspath + filelist[picindex])
                    shutil.copy(otherclasspath + '/' + filelist[picindex],
                                savepath + otherclasskeyword + '__image__' + str(j) + '.jpg')
                    j += 1
                else:
                    continue
        else:
            j = 0
            while (j < otherkeywordnum[i]):  # 每个干扰类别有几张图
                otherkeywordlist.append(otherclasskeyword)
                # print(str(otherkeywordlist))
                filelist = []
                otherclasspath = os.path.join(allimages, otherclass, otherclasskeyword)
                # 选择几张文本图片

                for file in os.listdir(otherclasspath):
                    filelist.append(file)
                picindex = random.randint(0, len(filelist) - 1)
                if (filelist[picindex] not in otherpicpathlist):  # 图片不能重复
                    otherpicpathlist.append(otherclasspath + filelist[picindex])
                    shutil.copy(otherclasspath + '/' + filelist[picindex],
                                savepath + otherclasskeyword + '__image__' + str(j) + '.jpg')
                    j += 1
                else:
                    continue
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
    index = 12
    tmpclasses = allClasses  # 其他类别
    while index < 20:
        print('index: ', str(index))
        picNum = 0
        savepath = jugePathMakeDir(imgPath + 'Challenge' + str(index))  # 第index张图片暂存，12张
        while picNum != 12:
            if os.path.exists(savepath):
                shutil.rmtree(savepath)
            savepath = jugePathMakeDir(imgPath + 'Challenge' + str(index))
            classindex_A = random.randint(0, len(allClasses) - 1)  # 从所有大类中选一个类别
            objectclass_A = allClasses[classindex_A]
            objectkeyword_A = get_keyword_for_object(objectclass_A)  # 目标关键词---object A， 该值要保存
            print('class_A:', objectclass_A, '  object_A:', objectkeyword_A)
            if (objectclass_A == 'weapon' or objectclass_A == 'vehicle'):
                tmpclasses = no_weapon_and_vehicle

            # 生成问题和查询关键词
            txtpath_A = './alltxt/' + objectclass_A + '/' + objectkeyword_A + '.txt'
            question_A, queryKey_A = produceQuestion(objectkeyword_A, txtpath_A)

            # 共有几张目标图片, 该值要保存
            ans_num = random.randint(1, 3)
            print('ans_num: ', ans_num)
            ansPath = []  # 此列表保存所有

            # 为目标图片随机选择文本验证码图片
            text_object_num = 0  # 没有文本图片
            if text_object_num == 1:
                ansPath.append(getTextPic(objectkeyword_A.replace('_', ' ').replace('-', ' '), savepath, 0, True))
            picpath_A = os.path.join(allimages, objectclass_A, objectkeyword_A)
            tmplist = savePicFormore(objectkeyword_A, queryKey_A, picpath_A, savepath, ans_num - text_object_num)
            print(tmplist)
            for k in range(len(tmplist)):
                ansPath.append(tmplist[k])
            print('ansPath: ', str(len(ansPath)))

            print('Question_A:', question_A, '  Query_A:', queryKey_A)

            otherKeywordlist = getOtherKeywords(objectclass_A, ans_num, savepath)
            # ansPath = sorted(os.listdir(savepath)[0:1], key=lambda x: os.path.getmtime(os.path.join(savepath, x)))
            resizePic(savepath)
            imgNum = len(os.listdir(savepath))
            # ansPos, imgNum = pastePic(savepath, resultPath, index)
            # print(ansPos)
            picNum = imgNum
            ansQuestion = [question_A]
            ansQuery = [queryKey_A]
            ansKeyword = [objectkeyword_A]

        with open('./question_text/question-2022-9-29.txt', 'a', encoding='utf-8') as fw:
            strline = str(index) + '.\t' + str(ansQuestion) + '\t' + str(ansPath) + '\t' + str(ansKeyword) + '\t' + str(
                ansKeyword * ans_num + otherKeywordlist) + '\t' + str(ans_num) + '\n'
            fw.write(strline)

        index += 1

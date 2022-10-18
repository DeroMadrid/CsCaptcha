from __future__ import division
from PIL import Image
import os
import re
import random
import time
import shutil
from CsCaptchaTextObject import *

alltxt = './alltxt/'  # 保存所有问题文本

allClasses = ['animal', 'appliance', 'clothes', 'drink', 'furniture', 'fruit', 'plant',
              'tableware', 'instrument', 'job', 'sport', 'vehicle', 'weapon']

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
    'scenes': scenesList,
    'sport': sportList,
    'tableware': tablewareList,
    'tools': toolsList,
    'vehicle': vehicleList,
    'water': waterList,
    'weapon': weaponList
}

noClassifylist = []


# 得到所有关键词
def getAllKeyword():
    for tmpclass in allClasses:
        filepath = './wltxt/' + tmpclass
        for file in os.listdir(filepath):
            allKeywords.get(tmpclass).append(file.split('.')[0])
        # print(str(allKeywords.get(tmpclass)))


def checkExist(keyword):
    flag = "not exist"
    if keyword in animalList:
        flag = "animal"
    if keyword in applianceList:
        flag = "appliance"
    if keyword in clothesList:
        flag = "clothes"
    if keyword in drinkList:
        flag = "drink"
    if keyword in fruitList:
        flag = "fruit"
    if keyword in furnitureList:
        flag = "furniture"
    if keyword in instrumentList:
        flag = "instrument"
    if keyword in jobList:
        flag = "job"
    if keyword in plantList:
        flag = "plant"
    if keyword in scenesList:
        flag = "scenes"
    if keyword in sportList:
        flag = "sport"
    if keyword in tablewareList:
        flag = "tableware"
    if keyword in toolsList:
        flag = "tools"
    if keyword in vehicleList:
        flag = "vehicle"
    if keyword in waterList:
        flag = "water"
    if keyword in weaponList:
        flag = "weapon"

    return flag


def Classify(keyword):
    flag = "xxx"
    return flag


if __name__ == '__main__':
    questionpath = "D:/Desktop/知识图谱数据集/COMET/COMETQuestion.txt"
    with open(questionpath, encoding='utf-8') as fr:
        questionList = fr.readlines()
    print(questionList)
    for line in questionList:
        keyword1 = line.split('\t')[0]
        if keyword1 not in noClassifylist:
            noClassifylist.append(keyword1)
    print(noClassifylist)

        # tem = checkExist(keyword1)
        # if tem == "not exist":
        #     newTerm = Classify(keyword1)
        #     filepath = "./wltxt/" + newTerm + "/"
        #     os.mkdir(filepath)
        #     txtpath = filepath + keyword1 + ".txt"
        #     with open(txtpath, 'a', encoding='utf-8') as fw:
        #         fw.write(line)
        # else:
        #     txtpath = "./wltxt/" + tem + "/" + keyword1 + ".txt"
        #     with open(txtpath, 'a', encoding='utf-8') as fw:
        #         fw.write(line)
        # # 这里应该实现一个函数来对关键词进行分类，首先判断是否在各个大类中已经存在。 如果已经存在，直接将问题扩充到关键词的问题txt中
        # # 如果不在，分类思想是： 根据判断关键词 和 16个大类进行逐个比较，得到一个可能性系数，归为系数权重最大的大类中。 随后创建新的关键词问题文本txt，将问题扩充进去。
        # #


'''
Description:    下载图片
Date:   2018/12/26
Author: Gao Yipeng

Date:   2021/9/27
Remix:  Wang Long
Description:   修改代码
revision: 修改爬图函数，正常从百度图片中爬取图片
'''

import requests
import os
import json

# 所有问题列表
animalList = []
applianceList = []
clothesList = []
drinkList = []
fruitList = []
furnitureList = []
instrumentList = []
jobList = []
plantList = []
sportList = []
tablewareList = []
toolsList = []
vehicleList = []
vegetableList = []
waterList = []
weaponList = []

# 所有的大类
allClasses = ['animal', 'appliance', 'clothes', 'drink', 'furniture', 'fruit', 'plant',
              'tableware', 'instrument', 'job', 'sport', 'vehicle', 'weapon']

# 记录所有问题
allQuestions = {
    'animal': animalList,
    'appliance': applianceList,
    'clothes': clothesList,
    'drink': drinkList,
    'furniture': furnitureList,
    'instrument': instrumentList,
    'job': jobList,
    'plant': plantList,
    'sport': sportList,
    'tableware': tablewareList,
    'vehicle': vehicleList,
    'weapon': weaponList
}


# 得到所有问题列表
def getAllQuestionList():
    for tmpclass in allClasses:
        filepath = './questions/' + tmpclass + '.txt'
        with open(filepath) as fr:
            tmplist = fr.readlines()
        for line in tmplist:
            allQuestions.get(tmpclass).append(line)


# 判断路径下文件夹是否存在,不存在则创建路径并返回
def jugePathMakeDir(path):
    if os.path.exists(path) == False:
        os.makedirs(path)
    return path + '/'


# 从百度上扒图
def getManyPages(keyword, pages):
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
        'rn': 60,
        'gsm': '1e',
        '1664435415912': '',
    }
    url = 'https://image.baidu.com/search/acjson'
    urls = []

    result = requests.get(url, headers=header, params=params)
    r = result.text
    r.replace('\\', '////')
    try:
        result1 = json.loads(r, strict=False)
        for line in result1['data'][:-1]:
            urls.append(line['thumbURL'])
    except:
        print("chuxian fanxiegang")
    return urls  # 返回所有缩略图url


# 每一个保存60张
def getImg(dataList, localPath, keyword):
    result = None
    flag = False
    urls = []
    for list in dataList:
        urls.append(list)
    if not os.path.exists(localPath):  # 新建文件夹
        os.mkdir(localPath)
    i = 0
    for url in urls:
        try:
            # if url.get('thumbURL') != None:
            #     print('正在下载：%s' % url.get('thumbURL'))
            #     try:
            #         ir = requests.get(url.get('thumbURL'), timeout=10)
            #     except requests.exceptions.ReadTimeout:
            #         print('HTTP超时')
            #         continue
            #     except requests.exceptions.ConnectionError:
            #         print('当前请求的URL地址出现错误')
            #         continue
            #     except Exception:
            #         continue
            #     img = open(localPath + keyword + str(i) + '.jpg', 'wb')
            #     img.write(ir.content)
            #     i += 1
            # else:
            #     print('图片链接不存在,重新下载')  # 图片链接不存在需要重新查找
            #     continue
            print('正在下载：%s' % url)
            try:
                ir = requests.get(url, timeout=10)
            except requests.exceptions.ReadTimeout:
                print('HTTP超时')
                continue
            except requests.exceptions.ConnectionError:
                print('当前请求的URL地址出现错误')
                continue
            except Exception:
                continue
            img = open(localPath + keyword + str(i) + '.jpg', 'wb')
            img.write(ir.content)
            i += 1

        except Exception:
            continue


# 60张
def baiduPicSave(keyword, savepath):
    dataList = getManyPages(keyword, 2)  # 参数1:关键字，参数2:要下载的页数
    getImg(dataList, savepath, keyword)


if __name__ == '__main__':
    # '''
    for i in range(len(allClasses)):
        print(allClasses[i])
        for file in os.listdir('./alltxt/' + allClasses[i] + '/'):  # 每一个关键词
            keywordname = file.split('.')[0]  # 关键词
            questionlist = []  # 每一个关键词的问题
            querylist = []  # 查询关键词
            with open('./alltxt/' + allClasses[i] + '/' + file, encoding='utf-8') as f:
                questionlist = f.readlines()
            for line in questionlist:  # 对每个问题都记录查询关键词querykey
                if (line.strip().find('@') != -1):
                    querykey = line.strip().split('@')[1]
                else:
                    querykey = line.strip().split('\t')[0]
                if (querykey not in querylist):  # 获取此关键词下的所有查询querykey
                    querylist.append(querykey)
            # print(str(querylist))
            savepath = './allimage/' + allClasses[i] + '/' + keywordname + '/'
            jugePathMakeDir(savepath)
            for key in querylist:
                print(key)
                tmp = 0
                for keyfile in os.listdir(savepath):
                    if (keyfile.find(key) != -1):
                        tmp += 1
                if tmp < 50:
                    baiduPicSave(key, savepath)

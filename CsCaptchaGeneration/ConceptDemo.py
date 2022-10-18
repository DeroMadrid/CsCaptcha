"""
wanglong
purpose: 来获取conceptnet相关的问题文本

需要统计问题文本中所有的关系属性
随后根据问题文本的关系属性来对问题文本进行筛选。

完善代码，实现直接对txt文件进行修改，保存
"""

import requests
KeyWord = "jacket"  # 搜索的关键词
lengthOfList = 1000  # 搜索结果每一页中条目数量，（尽可能大，保证能一次性得到所有的内容条目来放到一个json文件中）
URI = "http://api.conceptnet.io/c/en/" + KeyWord + "?offset=0&limit=" + str(lengthOfList)
# 更换查询的关键词需要在下面obj的查询URI中进行更换：
obj = requests.get(URI, verify=False).json()
print(obj.keys())  # json中包括context，id，edge和version，其中edge中的是需要的关系条目
num = len(obj['edges'])  # 得到一共有多少个和关键词有关系的条目
print(len(obj['edges']))

txtpath = "D:/Desktop/txt/" + KeyWord + ".txt"  # 用来保存问题文本的txt文件

correct_count = 0  # 在逐个遍历中得到可以作为问题的条目数量。
Rel_list = ['RelatedTo', 'Synonym', 'IsA', 'PartOf', 'MannerOf', 'HasA', 'AtLocation', 'UsedFor', 'HasProperty',
            'CreatedBy', 'CapableOf', 'DistinctFrom', 'Desires', 'NotDesires', 'Antonym', 'HasPrerequisite',
            'ReceivesAction', 'CausesDesire', 'DefinedAs', 'HasSubevent']  # 用来存放所有的关系属性种类

Need_list = ['IsA', 'PartOf', 'MannerOf', 'HasA', 'AtLocation', 'UsedFor', 'HasProperty',
            'CreatedBy', 'CapableOf', 'DistinctFrom', 'Desires', 'NotDesires', 'Antonym', 'HasPrerequisite',
            'ReceivesAction', 'CausesDesire', 'DefinedAs', 'HasSubevent']  # 选择需要的关系属性种类

# 所有的可能关系种类
# ['RelatedTo', 'Synonym', 'IsA', 'PartOf', 'MannerOf', 'HasA', 'AtLocation', 'UsedFor', 'HasProperty',
# 'CreatedBy', 'CapableOf', 'DistinctFrom']

# ['RelatedTo', 'Synonym', 'IsA', 'PartOf', 'MannerOf', 'HasA', 'AtLocation', 'UsedFor', 'HasProperty',
# 'CreatedBy', 'CapableOf', 'DistinctFrom', 'Desires', 'NotDesires', 'Antonym', 'HasPrerequisite', 'ReceivesAction',
# 'CausesDesire', 'DefinedAs', 'HasSubevent']

for i in range(num):
    if obj['edges'][i]['surfaceText'] and obj['edges'][i]['rel']['label'] in Need_list:
        correct_count += 1
        print(correct_count, ": ", obj['edges'][i]['surfaceText'], ", ", obj['edges'][i]['rel']['label'])
        rel_label = obj['edges'][i]['rel']['label']

        # surfacetext可以作为问题文本， /rel/label 是关系属性
        # print(correct_count, ": ", obj['edges'][i]['rel']['label'])
        # if rel_label not in Rel_list:  # 遍历得到所有的关系属性名
        #     Rel_list.append(rel_label)

        with open(txtpath, 'a', encoding='utf-8') as fw:
            lines = KeyWord + '\t' + obj['edges'][i]['surfaceText'] + '\n'
            fw.write(lines)

# print(Rel_list)

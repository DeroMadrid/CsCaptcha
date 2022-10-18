"""
wanglong

目的：将COMET数据集中的数据转化为需要的问题文本格式

过程：读取数据，根据每一行数据的关系类别进行不同的问题转化。
    对需要的问题进行保留，并根据关键词来生成对应的问题。
"""

txtPath = "D:/Desktop/知识图谱数据集/COMET/test1.txt"
questionpath = "D:/Desktop/知识图谱数据集/COMET/COMETQuestion.txt"
with open(txtPath, encoding='utf-16') as fr:
    questionList = fr.readlines()

print(len(questionList))

rel_list = []

# ['oEffect', 'oReact', 'oWant', 'xAttr', 'xEffect', 'xIntent', 'xNeed', 'xReact', 'xWant', 'AtLocation', 'ObjectUse',
# 'Desires', 'HasProperty', 'NotDesires', 'Causes', 'HasSubEvent', 'xReason', 'CapableOf', 'MadeUpOf', 'isAfter',
# 'isBefore', 'isFilledBy', 'HinderedBy']
answer = ""
question = ""
for i in range(len(questionList)):
    rel = questionList[i].split('\t')[1]
    keyword1 = questionList[i].split('\t')[0]
    keyword2 = questionList[i].split('\t')[2]
    if rel == "HasProperty":
        question = "What is " + keyword2 + "?"
        answer = keyword1
        line = answer + '\t' + question + '\n'

    elif rel == "ObjectUse":
        question = "What is used to " + keyword2 + "?"
        answer = keyword1
        line = answer + '\t' + question + '\n'

    elif rel == "AtLocation":
        question = "What can you see in " + keyword2 + "?"
        answer = keyword1
        line = answer + '\t' + question + '\n'

    elif rel == "CapableOf":
        question = "What/Who is capable of " + keyword2 + "?"
        answer = keyword1
        line = answer + '\t' + question + '\n'

    elif rel == "Causes":
        question = "What can cause " + keyword2 + "?"
        answer = keyword1
        line = answer + '\t' + question + '\n'

    elif rel == "Desires":
        question = "What/Who will desire " + keyword2 + "?"
        answer = keyword1
        line = answer + '\t' + question + '\n'

    elif rel == "HasSubEvent":
        question = "What has sub event like " + keyword2 + "?"
        answer = keyword1
        line = answer + '\t' + question + '\n'

    # elif rel == "isFilledBy":
    #     # 因为答案范围有点宽泛，可以删掉
    #     print(keyword1)
    #     # question = keyword1.replace('——', 'what') + "?"
    #     question = keyword1
    #     answer = keyword2
    #     line = answer + '\t' + question + '\n'

    elif rel == "MadeUpOf":
        question = "What is made up of " + keyword2 + "?"
        answer = keyword1
        line = answer + '\t' + question + '\n'

    elif rel == "NotDesires":
        question = "What does not desires " + keyword2 + "?"
        answer = keyword1
        line = answer + '\t' + question + '\n'
    else:
        line = ""
    with open(questionpath, 'a', encoding='utf-8') as fw:
        fw.write(line)



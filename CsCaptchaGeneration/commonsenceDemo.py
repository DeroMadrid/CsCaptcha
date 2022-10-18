
import jsonlines

jsonPath = "D:/Desktop/知识图谱数据集/commonsenseQA/test_rand_split.jsonl"
txtPath = "D:/Desktop/知识图谱数据集/commonsenseQA/test.txt"
with open(jsonPath, 'r+',  encoding='utf-8') as fr:
    for item in jsonlines.Reader(fr):
        # print(questionList[i])
        question = item["question"]["stem"]  # 问题文本
        choiceA = item["question"]["choices"][0]["text"]  # 各个选项文本
        choiceB = item["question"]["choices"][1]["text"]
        choiceC = item["question"]["choices"][2]["text"]
        choiceD = item["question"]["choices"][3]["text"]
        choiceE = item["question"]["choices"][4]["text"]
        num = ord(item["answerKey"])-65  # 将ABCDE转换为01234，之后直接选出答案文本
        answerWord = item["question"]["choices"][num]["text"]

        with open(txtPath, 'a', encoding='utf-8') as fw:
            lines = answerWord + '\t' + question + '\n'
            fw.write(lines)

# 数据的每一行的格式, 但是是str：
# {"answerKey": "A",
#  "id": "1afa02df02c908a558b4036e80242fac",
#  "question": {"question_concept": "revolving door",
#               "choices": [{"label": "A", "text": "bank"},
#                           {"label": "B", "text": "library"},
#                           {"label": "C", "text": "department store"},
#                           {"label": "D", "text": "mall"},
#                           {"label": "E", "text": "new york"}],
#               "stem": "A revolving door is convenient for two direction travel, but it also serves as a security measure at a what?"}}

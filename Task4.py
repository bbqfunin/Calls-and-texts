"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""
tui = []
recall = []
sendtexts = []
retexts = []
#建立发送短信列表和接受短信列表
for i in range(len(texts)):
    sendtexts.append(texts[i][0])
    retexts.append(texts[i][1])
#建立接受电话列表和发送电话列表中可能的推销员列表并删重排序
for i in range(len(calls)):
    recall.append(calls[i][1])
    tui.append(calls[i][0])
tui = sorted(list(set(tui)))
#删除以上得到的推销员列表中发送短信，接收短信或者接收电话的号码
for phonecall in tui:
    if (phonecall in recall) or (phonecall in sendtexts) or (phonecall in retexts):
        tui.remove(phonecall)
#逐行输出结果
print("These numbers could be telemarketers: ")
for pcall in tui:
    print(pcall)









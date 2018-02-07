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
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""

#part 1
Bancall = []
code = []
#产生被班加罗尔地区电话拨打的所有电话号码的列表
for i in range(len(calls)):
    if calls[i][0].startswith("(080)"):
        Bancall.append(calls[i][1])
#按照三种电话号码格式抽取上述列表中电话号码的区号或指定前缀
for i in range(len(Bancall)):
    if Bancall[i].startswith("(0"):
        code.append(Bancall[i][Bancall[i].find("(0")+1:Bancall[i].find(")")])
    elif Bancall[i].startswith("140"):
        code.append("140")
    elif (Bancall[i].startswith(("7","8","9"))) and (Bancall[i].find(" ")):
        code.append(Bancall[i][:4])
#去重，排序，规范成列表格式
code = sorted(list(set(code)))
print("Part 1 \nThe numbers called by people in Bangalore have codes:")
#逐行输出
for item in code:
    print(item)

#part 2
n = 0
for i in range(len(Bancall)):
    if Bancall[i].startswith("(080)"):
        n += 1
percent = n / len(Bancall)
percent = format(percent, "0.2%")
print("\nPart 2 \n{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore".format(percent))










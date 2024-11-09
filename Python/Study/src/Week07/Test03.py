# 列表存放某班期末考试成绩等级，
# 请统计出各个等级的人数并按输出排名前三的。
list1=["优秀","良好","及格","良好","不及格","优秀","良好","及格","良好","优秀","良好","及格","良好","优秀","良好","及格","优秀","良好","及格","优秀","良好","及格","不及格","及格"]
dict1 = {}
for i in set(list1):
    dict1[i] = list1.count(i)
# list1 =  [[k,v] for k,v in dict1.items()]

list2 =  sorted(dict1.items(),key=lambda  x:x[1],reverse=True)
print(list2)
print([i[0] for  i in list2][:3])
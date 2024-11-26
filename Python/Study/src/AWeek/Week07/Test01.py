s1 = set("c.biancheng.net")
t1=set("bianchenghello")
# print(s1.issubset(t1))

# 1.s1和t1共同的元素；
print(set(s1) & set(t1))
print(set(s1).intersection(set(t1)))
# 2.s1和t1所有的元素；
print(set(s1) | set(t1))
print(set(s1).union(set(t1)))
# 3.s1有的但t1没有的元素；
print(set(s1) - set(t1))
print(set(s1).difference(set(t1)))
# 4.不同属于s1和t1的元素；
print(set(s1) ^ set(t1))
print(set(s1).symmetric_difference(set(t1)))


list1=[2,5,1,3,2,5,7,4,5,2,1,3,1,5,8,9,7,5,4,5,9,5,2,0,4,7,5]
# 统计列表中不同元素的个数
# 这个需求是统计列表中不同元素有几个，由于列表是允许存在重复元素的，但是集合却不允许存在重复元素，所以可以将list转换为set,然后求长度。
print(len(set(list1)))
# 统计列表中元素出现的次数
print("================")
for i in set(list1):
    print(i,list1.count(i))
# 统计列表中元素个数以及所在列表的位置（拔高思考题）
print("================")
dict1 = {}
for k,v in enumerate(list1):
    if v in dict1:
        print(dict1[v])
        dict1[v].append(k)
        continue
    dict1[v] = [k]
print(dict1)
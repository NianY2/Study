"""
任务描述
文件中包含有2018和2019手机销售榜单数据（市场份额百分数），请根据要求升序输出分析结果：

1.输入'1'时，以列表形式在两行中分别输出2019年和2018年上榜品牌
2.输入'2'时，以列表形式输出2019年和2018年都上榜的品牌
3.输入'3'时，以列表形式输出2019年和2018年上榜的所有品牌
4.输入'4'时，以列表形式输出2019年新上榜品牌
5.输入'5'时，以列表形式输出2019年新上榜和落榜品牌

读取文件可参考代码：

with open('sale2019.csv', 'r', encoding='utf-8') as data2019:
    sale2019 = [[line.strip().split(',')[0], float(line.strip().split(',')[1])] for line in data2019]
示例
输入：
5
# [['华为', 34.3], ['vivo', 18.5], ['OPPO', 18.6], ['小米', 12.3], ['Apple', 8.6], ['魅族', 1.8], ['三星', 1.5], ['联想', 0.8], ['中兴', 0.6]]
输出：
['中兴', '联想', '金立']
"""
# with open('sale2019.csv', 'r', encoding='utf-8') as data2019:
#     sale2019 = [[line.strip().split(',')[0], float(line.strip().split(',')[1])] for line in data2019]
# with open('sale2018.csv', 'r', encoding='utf-8') as data2018:
#     sale2018 = [[line.strip().split(',')[0], float(line.strip().split(',')[1])] for line in data2018]
sale2019 =  [['华为', 34.3], ['vivo', 18.5], ['OPPO', 18.6], ['小米', 12.3], ['Apple', 8.6], ['魅族', 1.8], ['三星', 1.5], ['联想', 0.8], ['中兴', 0.6]]
sale2018 = [['华为', 30.5], ['vivo', 19.1], ['OPPO', 19.5], ['小米', 12.3], ['Apple', 13.5], ['魅族', 2.4], ['三星', 1.5], ['金立', 1.2]]
# 1.输入'1'时，以列表形式在两行中分别输出2019年和2018年上榜品牌
# 2.输入'2'时，以列表形式输出2019年和2018年都上榜的品牌
# 3.输入'3'时，以列表形式输出2019年和2018年上榜的所有品牌
# 4.输入'4'时，以列表形式输出2019年新上榜品牌
# 5.输入'5'时，以列表形式输出2019年新上榜和落榜品牌

num = input()

if num == "1":
    resLs = sorted(sale2018, key=lambda x: x[0])
    resLs2 = sorted(sale2019, key=lambda x: x[0])
    print([i[0] for i in resLs2])
    print([i[0] for i in resLs])


elif num == "2":
    dict1 = {}
    dict2 = {}
    for k,v in enumerate(sale2018):
        dict1[v[0]] = v[1]
    for k,v in enumerate(sale2019):
        if v[0] in dict1:
            dict2[v[0]] = v[1]
    resLs = [[k,v] for k,v in dict2.items()]

    resLs = sorted(resLs,key=lambda x:x[0])
    print([i[0] for i in resLs])
elif num == "3":
    dict1 = {}
    for k,v in enumerate(sale2018):
        dict1[v[0]] = v[1]
    for k,v in enumerate(sale2019):
        dict1[v[0]] = v[1]
    resLs = [[k,v] for k,v in dict1.items()]
    resLs = sorted(resLs,key=lambda x:x[0])
    print([i[0] for i in resLs])
elif num == "4":
    dict2 = {}
    dict1 = {}
    for k,v in enumerate(sale2018):
        dict2[v[0]] = v[1]
    for k,v in enumerate(sale2019):
        if v[0] not in dict2:
            dict1[v[0]] = v[1]
    resLs = [[k,v] for k,v in dict1.items()]
    resLs = sorted(resLs,key=lambda x:x[0])
    print([i[0] for i in resLs])
elif num == "5":
    dict1 = {}
    dict2 = {}
    dict3 = {}
    for k,v in enumerate(sale2018):
        dict1[v[0]] = v[1]
    for k,v in enumerate(sale2019):
        dict2[v[0]] = v[1]
    for k, v in enumerate(sale2019):
        if v[0] not  in dict1:
            dict3[v[0]] = v[1]
    for k, v in enumerate(sale2018):
        if v[0] not  in dict2:
            dict3[v[0]] = v[1]

    resLs = [[k,v] for k,v in dict3.items()]
    resLs = sorted(resLs,key=lambda x:x[0])
    print([i[0] for i in resLs])

# with open('sale2019.csv', 'r', encoding='utf-8') as data2019:sale2019 = [[line.strip().split(',')[0], float(line.strip().split(',')[1])] for line in data2019]
# with open('sale2018.csv', 'r', encoding='utf-8') as data2018:sale2018 = [[line.strip().split(',')[0], float(line.strip().split(',')[1])] for line in data2018]
# brands2019,brands2018,choice = [brand[0] for brand in sale2019],[brand[0] for brand in sale2018],input()
# result = ((sorted(brands2019), sorted(brands2018)) if choice == '1' else sorted(set(brands2019) & set(brands2018)) if choice == '2' else sorted(set(brands2019) | set(brands2018)) if choice == '3' else sorted(set(brands2019) - set(brands2018)) if choice == '4' else sorted(set(brands2019) - set(brands2018)) + sorted(set(brands2018) - set(brands2019)) if choice == '5' else [])
# ((print(result[0]), print(result[1])) if choice == '1' else print(result))
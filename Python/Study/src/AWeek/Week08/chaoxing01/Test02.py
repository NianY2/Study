# 编写一函数，实现输出字典中最大键值所对应的键。
# 例如：字典{'A':1,'B':2,'C':3},那
# 这个字典的键值最大的是3，其对应的键则是“C”，函数要输出“C”

def getDictMaxKeyByValue(dict1:dict)->str:
    ans = (0,-1)
    for k,v in dict1.items():
        if v > ans[1]:
            ans = (k,v)
    return ans[0]

if __name__ == '__main__':
    print(getDictMaxKeyByValue({'A':1,'B':2,'C':3}))
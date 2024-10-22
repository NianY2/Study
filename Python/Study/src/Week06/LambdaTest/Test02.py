"""
根据元素的次数进行升序排序
"""
l=[('高级工程师',25),('中级工程师',20),('无职称',48)]
l2 = sorted(l,key=lambda x:x[1],reverse=False)
print(l2)
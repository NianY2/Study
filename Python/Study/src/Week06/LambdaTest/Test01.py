"""
根据元素平方的大小按升序排序
"""

list1 = [1, 42, 3, -7, 8, 9, -10, 5]
list2 = list(map(lambda x:x*x,list1))
list2.sort(reverse=1)
print(list2)
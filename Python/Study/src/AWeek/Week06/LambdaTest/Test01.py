"""
根据元素平方的大小按升序排序
"""

list1 = [1, 42, 3, -7, 8, 9, -10, 5]
list2 = sorted(list1,key=lambda  x:x**2)
print(list2)
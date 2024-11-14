# 用函数实现，list1=[1,2,5,6,7,9,78],求列表中不能被3整除的数？
from typing import List, Optional


def d(list1: List) -> Optional[int]:
    for i in list1:
        if i % 3 != 0:
            return i

print(d([1, 2, 5, 6, 7, 9, 78]))

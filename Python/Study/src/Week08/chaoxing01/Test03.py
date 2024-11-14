# 编写函数，求两个100以内的随机整数的最小公倍数和最大公约数。
"""
12 18
12的约数有：1, 2, 3, 4, 6, 12
18的约数有：1, 2, 3, 6, 9, 18
共有的约数是：1, 2, 3, 6
最大公约数是6

12的倍数有：12, 24, 36, 48, 60, 72, ...
18的倍数有：18, 36, 54, 72, 90, ...
最小的一个是36

a×b=GCD(a,b)×LCM(a,b)
"""

import  random
def get_gcd(n1:int,n2:int) -> int:
    """
    最大公约数Greatest Common Divisor
    欧几里得算法: 两个整数的最大公约数（GCD）与其中一个整数和这两个数的余数之间的GCD是相同的。
    """
    while n2 != 0:
        t1 = n1
        n1 = n2
        n2 = n2 % t1
    return n1
def get_lcn(n1:int,n2:int) -> int:
    """最小公倍数Least Common Multiple"""
    return int(n1*n2/get_gcd(n1, n2))
def get_gcd_and_lcn(n1:int,n2:int)->tuple[int,int]:
    return get_gcd(n1,n2),get_lcn(n1, n2)

if __name__ == '__main__':
    print(get_gcd(12,18))
    print(get_gcd_and_lcn(12,18))
    print(get_gcd_and_lcn(1, 8))
    num1 =  int(random.random() * 100 + 1)
    num2= int(random.random() * 100 + 1)
    print(num1,num2,get_gcd_and_lcn(num1,num2))
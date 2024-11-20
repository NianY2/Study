# 利用Python中支持默认值参数的特性，修改上一节里定义的幂函数power(x,n)，使其默认计算x的平方。
def power(x:int,n:int=2)->int:
    return  x**n
if __name__ == '__main__':
    print(power(10))
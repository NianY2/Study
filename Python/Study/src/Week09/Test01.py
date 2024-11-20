# 请输入一个数，并判断该数是否是素数

def ifs(num):
    num = int(num)
    if num <= 1:
        print(f"{num}不是素数")
        return  False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            print(f"{num}不是素数")
            return False
    print(f"{num}是素数")
    return  True
ifs(input())

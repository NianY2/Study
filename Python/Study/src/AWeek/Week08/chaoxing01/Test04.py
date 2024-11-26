# 编写程序求1**2 - 2**2 + 3**2 +  4**2 +  ... + 99**2
def test01(num1:int)->int:
    res = 0
    for i in range(1,num1+1):
        if i % 2 != 0:
            res += i**2
        else:
            res -= i**2
    return res
print(test01(99))
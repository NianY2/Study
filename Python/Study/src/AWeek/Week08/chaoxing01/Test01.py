# 1. (简答题) 编写一函数，实现从18位的身份证号码中获取出身年月日，
# 并以类似于“2006年08月12日”的形式输出自己的出生日期。

def getBirthDateByIDCard(idCard:str)->str:
    return f"{idCard[6:10]}年{idCard[10:12]}月{idCard[12:14]}日"

if __name__ == '__main__':
    print(getBirthDateByIDCard("43021219911104635X"))
    print(getBirthDateByIDCard("341525195702263718"))
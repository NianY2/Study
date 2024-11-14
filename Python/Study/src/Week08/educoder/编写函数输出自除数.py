"""
任务描述
一个不含0的数，如果它能被它的每一位除尽，则它是一个自除数。
例如128是一个自除数，因为128能被1、2、8整除。
编写函数selfDivisor(num)判断num是否为自除数，
使用该函数输出不大于N的所有自除数。
（注意，含有数字0的数不是自除数）

输入格式
输入为一行，一个正整数N（N>=1）。

输出格式
输出为一行，是不大于N的所有自除数，每个数后面有一个空格。

示例 1
输入：
1
输出：
1
"""
def selfDivisor(num:int)->int:
    ans = []
    for i in range(num+1):
        if "0" in str(i):
            continue
        flag = True
        for j in str(i):
            if i % int(j) != 0:
                flag = False
                break
        if flag:
            ans.append(str(i))
    return  " ".join(ans)
if __name__ == '__main__':
    print(selfDivisor(int(input())))

"""
任务描述
定义一个函数来判断单词m是否可以由字符串n中出现的字母来组成。
本题保证字符串中出现的字母均为小写字母，且不考虑n中的字母使用次数。
在两行中分别输入两个字符串m,n
如果输入的m包含有除字母外的其他字符，输出ERROR结束程序，否则继续输入字符串n。
如果m,n 满足条件，则输出FOUND，否则输出NOT FOUND

示例 1
输入：
word
world
输出：
FOUND

示例 2
输入：
1a3e
输出：
ERROR

示例 3
输入：
at
bcda
输出：
NOT FOUND
"""
def test(m:str,n:str)->str:
    for i in m:
        if i not in n:
            return "NOT FOUND"
    return "FOUND"
if __name__ == '__main__':
    try:
        print(test(input(),input()))
    except Exception as e:
        print("ERROR")



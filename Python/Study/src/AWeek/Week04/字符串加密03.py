"""
在一行中输入一个包括大小写字母和数字的字符串，
编程将其中字母都转为大写，
然后将大写字母用该字母后的第4个字母替换，
其他字符原样输出，实现字符串加密。
1. 大写字母字符串
2. 大写字母前4个切下来拼接到后面
3. 输入一个字符串input()
4. 字母都转为大写upper()
5. 遍历字符串
    5.1 如果当前字符包含在大写字母的字符串中(find()，得到当前字母在大写字母中的序号)
        a. 将大写字母用该字母后的第4个字母替换拼接(用变换了顺序的字符串中对应序号的字母替换)
    5.2 否则
        b. 其他字符原样拼接
6. 输出变换过的字符串
"""

s = input().upper()
s2 = ""
for i in s:
    if "A" <=  i  <= "Z":
        s2 += chr((ord(i)-ord("A")+4)%ord("Z")+ord("A"))
    else:
        s2+=i
print(s2)


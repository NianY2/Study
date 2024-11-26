"""
任务描述
用户在一行中输入一个包括大小写字母和数字的字符串，编程实现字符串加密。加密规则如下：
将字符串中的大写字母用字母表中该字母后的第5个字母替代
将字符串中的小写字母用字母表中该字母后的第3个字母替代
字符串中的其他字符原样输出
输入格式
输入一个至少包含一个字母的字符串

输出格式
输出加密后的字符串

示例 1
输入：

Life is short, you need Python!
输出：
Qlih lv vkruw, brx qhhg Ubwkrq!

11 -- 1
12 -- 2

"""
s = input()
s2 = ""
for i in s:
    if "a" <= i < "x":
        s2 += chr(ord(i) + 3)
    elif "A" <= i < "V":
        s2 += chr(ord(i) + 5)
    elif "x" <= i <= "z":
        s2 += chr(ord(i) + 3 - 26)
    elif "V" <= i <= "Z":
        s2 += chr(ord(i) + 5 - 26)
    else:
        s2+=i

print(s2)
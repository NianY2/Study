# 用递归方法反转一个字符串，例如“abcde”，反转为“edcba”。
def reverse(s:str)->str:
    if s == "":
        return "";
    return s[len(s)-1]+reverse(s[0:len(s)-1])
print(reverse("abcde"))

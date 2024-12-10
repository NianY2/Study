"""
读百家姓获得姓的列表
赵钱孙李，周吴郑王。 冯陈褚卫，蒋沈韩杨。 ...... 巢关蒯相，查后荆红。 游竺权逯，盖益桓公。 万俟司马，上官欧阳。 夏侯诸葛，闻人东方。 ...... 墨哈谯笪，年爱阳佟。 第五言福
提示： 百家姓前51行为单姓，51行以后为复姓，需要分别处理。
每行读取为字符串，去除换行符、逗号和句号拼接为一个字符串，再用list()转列表，
每个字为一个元素 51行以后拼接为一个字符串，每次取两个字加入列表
"""
def split_by_len(s,l):
    return [s[i:i+l] for i in range(0,len(s),l)]
with open("./第9章 文件操作/百家姓.txt","r",encoding="utf8") as f:
    s = f.read().split("\n")
n = 51
ans = []
s1l = s[:n]
s2l = s[n:]
s1 = "".join(s1l).replace("，","").replace("。","")
s2 = "".join(s2l).replace("，","").replace("。","")
print(split_by_len(s1,1))
print(split_by_len(s2,2))
ans = split_by_len(s1,1)+split_by_len(s2,2)
print(ans)
print(len(ans))
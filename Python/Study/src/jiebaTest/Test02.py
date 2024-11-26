import  jieba
with open("20大报告.txt","r",encoding="utf8") as f:
    s = f.read()
words = jieba.lcut(s)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0)+1
items = list(counts.items())
items = sorted(items,key=lambda x:x[1],reverse=True)
print(items[0:5])
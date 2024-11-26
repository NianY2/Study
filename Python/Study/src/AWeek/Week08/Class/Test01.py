# 统计英文中单词出现的次数并按降序输出
txt0="Twinkle, twinkle, little star, how I wonder what you are.Up above the world so high, like a diamond in the sky.When the blazing sun is gone, when he nothing shines upon.Then you show your little light, Twinkle twinkle all the night."
# print(txt0.split(","))
count = {}
for i in txt0:
    if i in ",.?!~":
        txt0 = txt0.replace(i," ")

for j in txt0.split(" "):
    if j != "":
        count[j] = count.get(j,0)+1

ans = [k for k,v in count.items()]
print(sorted(ans,key=lambda x:count[x],reverse=True))
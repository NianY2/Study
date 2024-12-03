import json

with open("score1034.json","r+",encoding="utf8") as f:
    s = f.read()
l1:list = json.loads(s)
l = [list(i.values()) for i in l1]
l.insert(0,list(l1[0].keys()))
print(l[:int(input())])


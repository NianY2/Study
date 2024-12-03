with open("The Great Learning.txt","r+",encoding="utf8") as f:
    sl = f.read()
line_num = int(input())
s1 = sl.split("\n")
s2 = "\n".join(s1[:line_num])
if line_num < len(s1):
    s2+="\n"
print(len(s2),len(set(s2)))

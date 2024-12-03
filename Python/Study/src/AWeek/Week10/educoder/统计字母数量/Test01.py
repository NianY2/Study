with open("The Old Man and the Sea.txt","r+",encoding="utf8") as f:
    s = f.read()
sl = s.split("\n")
n = int(input())
s = "".join(sl[:n]).lower()
ans = []
for i in range(ord('a'),ord('z')+1):
    ans.append((chr(i), s.count(chr(i))))
ans = sorted(ans,key=lambda x:(x[1],-ord(x[0])),reverse=True)
for i in ans:
    print(f"{i[0]} 的数量是 {i[1]:>3} 个")

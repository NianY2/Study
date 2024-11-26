print(f"{'*':*^100}")
print([x for x in range(10) if x % 2 == 0])
print([x if x > 0 else -x for x in range(-5, 5)])
print([(x, y) for x, y in zip([1, 2, 3], [4, 5, 6])])
# 2.	变量1的取值范围是1~10，变量2的取值范围是1到变量i的，求变量1与变量2的积
print([i*j for i in range(1,11) for j in range(1,i+1) ])
# 3.	设计篮球比赛，小组赛有四支队伍，分主客场，求要比赛多少场，对战情况如何？
l1 =  [(i,j) for  i in "ABCD" for j in "ABCD" if i != j]
print(l1)
print(len(l1))

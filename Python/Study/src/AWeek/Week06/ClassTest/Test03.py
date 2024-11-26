# 2. (简答题) 请设计篮球比赛，小组赛有四支队伍，分主客场，求对战情况如何？（用元组推导式）
t1 =  tuple((i,j)for  i in "ABCD" for j in "ABCD" if i != j)
print(t1)
print(len(t1))

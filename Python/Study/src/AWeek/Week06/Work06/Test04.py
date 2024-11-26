"""
变量i的取值范围是1~10，变量j的取值范围是1到i的，求变量i与变量j的积。
"""
for i in range(1,11):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()

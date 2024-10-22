# 我国古代数学家张丘建在《算经》一书中提出的数学问题：
# 鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。
# 百钱买百鸡，如果要求鸡翁、鸡母、鸡雏都不为零，问鸡翁、鸡母、鸡雏各几何？
# 鸡雏
price = 100
for chicken5 in range(1,price//5+1):
    chicken1 = 0
    chicken3 = 0
    for chicken3 in range(1,(price-chicken5*5)//3+1):
        chicken1 = (price-chicken3*3 - chicken5*5)*3
        if chicken1 != 0 and chicken3 != 0 and chicken5 != 0 and chicken5+chicken3+chicken1 == 100:
            print(chicken5,chicken3,chicken1)
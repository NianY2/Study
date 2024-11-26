# 我国古代数学家张丘建在《算经》一书中提出的数学问题：
# 鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。
# 百钱买百鸡，如果要求鸡翁、鸡母、鸡雏都不为零，问鸡翁、鸡母、鸡雏各几何？
# 鸡雏
# cock + hen + chicken == 100
# cock * 5 + hen * 3 + chicken // 3 = 100
# cock * 15 + hen * 9 + chicken  = 300
# cock * 15 + hen * 9 + (100 - cock - hen)  = 300
# cock * 14 + hen * 8 + 100 = 300
# hen = (300 - cock * 14) // 8
# hen = 25 - cock * 7 // 4
# 因hen 为正整数，所以cock 必为4的倍数，
# 且最大值不超过12（cock = 16时，hen 为负值了）
# cock 取值只能为4，8，12
for cock in range(4,13,4):
    hen = 25 - cock * 7 // 4
    chicken = 100 - cock - hen
    print(cock, hen, chicken)
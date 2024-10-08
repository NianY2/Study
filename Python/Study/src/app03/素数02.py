# num = int(input())
# for i in range(2,num):
#     if num % i == 0:
#         print("不是")
#         break
# # 当 for 循环被 break 中断后，其后的 else 语句就不执行了
# else:
#     print("是")
num = 0
max_num = 0
while num < 50:
    i = 2
    while i < num:
        if num % i == 0:
            break
        i+=1
    else:
        max_num = max(max_num,num)
    num+=1
print(max_num)

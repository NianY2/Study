num = int(input())
for i in range(2,num):
    if num % i == 0:
        print(f"不是{i},{num/i}")
        break
# 当 for 循环被 break 中断后，其后的 else 语句就不执行了
else:
    print("是")
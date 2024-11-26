num = 0
max_num = 0
num2 =  int(input())
while num <= num2:
    i = 2
    while i < num:
        if num % i == 0:
            break
        i+=1
    else:
        max_num = max(max_num,num)
    num+=1
print(max_num)

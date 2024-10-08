import random
num = random.randint(1,1024)
print(num)
for i in range(5,0,-1):
    num2 = int(input("Please enter："))
    if num == num2:
        print("yes")
        break
    elif num2 > num:
        print("It's big")
    elif num2 < num:
        print("It's small")
else:
    print("Game over")

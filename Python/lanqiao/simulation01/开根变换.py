import math


def test(n):
    res = 0
    while n != 1:
        n = int(math.sqrt(n))
        res += 1
    return  res
if __name__ == '__main__':
    print(test(2024))
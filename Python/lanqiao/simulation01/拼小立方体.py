"""
小蓝有很多 1x1x1 的小立方体，他可以使用多个立方体拼成更大的立方体。
例如，小蓝可以使用 8 个小立方体拼成一个大立方体，每边都是 2 个。
又如，小蓝可以使用 27 个小立方体拼成一个大立方体，每边都是 3 个。
现在，小蓝有 2024 个小立方体，他想再购买一些小立方体，用于拼一个超大的立方体，
要求所有的小立方体都用上，拼成的大立方体每边长度都相等。
请问，小蓝最少需要购买多少个小立方体？
"""



def test(n):
    num = int(pow(n,1/3))+1
    return  num**3 - 2024
if __name__ == '__main__':
    print(test(2024))
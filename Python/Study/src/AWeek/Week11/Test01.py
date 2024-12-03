"""
1. 简单的计算器
编写程序，请设计一个简单的计算器类，可以进行加法、减法、乘法、除法、整除、幂运算。（用pycharm完成）
①分两行接收输入的两个数；
②接收输入的运算符，进行响应的运算
③输出完整的运算过程和结果。
"""
class Calculator:

    @staticmethod
    def add(num1,num2):
        return  num1+num2

    @staticmethod
    def sub( num1, num2):
        return num1 - num2

    @staticmethod
    def mul( num1, num2):
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        try:
            return num1 / num2
        except Exception:
            print("除数为0")

    @staticmethod
    def m(num1, num2):
        return num1 ** num2

    @staticmethod
    def swich(a,b,s):
        m = {
            "+":Calculator.add,
            "-": Calculator.sub,
            "*": Calculator.mul,
            "/": Calculator.divide,
            "**": Calculator.m,
        }
        return  m[s](a,b)

if __name__ == '__main__':
    print(Calculator.swich(int(input()),int(input()),input()))
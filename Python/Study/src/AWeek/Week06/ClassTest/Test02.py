# 使用元组创建一个存储python关键字的对象，并检测给定的单词是否是python关键字。

tuple1 = ("False","True","None") # ....
def is_keyword(str1:str):
    return  str1 in tuple1
if __name__ == '__main__':
    print(is_keyword("False"))
    print(is_keyword("SSS"))

"""
任务描述
微软产品一般都一个25位的序列号，是用来区分每份微软产品的产品序列号。
产品序列号由五组被“-”分隔开，由字母数字混合编制的字符串组成，
每组字符串是由五个字符串组成。如： 36XJE-86JVF-MTY62-7Q97Q-6BWJ2

序列号中每个字符是取自于以下24个字母及数字之中的一个： B C E F G H J K M P Q R T V W X Y 2 3 4 6 7 8 9 。
采用这24个字符的原因是为了避免混淆相似的字母和数字，如I 和1，O 和0等，避免产生不必要的麻烦。

请编写程序，根据用户输入的个数和随机数种子，随机生成相应个数的序列号并输出。

随机数种子函数语法为：
random.seed(n)

本题要求应用random.choice()方法每次获得一个随机字符！！！

输入格式
分两行中依次输入：
第一行输入一个正整数，代表要生成的序列号的个数
第二行输入一个正整数，代表随机数种子

输出格式
分行依次输出指定个数的序列号

示例
输入：

2
10

输出：

3CVX3-BJWXM-6HCYX-QEK9R-CVG4R
TVP7M-WH7P7-RGWKW-4TC3B-KGJP2
"""
import  random
num = int(input())
random1 = random.Random()
random1.seed(int(input()))
for j in range(num):
    for i in range(1,26):
        s =  random1.choice(["B", "C", "E", "F", "G", "H", "J", "K", "M", "P", "Q", "R", "T", "V", "W", "X", "Y", 2, 3, 4, 6, 7, 8, 9])
        print(s,end="")
        if i % 5 == 0 and i != 25:
            print("-",end="")
    print()

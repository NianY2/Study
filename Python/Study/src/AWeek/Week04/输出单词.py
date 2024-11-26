"""
任务描述
输入一个英文句子，每个单词间用空格分隔，
标点符号前面无空格，后面跟一个空格。
请按出现顺序将每个单词分行输出（标点符号归属于前面的单词）。

输入格式
一个英文句子

输出格式
分行依次输出句子中的单词

示例
输入：
Never forget to say "thanks".
输出：
Never
forget
to
say
"thanks".
"""
s = input()
for i in s:
    if i == " ":
        print()
    else:
        print(i,end="")
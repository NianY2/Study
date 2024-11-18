"""
符统计
问题描述
给定一个只包含大写字母的字符串S，请你输出其中出现次数最多的字符。
如果有多个字母均出现了最多次, 按字母表顺序依次输出所有这些字母。

输入格式
一个只包含大写字母的字等串S

输出格式
若干个大写字母，代表答案。
样例输入
BABBACAC
样例输出
AB
"""
from collections import Counter


def test(S):
    cnt = {}
    for i in S:
        cnt[i] = cnt.get(i,0) + 1
    mx = max(cnt.values())

    ans = [c for c in cnt if cnt[c] == mx]
    ans.sort()
    return "".join(ans)




if __name__ == '__main__':
    # print(test(input()))
    print(test("BABBACAC"))


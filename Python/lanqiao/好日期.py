"""
如果一个日期的日期以 1 结尾（1日、11日、21日、31日）且为星期一，则称这个日期为一好日期。
请问从 1901 年 1 月 1 日至 2024 年 12 月 31 日总共有多少个一好日期。
提示：1901 年 1 月 1 日是星期二。
"""
def if_run(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return  True
    return False
def getDays(year,month):
    day30 = [4,6,9,11]
    if month in day30:
        return 30
    elif month == 2:
        if if_run(year):
            return 29
        return  28
    else:
        return  31


def test(year1,year2):
    res  = 0
    week = 2
    for year  in range(year1,year2):
        for month in range(1,13):
            days = getDays(year,month)
            for day in range(1,days+1):
                if str(day)[-1] == "1" and week == 1:
                    res += 1
                week%=7
                week+=1
    return  res
if __name__ == '__main__':
    print(test(1901,2024))

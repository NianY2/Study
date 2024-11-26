def is_leap(year):
    """参数为表示年份的整数，判断该年份是否为闰年，
    返回布尔值，即闰年返回True，非闰年返回False
    """
    # 补充你的代码
    year = int(year)
    if year % 400 == 0 or (year %  4==0 and year % 100  != 0):
        return  True
    return False


def days_of_month(date_str):
    """根据输入的表示年月日的字符串，返回其中月份的天数"""
    month = int(date_str[4:6])
    if month in [4,6,9,11]:
        return 30
    elif month == 2:
        if is_leap(date_str[0:4]):
            return  29
        else:
            return  28
    else:
        return  31


if __name__ == '__main__':
    # date_in = input()  # 输入一个年月日
    # print(days_of_month(date_in))
    print(days_of_month("20000219"))
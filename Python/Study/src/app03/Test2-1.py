def income_tax():
    """用户输入应发工资薪金所得、五险一金金额和个税免征额，输出应缴税款和实发工资，
    结果保留小数点后两位。当输入数字小于0 或等于0 时，输出“error”。
    实发工资 = 应发工资 - 五险一金 - 个人所得税
    建议使用以下变量名：
    salary：每月应发工资薪金
    insurance_fund：五险一金
    exemption：个税免征额
    educted_amount：速算扣除数
    测试用例
    输入（冒号前是提示性文字，冒号后的数字为用户输入）
    请输入应发工资薪金金额：16000
    请输入五险一金金额：4000
    请输入个税免征额：5000
    输出
    应缴税款490.00 元，实发工资11510.00 元。
    """
    # ====================Begin===================================
    list1 = (
        (0,3,0),
        (3000, 10, 210),
        (12000, 20, 1410),
        (25000, 25, 2660),
        (35000, 30, 4410),
        (55000, 35, 7160),
        (80000, 45, 15160),
    )
    salary = float(input())
    insurance_fund = float(input())
    exemption = float(input())

    if salary <= 0 or insurance_fund <= 0 or exemption <= 0:
        print("error")
        return
    num = salary - insurance_fund - exemption
    yjns = 0
    for i in list1[::-1]:
        if num >  i[0]:
            yjns =  num * i[1] / 100 - i[2]
            break

    print(f"应缴税款{yjns:.2f}元，实发工资{(salary-insurance_fund-yjns):.2f}元。")
    # 应纳税额 = (工资薪金所得 - 五险一金 - 个税免征额) × 适用税率 - 速算扣除数
    # 实发工资 = 应发工资 - 五险一金 - 应缴税款
    # ======================End=================================


if __name__ == '__main__':
    income_tax()  # 调用函数完成计算和输出

#读CSV文件
# with open('score.csv', 'r', encoding='utf-8') as csv_obj:
#     data_lst = []
#     for line in csv_obj:
#         data_lst.append(line.strip().split(','))
# print(data_lst)

#读CSV文件,创建函数
# def read_csv(filename):
#     """接收csv格式文件名为参数，根据逗号将每行切分为一个列表。
#     每行数据做为二维列表的一个元素，返回二维列表。
#     """
#     with open(filename, 'r', encoding='utf-8') as csv_obj:
#         data_lst = [line.strip().split(',')
#         for line in csv_obj]
#         return data_lst
# if __name__ == '__main__':
#      file = 'score.csv'  # 定义文件名变量，方便程序扩展和修改
#      data = read_csv(file)   # 读文件转为二维列表
#      print(data)             # 输出列表

#2.写CSV文件
# def write_file(ls, new_file):
#     """接收一个二维列表和一个表示文件名的字符串为参数，
#      将二维列表中的列表元素中的数据拼接在一起写入文件中，
#      每写入一组数据加一个换行符。"""
#     with open(new_file, 'w', encoding='utf-8') as file:  # 写模式
#          for x in ls:
#             file.writelines(','.join(x) + '\n')
#
# if __name__ == '__main__':
#     data = [['姓名', '学号', '高数', '英语', 'python', '物理', 'java', 'C语言'],
#             ['罗明', '1217106', '95', '85', '96', '88', '78', '90'],
#             ['金川', '1217116', '85', '86', '90', '70', '88', '85']]
#     file ='score_new.csv'
#     write_file(data, file)

#读文件统计成绩
#1.读取并显示文件内容,方法1：
# def read_csv(filename):
#     """接收csv格式文件名为参数，根据逗号将每行切分为一个列表。
#     每行数据做为二维列表的一个元素，返回二维列表。
#     """
#     data_lst = []
#     with open(filename, 'r', encoding='utf-8') as csv_obj:
#         for line in csv_obj:
#             data_lst.append(line.strip().split(','))
#     return data_lst
#
# if __name__ == '__main__':
#     file = 'score.csv'  # 定义文件名变量
#     data = read_csv(file)   # 读文件转为二维列表
#     print(data)             # 输出列表

#读取并显示文件内容，用推导式实现，方法2
# def read_csv(filename):
#     """接收csv格式文件名为参数，根据逗号将每行切分为一个列表。
#     每行数据做为二维列表的一个元素，返回二维列表。
#     """
#     with open(filename, 'r', encoding='utf-8') as csv_obj:
#         data_lst = [line.strip().split(',') for line in csv_obj]
#     return data_lst
# if __name__ == '__main__':
#     file = 'score.csv'  # 定义文件名变量
#     data = read_csv(file)   # 读文件转为二维列表
#     print(data)             # 输出列表

#2.计算每位同学的总分附加到课程成绩后面，并写入到score.csv文件中
# def total(ls):
#     """接收读文件获得的二维列表为参数，计算并输出每位同学总分。"""
#     total_score = []                 # 创建空列表
#     ls[0].append('总分')    # 先为标题行末尾增加一个元素'总分'
#     for x in ls[1:]:                 # 遍历非标题行
#         # 对成绩部分汇总，转为元素为字符串的列表后加到x上
#         total_score.append(x + [str(sum(map(int, x[2:])))])
#     return [ls[0]] + total_score      # 返回列表
#
# def write_file(ls, new_file):
#     """接收一个二维列表和一个表示文件名的字符串为参数，
#      将二维列表中的列表元素中的数据拼接在一起写入文件中，
#      每写入一组数据加一个换行符。"""
#     with open(new_file, 'w', encoding='utf-8') as file:  # 写模式
#          for x in ls:
#             file.writelines(','.join(x) + '\n')
#
# if __name__ == '__main__':
#     file = 'score.csv'  # 定义文件名变量
#     with open(file, 'r', encoding='utf-8') as csv_obj:
#         data_lst = [line.strip().split(',') for line in csv_obj]
#         data =total(data_lst)   # 读文件转为二维列表
#     # print(data)
#     score_new='score_new.csv'
#     write_file(data,score_new)

#3.根据每名同学的各科成绩进行降序排序，考虑到标题行不能参与排序，需先将其切除，对剩余部分进行排序
# def sort_list(ls, n):
#     """接受列表和表示字段序号的整数n为参数，根据第 n 列值对二维列表降序排序。"""
#     ls_title = [ls[0]] # 序号0的元素是标题，标题不参与排序
#     ls_score = ls[2:] # 序号2以后的是成绩数据，将成绩数据切分出来
#     ls_score.sort(key=lambda x: int(x[n]), reverse=True)  # 按整数降序
#     return ls_title + ls_score
#
# if __name__ == '__main__':
#     file = 'score.csv'  # 定义文件名变量
#     with open(file, 'r', encoding='utf-8') as csv_obj:
#         num=int(input())
#         data_lst = [line.strip().split(',') for line in csv_obj]
#         data =sort_list(data_lst,num)   # 读文件转为二维列表
#     print(data)

#用pandas库读写文件
# import pandas as pd                  # 导入pandas库起别名为pd
# score = pd.read_csv('score.csv') # 读文件中的数据dataframe对象中
# scoreSum = [sum(x[1:]) for x in score.values.tolist()]  # 计算总分
# print(scoreSum)                      # 查看计算的总分
# score['总分'] = scoreSum              # 在数据最后加上score一列
# score = score.sort_values(by=['总分'], ascending=False)  # 总分降序排序
# score.to_csv('scoreSum.csv', index=False)            # 写回到文件，

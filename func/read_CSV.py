import os
import csv


def read(filename):
    # 使用相对路径  __file__是Pyth的内置函数，表示当前代码文件
    # os表示操作系统，path表示操作系统中的路径
    # dirname表示当前的路径，不包含文件名
    base_path = os.path.dirname(__file__)
    # replace替换路径，把字符串中的 old（旧字符串） 替换成 new(新字符串)，
    path = base_path.replace('func','data/'+filename)
    print(path)
    list=[]
    with open(r'%s'%path, encoding='UTF-8') as content:
        data = csv.reader(content)
        print('1111111111111111111111')
        print(data)
        for row in data:
            # if row:
            list.append(row)
                # print(row)

    # 测试数据不包含第一行表头
    return list[1:]


if __name__ == '__main__':
    # pass
    list = read('geren-xingbie.csv')
    print(list)


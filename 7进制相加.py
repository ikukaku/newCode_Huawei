# -*- encoding: utf-8 -*-
"""
@File    : 7进制相加.py
@Time    : 2019-11-03 21:47
@Author  : ikukaku
@Email   : 1073258077@qq.com
"""


def str_to_int(str_1, old_format, new_format):

    new_format = int(new_format)
    result = []
    ten_format = int(str_1, int(old_format))
    while True:
        b = ten_format / new_format
        c = ten_format % new_format
        result.append(c)
        if b == 0:
            break
        ten_format = b
    result.reverse()
    result_str = ""
    for i in result:
        result_str = result_str + str(i)
    return result_str


N = raw_input()
N_list = N.split(" ")
N1 = int(N_list[0],7)
N2 = int(N_list[1],7)
total = N1+N2
print str_to_int(str(total), "10", "7")


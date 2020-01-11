# -*- coding: utf-8 -*-


def str_to_int(str_1, old_format, new_format):
    '''
    进制转换
    :param str_1:  待转换字符串
    :param old_format: 旧进制
    :param new_format: 新进制
    :return: 转换后的字符串
    '''

    new_format = int(new_format)
    result = []
    ten_format = int(str_1, old_format)
    while True:
        b = ten_format / new_format  # 商
        c = ten_format % new_format  # 余数
        result.append(c)
        if b == 0:
            break
        ten_format = b
    result.reverse()
    result_str = ""
    for i in result:
        result_str = result_str + str(i)
    return result_str

print(str_to_int("10",7, 16))
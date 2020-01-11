# -*- encoding: utf-8 -*-
"""
@File    : 求int型正整数在内存中存储时1的个数.py
@Time    : 2019-11-03 19:24
@Author  : ikukaku
@Email   : 1073258077@qq.com

题目描述
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。

输入描述:
 输入一个整数（int类型）

输出描述:
 这个数转换成2进制后，输出1的个数

示例1
输入
5

输出
2
"""

while True:
    try:
        zzz = int(raw_input())
        bin_str = str(bin(zzz))
        max_1 = 0
        for i in range(len(bin_str)):
            if bin_str[i] == "1":
                max_1 = max_1 + 1
        print max_1
    except:
        break
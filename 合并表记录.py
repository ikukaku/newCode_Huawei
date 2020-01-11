# -*- encoding: utf-8 -*-
"""
@File    : 合并表记录.py
@Time    : 2019-11-03 18:58
@Author  : ikukaku
@Email   : 1073258077@qq.com

题目描述
数据表记录包含表索引和数值（int范围的整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开

输出描述:
输出合并后的键值对（多行）

示例1
输入
4
0 1
0 2
1 2
3 4

输出
0 3
1 2
3 4
"""

N = int(raw_input())
input_raw = {}
for i in xrange(N):
    x = raw_input()
    _a = int(x.split(' ')[0])
    _b = int(x.split(' ')[-1])
    if input_raw.has_key(_a):
        input_raw[_a] = input_raw[_a]+_b
    else:
        input_raw.setdefault(_a, _b)
for i in sorted(input_raw.keys()):
    print str(i)+' '+str(input_raw[i])
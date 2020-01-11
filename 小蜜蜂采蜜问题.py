# -*- encoding: utf-8 -*-
"""
@File    : 小蜜蜂采蜜问题.py
@Time    : 2019-11-03 10:29
@Author  : ikukaku
@Email   : 1073258077@qq.com

练习题:

蜂巢在坐标（0,0）的位置，有五处花丛，蜜蜂从蜂巢出发，要把五处花丛的花蜜采完再回到蜂巢，最短距离是多少。
输入说明：一行输入，10个数分别是五处花丛的坐标（x1,y1,x2,y2,x3,y3,x4,y4,x5,y5）
"""

import itertools

# 对所有节点进行全排列，根据全排列的结果来进行计算最短路径
nums=[1,2,3,4,5]
print list(itertools.permutations(nums))
print list(itertools.combinations(nums,3))




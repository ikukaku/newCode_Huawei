# -*- encoding: utf-8 -*-
"""
@File    : 将真分数分解为埃及分数.py
@Time    : 2019-11-03 17:06
@Author  : ikukaku
@Email   : 1073258077@qq.com

题目描述
分子为1的分数称为埃及分数。现输入一个真分数(分子比分母小的分数，叫做真分数)，请将该分数分解为埃及分数。如：8/11 = 1/2+1/5+1/55+1/110。

输入描述:
输入一个真分数，String型

输出描述:
输出分解后的string

示例1
输入
8/11

输出
1/2+1/5+1/55+1/110
"""

result_int = []
def chuli(a, b):
    if a == 1:
        result_int.append(b)
    else:
        shang = b/a
        yushu = b%a
        result = shang+1
        b = b*result
        a = a-yushu
        result_int.append(result)

        n = int(a)
        m = int(b)
        for i in range(2, n):
            while (n % i == 0 and m % i == 0):
                n = n // i
                m = m // i
        chuli(n,m)

a ,b = raw_input().strip().split("/")
chuli(int(a),int(b))


hah = ""
for i in result_int:
    hah = hah+ "1/"+str(i) + "+"
print hah[:-1]

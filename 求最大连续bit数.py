# -*- encoding: utf-8 -*-
"""
@File    : 求最大连续bit数.py
@Time    : 2019-11-03 18:25
@Author  : ikukaku
@Email   : 1073258077@qq.com

题目描述
功能: 求一个byte数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1

输入: 一个byte型的数字

输出: 无

返回: 对应的二进制数字中1的最大连续数
输入描述:
输入一个byte数字

输出描述:
输出转成二进制之后连续1的个数

示例1
输入
3

输出
2


int(x [,base ])         将x转换为一个整数
long(x [,base ])        将x转换为一个长整数
float(x )               将x转换到一个浮点数
complex(real [,imag ])  创建一个复数
str(x )                 将对象 x 转换为字符串
repr(x )                将对象 x 转换为表达式字符串
eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s )               将序列 s 转换为一个元组
list(s )                将序列 s 转换为一个列表
chr(x )                 将一个整数转换为一个字符
unichr(x )              将一个整数转换为Unicode字符
ord(x )                 将一个字符转换为它的整数值
hex(x )                 将一个整数转换为一个十六进制字符串
oct(x )                 将一个整数转换为一个八进制字符串


dec = input('10进制数为：')
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))

string1 = '101010'
print('二进制字符串转换成十进制数为：'，int(string1,2))
string1 = '367'
print('八进制字符串转换成十进制数为：'，int(string1,8))
string3 = 'FFF'
print('十六进制字符串转换成十进制数为：'，int(string1,16))
"""
while True:
    try:
        zzz = int(raw_input())
        bin_str = str(bin(zzz))
        max_1 = 0
        temp_le = 0
        for i in range(len(bin_str)):
            if bin_str[i] == "1":
                temp_le = temp_le + 1
                max_1 = max(max_1, temp_le)
            else:
                max_1 = max(max_1, temp_le)
                temp_le = 0

        print max_1
    except:
        break




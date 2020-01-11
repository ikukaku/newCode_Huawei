# -*- encoding: utf-8 -*-
"""
@File    : 最长回文字串.py
@Time    : 2019-11-02 23:15
@Author  : ikukaku
@Email   : 1073258077@qq.com
"""
'''
题目描述
Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，
但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。
比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。
因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），
Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？
'''


def find_max_length(input_str):
    str_length = len(input_str)
    max_length = str_length
    # 最长子串是原始字符串
    if input_str[::-1] == input_str:
        return max_length

    for i in range(max_length-1, 1, -1):
        round_time = str_length-i+1
        for j in range(round_time):
            temp = input_str[j:j+i]
            if temp[::-1]==temp:
                return i
    return 1


ori = raw_input()
print find_max_length(ori)

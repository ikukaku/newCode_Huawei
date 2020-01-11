# -*- coding: utf-8 -*-
def is_sushu(n):
    '''
    判断是否是素数
    :param n:
    :return:
    '''
    help = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if n in help:
        return True
    if n % 2 == 0:
        return False
    time = int(n ** 0.5) + 1
    for i in xrange(3, time, 2):
        if n % i == 0:
            return False
    else:
        return True


def Factorization(n):
    '''
    分解质因数-非递归
    :param n:
    :return:
    '''
    if is_sushu(n):
        return [str(n)]
    result = []
    for i in range(2, n):
        if is_sushu(i):
            while n % i == 0:
                result.append(str(i))
                n = n / i
                if is_sushu(n):
                    result.append(str(n))
                    return result



def Factorization2(n):
    '''
    分解质因数-递归
    :param n:
    :return:
    '''
    if is_sushu(n):
        return [str(n)]
    result = []
    for i in range(2, n):
        if is_sushu(i):
            if n % i == 0:
                result.append(str(i))
                result_new = Factorization2(n/i)
                return result + result_new


print " ".join(Factorization(int(raw_input())))+" "

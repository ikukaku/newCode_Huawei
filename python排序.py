# -*- encoding: utf-8 -*-
"""
@File    : python排序.py
@Time    : 2019-11-03 19:01
@Author  : ikukaku
@Email   : 1073258077@qq.com


1、sort()
函数 （只对list有用）

sort(...)

　　L.sort(key=None, reverse=False)

　　key = 函数
这个函数会从每个元素中提取一个用于比较的关键字。默认是None

　　reverse = True / False(默认是False升序；True：降序)

　　作用：对原序列进行排序，也就是直接在原序列上操作，没有返回值

sorted()
函数

　　sorted(iterable, key=None, reverse=False)

　　iterable：是可迭代的对象

　　key：函数，这个函数会从每个元素中提取一个用于比较的关键字；默认是None

　　正确的写法是：key = func
函数名称不写括号
"""

#例子1：按元素的长度进行排序

a = [(1,), (1, 1), (1, 2, 3), (2, 4)]


def func(b):
    return len(b)


print(sorted(a, key=func, reverse=True))

# 执行返回：[(1, 2, 3), (1, 1), (2, 4), (1,)]


# ----------------------
# 例子2：有一个数组，第一列是员工ID，第二列是姓名，第三列是工资，请按工资的降序进行排序

l = [[1, 'tom', 3000], [2, 'com', 4000], [3, 'aom', 1500]]

print(sorted(l, key=lambda x: x[2]))
# 执行返回：[[3, 'aom', 1500], [1, 'tom', 3000], [2, 'com', 4000]]


# -----------------------
# 例子3：对list里面嵌套的字典，按照age进行升序排序

alist = [{"name": "a", "age": 20}, {"name": "b", "age": 30}, {"name": "c", "age": 25}]
print(sorted(alist, key=lambda x: x['age']))
# 执行返回：[{'name': 'a', 'age': 20}, {'name': 'c', 'age': 25}, {'name': 'b', 'age': 30}]
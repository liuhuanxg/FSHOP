# -*-coding:utf-8 -*-
"""
@project:QSHOP
@File: demo1.py
@Time: 2019/11/23 10:37
@user：python-刘欢    
"""
import json

# dumps
# 将python数据类型转化为json字符串。
# 字典 ——>object
# 列表——>array

# loads   将json串转化为python数据类型
'''
dict1 = {'name':'zhangsan'}
print(dict1,type(dict1))

json_dict = json.dumps(dict1)    #json数据类型的key和value必须同时都是双引号。
print(json_dict,type(json_dict))

dict2 = json.loads(json_dict)
print(type(dict2),dict2)
'''

# 装饰器：最初是用来在不修改源代码的基础上增加新的功能，后来延伸出更多的用法：身份校验机制，将一些共同的功能块通过装饰器实现,本质是一个闭包函数。
# 由三部分函数组成
# 1、被装饰的函数
# 2、装饰器外层函数，返回值是内层函数的地址
# 3、装饰器内层函数，返回值是被装饰函数的返回值


# 1、不带参数的装饰器
'''
def wraper(func):
    def inner():
        print(22222)
        func()
        print(33333)
    return inner

@wraper
def func():
    print(1111111)

# print(wraper(func))
# wraper(func)()
func()
'''

# 2、带单个参数的装饰器
'''
def wraper(func):
    def inner(number):
        print(22222,number)
        func(number)
        print(33333)
    return inner

@wraper
def func(numer):
    print(1111111)

# print(wraper(func))
# # wraper(func)  #相当于内层的inner函数
# wraper(func)(5)
func(5)
'''

# 3、带不确定参数的装饰器，通过*args和**kwargs接收参数
'''
def wraper(func):
    def inner(number,*args,**kwargs):
        print("number：",number)
        print("args：",args)
        print("kwargs：",kwargs)
        func(number,*args,**kwargs)
        print(33333)
    return inner

@wraper
def func(numer,*args,**kwargs):
    print(1111111)

# print(wraper(func))
# # wraper(func)  #相当于内层的inner函数
# wraper(func)(5)
func(5,1,name='张三')
func(5,1,2,3,name='张三',age=20)
'''

# 4、*args和**kwargs的用法
'''
def wraper(func):
    def inner(number,*args,**kwargs):
        print("number：",number)
        print("args1：",args)   #元组格式的数据(1,2,3)
        print("args2：",*args)  #单个数据格式1   2   3
        print(1,2,3)
        # **{'name':'zhangsan'}   ==>   name='张三'
        print("kwargs：",kwargs)
        # print("kwargs：",**kwargs)  #报错
        # print(name='张三',age=20)   #报错
        func(number,*args,**kwargs)
        print(33333)
    return inner

@wraper
def func(numer,*args,**kwargs):
    print(1111111)

# func(5,1,name='张三')
func(5,1,2,3,name='张三',age=20)
'''

# 5、带返回值的装饰器
"""
def wraper(func):
    def inner(number,*args,**kwargs):
        print(1,2,3)
        return func(number,*args,**kwargs)
    return inner

@wraper
def func(numer,*args,**kwargs):
    print(1111111)
    return '被装饰的函数'
print(func(5,1,name='zhangsan'))
"""

'''
import re

str1 = "abbbbbcccc"
pattern = re.compile('b+')
print(pattern.sub('b',str1))
'''
"""
import time
for i in range(20):
    print(''.join(str(time.time()).split('.')))
"""


def wraper1(func):
    print(11111111111)

    def inner():
        print(22222222)
        func()
        print(333333333)

    return inner


def wraper2(func):
    print(444444444444444)

    def inner():
        print(555555555555555)
        func()
        print(666666666666)

    return inner


def wraper3(func):
    print(7777777777777)

    def inner():
        print(888888888888)
        func()
        print(999999999999)

    return inner


def func():
    print(1010101010101010)


# func()


import time
print(time.time())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : test01.py
@Author: zhao
@Date  : 2025/4/2 19:14
@Desc  :  
@Exp   : 
'''

#测试内容
class A:
    def __init__(self,name):
        self.name=name

class B(A):
    pass

if __name__=="__main__":
    print("~"*30)
    a=A("zhao")
    print(a.name)
    print("~" * 30)

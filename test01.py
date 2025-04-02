#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : test01.py
@Author: zhao
@Date  : 2025/4/2 19:14
@Desc  :  
@Exp   : 
'''

#写一个单例模式
class D_l:
    __T=None
    def __new__(cls,*args):
        if not cls.__T:
           cls.__T=super().__new__(cls)
        return cls.__T


if __name__=="__main__":
    print("~"*30)
    a=D_l()
    a.name="zhao"
    print(a.name)
    print("~" * 30)
    c=D_l()
    print(c.name)

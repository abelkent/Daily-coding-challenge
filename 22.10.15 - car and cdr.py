# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:34:51 2022

@author: abelw
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair



test = cons(1,2)
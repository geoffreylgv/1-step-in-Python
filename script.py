#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
Python pour les debutant
Python pour debuter les algorithmes
"""
# file: script.py
# author: geoffreylgv
# date: december, 12 2020
#updated at : __

print("\t======================Starting small=================\n
\t*******************************Python algorithmique*****************************\n")

"""
factorial ==> return the factorial of
"""
def factorial(n):
    if n > 0:
         return n*factorial(n-1)
    else:
        return 1

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
\t*******************************Python algorithmique****************************\n")

"""
factorial ==> return the factorial of
"""
def factorial(n):
    if n > 0:
         return n*factorial(n-1)
    else:
        return 1

"""
is_palindrome ===> return true if is palindrome , else false
"""
def is_palindrome(word):
    # FIXME
    return word == word[::-1]
    result = is_palindrome(word)
 
    if result:
        print("True")
    else:
        print("False")
word_0 = "omo"
word_1 = "marvelcomicsunivers"
word_2 = "cic"
is_palindrome(word_2)
print("All clear !! Go to next")
"""
second palindrome ~input number~
"""
is_palindrome_number(number)
reverse_local = 0  
tmp = number
while(num > 0):  
    numeric_local = num % 10  
    reverse_local = reverse_local * 10 + numeric_local  
    number = number // 10  
if(tmp == reverse_local):  
    print("True : palindrome number")  
else:  
    print("False : not palindrome number")  
#end palindrome

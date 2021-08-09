# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:42:15 2018

@author: aicha
"""

from fractions import *
def Farey(a,b):
    n=a.numerator+b.numerator
    d=a.denominator+b.denominator
    return Fraction(n,d)


a=Fraction(3,4)
b=Fraction(1,13)
print(Farey(a,b))
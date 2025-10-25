'''
Created on Oct 24, 2025

@author: rharidas
'''
from inspect import Arguments
from mako.parsetree import Expression
"""
Lamda is anonymous functin and has no name It can take only one expression but any numer of Arguments
and it returns the expression
lamda arguments:Expression
"""
x=lambda a:a+10
print(x(5))

x=lambda a,b:a*b
print(x(6,5))

x=lambda a,b,c:a+b+c
print(x(6,5,1))
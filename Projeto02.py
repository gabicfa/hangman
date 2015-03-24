# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:17:19 2015

@author: gabialmeida
"""

d = open("palavras.txt", encoding="utf-8")
c= d.readlines()
lista = list()

for i in c:
    p= i.strip()
    if p != "":
        lista.append(p)

from random import choice
e =choice(lista)
print(e)
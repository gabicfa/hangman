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
import turtle       
window = turtle.Screen()    
window.bgcolor("white")
window.title("Jogo da Forca")
tartaruga= turtle.Turtle()  
tartaruga.speed(5)  
tartaruga.penup()      
tartaruga.setpos(-200,0)
tartaruga.pendown()
tartaruga.color("black")

dist = 100
angulo = 90
tartaruga.left(angulo)  
tartaruga.forward(dist) 
    
dist = 50
angulo=-90
tartaruga.left(angulo)  
tartaruga.forward(dist) 

window.exitonclick()

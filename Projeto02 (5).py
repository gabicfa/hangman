# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:17:19 2015

@author: gabialmeida

"""
 
from random import choice
import turtle 
from turtle import *

d = open("palavras.txt", encoding="utf-8")
c= d.readlines()
lista = list()

for i in c:
    p= i.strip()
    if p != "":
        lista.append(p)

e =choice(lista)

l= list(e)
print(l)

letra= list()
for a in l:
    b= a.strip()
    if b!= "":
        letra.append(b)

n=len(l)
m=len(letra)
  
window = turtle.Screen()    
window.title("Jogo da Forca")
tartaruga1= turtle.Turtle()  
tartaruga1.speed(5)  
tartaruga1.penup()      
tartaruga1.setpos(-500,-100)
tartaruga1.pendown()
tartaruga1.color("black")

dist = 200
angulo = 90
tartaruga1.left(angulo)  
tartaruga1.forward(dist) 
    
dist = 50
angulo=-90
tartaruga1.left(angulo)  
tartaruga1.forward(dist)

tartaruga2= turtle.Turtle()  
tartaruga2.speed(5)  
tartaruga2.penup()      
tartaruga2.setpos(-300,0)
tartaruga2.pendown()
tartaruga2.color("black")

for i in range(n):
    if l[i]!=" ":
        tartaruga2.forward(40)
        tartaruga2.penup()
        tartaruga2.forward(20)
        tartaruga2.pendown()
    else:
        tartaruga2.penup()
        tartaruga2.forward(60)
        tartaruga2.pendown()

#indicar que maisculo eh igual a minusculo e que letras com acentos sao iguais a letras sem acentos
#indicargar de novo
#excluir palavra ja jogada da lista
erros= 0
acertos=0
media= 0

while erros <6 and acertos <m:
    jogador = window.textinput("letras", "Digite uma Letra")
    if jogador in l :
      c= l.index(jogador)
      pen1=Pen()
      pen1.penup()
      pen1.goto(-300,10)
      pen1.forward(60*c+10)
      pen1.pendown()
      pen1.color('black')
      pen1.write(jogador, font= ("Arial", 14, "normal"))
      acertos+=1
    else:
        erros+=1
        if erros==1:
            pen=Pen()
            pen.penup()
            pen.goto(-450,60)
            pen.pendown()
            pen.circle(20)
        if erros==2:
            pen.goto(-450,10)
        if erros==3:
            dist = 40
            angulo=-45
            pen.left(angulo)  
            pen.forward(dist)
        if erros==4:
            pen.goto(-450,10)
            dist = 40
            angulo=270
            pen.left(angulo)  
            pen.forward(dist)
        if erros==5:
            pen.penup()
            pen.goto(-450,40)
            pen.pendown()
            dist = 30
            pen.forward(dist)
        if erros==6:
            pen.penup()
            pen.goto(-450,40)
            pen.pendown()
            dist= 40
            angulo=90
            pen.left(angulo)
            pen.forward(dist)

jogadas= 'erros'+'acertos'
media= 'acertos'/'jogadas'
print ("media de acertos: %f5.2" % media)

window.exitonclick()



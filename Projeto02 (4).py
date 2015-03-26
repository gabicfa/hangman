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

n=len(l)
  
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
#falta espacar palavras diferentes
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
#falta fazer imprimir letras na tela, conta o numero de acertos para fazer media
#indicar que maisculo eh igual a minusculo e que letras com acentos sao iguais a letras sem acentos
#indicar quando algo invalido foi escrito
#perguntar se quer jogar de novo
#excluir palavra ja jogada da lista
erros= 0 
acertos=0
while erros<6 and acertos<n:
    jogador = window.textinput("letras", "Digite uma Letra")
    if jogador in l :
     print("true")
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

window.exitonclick()



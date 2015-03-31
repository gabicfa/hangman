# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:17:19 2015

@author: gabialmeida

"""
 
from random import choice
import turtle 
from turtle import *

def desenhar_forca():
    pen1= Pen()  
    pen1.speed(5)  
    pen1.penup()      
    pen1.setpos(-500,-100)
    pen1.pendown()
    pen1.color("orange")
    
    dist = 200
    angulo = 90
    pen1.left(angulo)  
    pen1.forward(dist) 
        
    dist = 50
    angulo=-90
    pen1.left(angulo)  
    pen1.forward(dist)
    
    dist=30
    angulo=90
    pen1.right(angulo)
    pen1.forward(dist)
    

def  desenhar_tracos():   
    pen2.penup()      
    pen2.setpos(-300,-100)
    pen2.pendown()
    pen2.color("blue")
    
    for i in range(n):
        if l[i]!=" ":
            pen2.forward(40)
            pen2.penup()
            pen2.forward(20)
            pen2.pendown()
        else:
            pen2.penup()
            pen2.forward(60)
            pen2.pendown()
            
def letras_com_acento():
    pen3.penup()
    pen3.goto(-300,-100)
    pen3.forward(60*i + 10)
    pen3.pendown()
    pen3.write(l[i], font= ("Arial", 14, "normal"))
           

window = turtle.Screen()    
window.title("Jogo da Forca")
    
desenhar_forca()

x = "sim"

d = open("palavras.txt", encoding="utf-8")
c= d.readlines()
lista = list()

for i in c:
    p= i.strip().lower()
    if p != "":
        lista.append(p)

acertos1=0
erros1=0

while x=="sim" and len(lista)>0:

    e =choice(lista)
    l= list(e)
    
    letra= list()
    for a in l:
        b= a.strip()
        if b!= "":
            letra.append(b)
    
    n=len(l)
    m=len(letra)
    
    pen2= Pen()
    desenhar_tracos()
     
    erros2=0
    acertos2=0
    pen3=Pen()
    pen3.color("purple")
    pen4=Pen()
    pen4.color("pink")
    while erros2 <6 and acertos2 <m:
        jogador = window.textinput("letras", "Digite uma Letra")

        if jogador in l :
            for i in range(len(l)):
                if jogador == l[i]:
                  pen3.penup()
                  pen3.goto((-300 + 60*i + 10), -100)
                  pen3.pendown()
                  pen3.write(jogador, font= ("Arial", 14, "normal"))
                  acertos2 +=1
                elif jogador=="o" and l[i]=="ó" or l[i]=="ô":
                    letras_com_acento()
                    acertos2 +=1
                elif jogador=="a" and l[i]=="ã":
                    letras_com_acento()
                    acertos2 +=1
                elif jogador=="i" and l[i]=="í":
                    letras_com_acento()
                    acertos2 +=1
                
        else:
            erros2 +=1
            if erros2==1:
                pen4.penup()
                pen4.goto(-450, 30)
                pen4.pendown()
                pen4.circle(20)
            if erros2==2:
                pen4.goto(-450,-20)
            if erros2==3:
                dist = 40
                angulo=-45
                pen4.left(angulo)  
                pen4.forward(dist)
            if erros2==4:
                pen4.goto(-450,-20)
                dist = 40
                angulo=270
                pen4.left(angulo)  
                pen4.forward(dist)
            if erros2==5:
                pen4.penup()
                pen4.goto(-450,10)
                pen4.pendown()
                dist = 30
                pen4.forward(dist)
            if erros2==6:
                pen4.penup()
                pen4.goto(-450,10)
                pen4.pendown()
                dist= 40
                angulo=90
                pen4.left(angulo)
                pen4.forward(dist)
    acertos1 = acertos1 + acertos2
    erros1= erros1 + erros2           
    jogadas= acertos1 + erros1
    media= acertos1 / jogadas
    print (media)
    if acertos2==m:           
        x=str(window.textinput("Novamente", " PARABENS, VOCE ACERTOU A PARAVRA! Sua media foi de %5.2f acertos/palavra Jogar novamente? (sim ou nao)" % (media)))
    else:
        x=str(window.textinput("Novamente", " VOCE PERDEU! Sua media foi de %5.2f! Jogar novamente? (sim ou nao)" %(media)))
    if x=="sim":
        pen2.clear()
        pen2.reset()
        pen3.clear()
        pen3.reset()
        pen4.clear()
        pen4.reset()
        lista.remove(e)
        
y=str(window.textinput("fim", "O JOGO ACABOU"))
    
window.exitonclick()

    
    

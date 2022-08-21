# -*- coding: utf-8 -*-
"""
Created on Wed May 18 20:01:19 2022

@author: 91986
"""

import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,10],'ro--','bs---','ro','g^')
plt.ylabel("some values")
plt.xlabel("static values")
import matplotlib.pyplot as plt
Estimates=[1000,1010,1786,2000,1500,1500,100,120,150,150,150,170,175,180,197,200,200,200,200,200,200,220,220,220,220,234,250,250,250,263,270,275,275,286,300,300,300,300,300,300,300,300,320,350,350,400,400,400,400,400,450,467,500,500,500,500,500,500,550,550,600,600,600,650,700,700,720]
y=[]
for i in range(len(Estimates)):
    y.append(5)
plt.plot(Estimates,y)
#now next
def play():
    p1name=input('player 1,please enter your name')
    p2name=input('player 2,please enter your name')
    pp1=0
    pp2=0
play()
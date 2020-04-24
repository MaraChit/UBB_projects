# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 00:53:59 2020

@author: Ioana
"""
from copy import deepcopy 
from numpy import random
import math

def generate(matrix,n):
    cop = deepcopy(matrix)
    for i in range (0,n):
        for j in range (0,n):
            if cop[i][j]==0:
                cop[i][j]=random.randint(1,n+1)
                
    return cop

def checkSol(sol,n):
    #print(sol)
    for i in range (0,n):
        lista = []
        for j in range (0,n):
            lista.append(sol[i][j])
            
        #print(lista)
        if len(set(lista)) < n:
            #print(set(lista))
            return False
        
    for i in range (0,n):
        lista = []
        for j in range (0,n):
            lista.append(sol[j][i])
        #print(lista)
        if len(set(lista)) < n:
            #print(set(lista))
            return False
        
    """x=int(math.sqrt(n))
    for i in range (0,x):
        lista = []
        for j in range (0,x):
            lista.append(sol[i][j])
    if len(set(lista)) < n:
            return False"""
        
    return True

def start():
    #n = int(input("Number of squares: "))
    n=4
    m=[[3,0,0,2],[0,1,4,0],[1,2,0,4],[0,3,2,1]]
    """
    #sol=checkSol(generate(m,n),n)
    while checkSol(generate(m,n),n):
        checkSol(generate(m,n),n)"""
    
    ok= False
    while not ok:
        matrix=generate(m,n)
        #print(ok)
        ok=checkSol(matrix,n)
        #print(ok)
        if ok== True:
            print(matrix)
       

start()
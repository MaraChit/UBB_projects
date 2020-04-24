# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 23:44:32 2020

@author: Ioana
"""
from numpy import random
#import math

def read():
    words=[]
    f = open('words.txt','r')
    x=f.readline().split()
    print(x)
    for i in range (0, len(x)):
        words.append(x[i])
    f.close()
    return words

def splitWords(words):
    splitList =[]
    for el in words:
        for i in range(0, len(el)):
            splitList.append(el[i])
            
    return set(splitList)

def generateSol(words):
    
    solution = {}
    listt = splitWords(words)
    for charr in listt :
        if charr <= 'z' and charr >= 'a':
            solution[charr]=random.randint(0,16)
     
    return solution

def turnToNumbers(solution, words):
    numbers = []
    for word in words:
        if word not in ["=","+","-"]:
            x=0
            nr=0
            for charr in range (len(word)-1,-1,-1):
                nr=nr+solution[word[charr]]*pow(16,x)
                x=x+1
            numbers.append(nr)
        
    return numbers     

def checkCond(numbers, op):
    if op == '+':
        summ = 0
        for nr in range (0,len(numbers)-1):
            summ = summ + numbers[nr]
        if summ == numbers[-1]:
            return True
        
    elif op == '-' :
        summ = numbers[0]
        for nr in range (1,len(numbers)-1):
            summ = summ - numbers[nr]
        if summ == numbers[-1]:
            return True
    
    return False
        
    

def start():
    #words=['i','+','am','=','me']
    words=read()
    #print(words)
    op = words[1]
    #print(op)
    for i in range (0, 10000):
        sol=generateSol(words)
        nrs=turnToNumbers(sol,words)
       #print(sol)
        if checkCond(nrs,op):
            print(sol)
            break


start()

#[eat, +,cake,=, healthy]
#[e, a, t, c, a, k, e, h , e,  a, l, t, h, y]

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:50:07 2020

@author: Ioana
"""
from particle import particle
from random import random, randint
from copy import deepcopy
#from numpy.core._multiarray_umath import square

class pso:
    def __init__(self, n, noOfParticles, w, c1, c2):
        self.__population = [particle(n) for x in range(noOfParticles)]
        self.__size = noOfParticles
        self.__n = n
        self.__neighbours = self.selectNeighbours()
        self.__params = [w,c1,c2]
    
    def getPop(self):
        return self.__population
    
    def selectNeighbours(self):
        nSize = 10
        neighbors=[]
        pop = self.__population
        for i in range(len(self.__population)):
            localNeighbor=[]
            for j in range(nSize):
                x=randint(0, len(pop)-1)
                while (x in localNeighbor or x == i):
                    x=randint(0, len(pop)-1)
                localNeighbor.append(x)
            neighbors.append(localNeighbor.copy())
        return neighbors
        
    def square(self,p):
        indS = p[0]
        indT = p[1]
        s = ""
        for i in range(self.__n):
            for j in range(self.__n):
                s += "("+"{:.2f}".format(indS[i][j])+", "+"{:.2f}".format(indT[i][j])+")"+" "
                #s += "("+str(indS[i][j])+", "+str(indT[i][j])+")"+" "

            s+="\n"
        return s
    
    def getBest(self):
        pop = self.__population
        bestP = pop[0].bestPozition
        bestF = pop[0].bestFit
        for i in range(self.__size):
            if pop[i].bestFit < bestF:
                bestF = pop[i].bestFit
                bestP = pop[i].bestPozition
        return (bestF, bestP)
    
    def getSol(self):
        pop = self.__population
        bestP = pop[0].position
        bestF = pop[0].fit
        for i in range(self.__size):
            if pop[i].fit < bestF:
                bestF = pop[i].fit
                bestP = pop[i].position
        return (bestF, bestP)
    
    
    def iteration(self, w):
        bestN = []
        pop = self.__population
        bestP = 0
        sBestP = 1
        for i in range(1,len(pop)):
            if pop[i].bestFit < pop[bestP].bestFit:
                sBestP = bestP
                bestP = i 
         
        for i in range(len(pop)):
            if i != bestP:
                bestN.append(bestP)
            else:
                bestN.append(sBestP)
        
        c1 = self.__params[1]
        c2 = self.__params[2]
        for i in range(len(pop)):
            for k in range(self.__n):
                for j in range(self.__n):
                    newVelocity = w * pop[i].velocity[0][k][j]
                    newVelocity = newVelocity + c1*random()*(pop[bestN[i]].position[0][k][j]-pop[i].position[0][k][j])    
                    newVelocity = newVelocity + c2*random()*(pop[i].bestPozition[0][k][j]-pop[i].position[0][k][j])
                    pop[i].setVelocity(0,k,j,newVelocity)
                    
                    newVelocity = w * pop[i].velocity[1][k][j]
                    newVelocity = newVelocity + c1*random()*(pop[bestN[i]].position[1][k][j]-pop[i].position[1][k][j])    
                    newVelocity = newVelocity + c2*random()*(pop[i].bestPozition[1][k][j]-pop[i].position[1][k][j])
                    pop[i].setVelocity(1,k,j,newVelocity)
        for i in range(len(pop)):
            newPos = [[],[]]
            for k in range(self.__n):
                newPos[0].append([])
                newPos[1].append([]) 
                for j in range(self.__n):
                    newPos[0][k].append(pop[i].position[0][k][j]+pop[i].velocity[0][k][j])
                    newPos[1][k].append(pop[i].position[1][k][j]+pop[i].velocity[1][k][j])
            pop[i].setPos(deepcopy(newPos))
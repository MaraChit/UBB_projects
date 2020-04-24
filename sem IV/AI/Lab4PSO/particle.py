# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:39:42 2020

@author: Ioana
"""

from copy import deepcopy
import numpy as np

class particle:
    def __init__(self, n):
        self.__squareSize = n
        self.__position = self.initParticle()
        self.__bestFitness = 100
        self.__bestPozition = deepcopy(self.__position)
        self.__fit = self.fitness(self.__position)
        self.__velocity = self.initVelocity()
        
    
    def fitness(self, position):
        errors = 0.0 
        indS = deepcopy(position[0])
        indT = deepcopy(position[1])
        for i in range(len(indS)):
            for j in range(len(indS)):
                indS[i][j] = int(indS[i][j])
                indT[i][j] = int(indT[i][j])
            
        for i in range(self.__squareSize):
            lstS = [0] * self.__squareSize
            lstT = [0] * self.__squareSize
            for j in range(self.__squareSize):
                if indS[j][i] in range(1,self.__squareSize+1):
                    lstS[indS[j][i]-1] = 1
            
                if indT[j][i] in range(1,self.__squareSize+1):
                    lstT[indT[j][i]-1] = 1
            for j in range(self.__squareSize):
                if lstS[j] == 0:
                    errors = errors + 1
                if lstT[j] == 0:
                    errors = errors + 1
                  
        for i in range(self.__squareSize):
            for j in range(self.__squareSize):
                for k in range(self.__squareSize):
                    for l in range(self.__squareSize):
                        if i != k or j != l:
                            if indS[i][j] == indS[k][l] and indT[i][j] == indT[k][l]:
                                errors = errors + 1
                                  
        indS = deepcopy(position[0])
        indT = deepcopy(position[1])
                
        for i in range(len(indS)):
            for j in range(len(indS)):
                indS[i][j] = int(indS[i][j])
                indT[i][j] = int(indT[i][j])
        
        for j in range(len(indS)):
            pS = indS[j]
            pS.sort()
            pT = indT[j]
            pT.sort()
            for i in range(self.__squareSize):
                if pS[i] != i+1:
                    errors = errors + 1
                if pT[i] != i+1:
                    errors = errors + 1
        
        if errors < self.__bestFitness:
            self.__bestFitness = errors
            self.__bestPozition = deepcopy(self.__position)
        
        return errors
    
    @property
    def velocity(self):
        return self.__velocity
    
    def setVelocity(self,i,j,k,value):
        self.__velocity[i][j][k] = value
    
    @property
    def fit(self):
        self.__fit = self.fitness(self.__position)
        return self.__fit
    
    @property
    def bestFit(self):
        return self.__bestFitness
    
    @property
    def position(self):
        return self.__position
    
    @property
    def bestPozition(self):
        return self.__bestPozition
    
    def initVelocity(self):
        l = []
        for i in range(self.__squareSize):
            l.append(0)
        a=[]
        for i in range(self.__squareSize):
            a.append(l)
        return [a,a]    
                     
    def setPos(self,p):
        self.__position = p
        self.__fit = self.fitness(self.__position)
                     
    def initParticle(self):
        return [list(list(np.random.permutation(self.__squareSize)+1) for x in range(self.__squareSize)), 
                list(list(np.random.permutation(self.__squareSize)+1) for x in range(self.__squareSize))]
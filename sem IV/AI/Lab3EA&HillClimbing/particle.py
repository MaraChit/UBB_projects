# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:21:45 2020

@author: Ioana
"""
from numpy import random

class Particle:
    def __init__(self,n):
        '''
        constructor
        n: size of poz
        '''
        self._n = n
        self._position =self.generateMatrix()
        self._velocity =self.generateMatrix()
        self._fitness = self.evaluate()
        
        #memory of the particle
        self._bestPosition=self._position.copy()
        self._bestFitness=self._fitness
    
    def generateMatrix(self):
        matrix=[]
        for i in range (0,self._n):
            matrix.append([])
        for i in range (0,self._n):
            for j in range (0,self._n):
                tupple=[]
                tupple.append(random.randint(1,self._n+1))
                tupple.append(random.randint(1,self._n+1))
                matrix[j].append(tupple)
        return matrix
    
    def evaluate(self):
        """ evaluates the particle """
        return self.fit(self._pozition)
        
    def fit(self,poz):
        """
        Determine the fitness of a particle. Lower is better.(min problem)
        pozition: the pozition of the particle we wish to evaluate
        """
        fit=0
        n=len(poz)
        
        #check for duplicates
        for i in range (0,n):
            for j in range(0,n):
                for x in range(0,n):
                    for l in range(0,n):
                        if i!=x or j!=l:
                            
                            if poz[i][j]==poz[x][l]:
                                fit = fit + 1
                
        
        
        #verify permutations on line
        for i in range (n):
            for j in range (n-1):
                if poz[i][j][0] != poz[i][j+1][0] or poz[i][j][1] != poz[i][j+1][1]:
                    fit = fit + 1
                
        #verify permutations on column
        for i in range (n-1):
            for j in range (n):
                if poz[i][j][0] != poz[i+1][j][0] or poz[i][j][1] != poz[i+1][j][1]:
                    fit = fit + 1
        return fit
    
    @property
    def getPosition(self):
        """ getter for pozition """
        return self._position

    @property
    def getFitness(self):
        """ getter for fitness """
        return self._fitness

    @property
    def getBestPozition(self):
        """ getter for best pozition """
        return self._bestPosition

    @property
    def getBestFitness(self):
        """getter for best fitness """
        return self._bestFitness
    
    def setPosition(self, newPoz):
        '''
        setter for position
        newPoz: the new position
        '''
        self._position=newPoz.copy()
        self._fitness=self.evaluate()
        # automatic update of particle's memory
        if (self._fitness<self._bestFitness):
            self._bestPosition = self._position
            self._bestFitness  = self._fitness
            

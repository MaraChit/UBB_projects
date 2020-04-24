# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:25:08 2020

@author: Ioana
"""

from numpy import random


class Population:
    
    def __init__(self,n,k):
        '''
        k: nr of individuals
        n: size of the individual
        '''
        self._n=n
        self._k=k
        
    def setSize(self,newN,newK):
        self._n=newN
        self._k=newK
        
    def individual(self):
        '''
        creates an individual with random numbers
        '''
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
    
    def population(self):
        '''
        generates a population of k individuals

        '''
        pop=[]
        for i in range (0,self._k):
            pop.append(self.individual())
        
        return pop
        
    
    def fitness(self,ind):
        '''
        returns the fitness of an individual: counts the number of "mistakes" in an individual
        mistakes= nr of duplicates + nr of cells that aren't permutations
        ind: individual to be analized
        '''
        fit=0
        
        #check for duplicates
        for i in range (0,self._n):
            for j in range(0,self._n):
                for x in range(0,self._n):
                    for l in range(0,self._n):
                        if i!=x or j!=l:
                            
                            if ind[i][j]==ind[x][l]:
                                fit = fit + 1
                
        
        
        #verify permutations on line
        for i in range (self._n):
            for j in range (self._n-1):
                if ind[i][j][0] != ind[i][j+1][0] or ind[i][j][1] != ind[i][j+1][1]:
                    fit = fit + 1
                
        #verify permutations on column
        for i in range (self._n-1):
            for j in range (self._n):
                if ind[i][j][0] != ind[i+1][j][0] or ind[i][j][1] != ind[i+1][j][1]:
                    fit = fit + 1
        

        return fit
        

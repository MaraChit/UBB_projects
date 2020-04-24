# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:18:29 2020

@author: Ioana
"""
from numpy import random

class EA:
    
    def __init__(self,n):
        '''
        n: size of the individual
        '''
        self._n=n
    
    def setSize(self,newN):
        self._n=newN
    
    
    def crossover(self,parent1, parent2):
        '''
        create a new individual from two others
        parent1, parent2: individuals to be combined
        '''
        
        child=[]
        for i in range (0,self._n):
            child.append([])
            
        index=random.randint(1,self._n-1)
        
        for i in range (0,index):
            for j in range (0,self._n):
                child[i].append(parent1[i][j])
                
        for i in range (index,self._n):
            for j in range (0,self._n):
                child[i].append(parent2[i][j])
            
        return child
    
    def mutation(self, parent):
        '''
        create a new individual by modifying another one
        parent: individual to be modified
        '''
        ind1 = random.randint(0,self._n)
        ind2 = random.randint(0,self._n)
        parent[ind1][ind2]=[random.randint(1,self._n+1),random.randint(1,self._n+1)]
        
        return parent
        
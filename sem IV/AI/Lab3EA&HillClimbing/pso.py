# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:39:42 2020

@author: Ioana
"""

from numpy import random

class PSO:
    def __init__(self,population):
        '''
        constructor
        population: particle population
        '''
        self._population= population
    
    def chooseNeighbour(self,nSize):
        '''
        generates a neighborhood of size nSize for a particle from the given population
        returns a matrix containg the positions of each neighborhood
        '''
        
        if (nSize>len(self._population)):
            nSize=len(self._population)

        neighbors=[]
        for i in range(len(self._population)):
            localNeighbor=[]
            for j in range(nSize):
                x=random.randint(0, len(self._population)-1)
                while (x in localNeighbor):
                    x=random.randint(0, len(self._population)-1)
                localNeighbor.append(x)
            neighbors.append(localNeighbor.copy())
        #print (neighbors)
        return neighbors
    

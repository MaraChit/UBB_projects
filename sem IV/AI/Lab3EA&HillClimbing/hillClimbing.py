# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:37:05 2020

@author: Ioana
"""
from numpy import random

class HillClimbing:
    
    def __init__(self,n):
        '''
        n:size of individual
        '''
        self._n=n
        
    def setSize(self,newN):
        self._n=newN
        
    def generateNeighbour(self,ind):
        '''
        generates a neighbour
        ind: the individual who's neighbour will be generated
        '''
        i=random.randint(1,self._n-1)
        j=random.randint(1,self._n-1)
        ind[i][j][0] =random.randint(1,self._n-1)
        ind[i][j][1]=random.randint(1,self._n-1)
        
        return ind

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:23:53 2020

@author: Ioana
"""
from particle import Particle

class ParticlePopulation:
    def __init__(self,n,k):
        '''
        constructor
        k:nr of particle
        n:size of particle
        '''
        self._k = k
        self._n = n
        #self._particle= Particle(self._n)
    
    def setData(self, newN, newK):
        self._k=newK
        self._n=newN
        
    def populationGenerate(self):
        '''
        generates a population of k particles
        WE PRESUME a population represents a neighborhood

        '''
        pop=[]
        for i in range (0,self._k):
            pop.append(Particle(self._n))
        
        return pop
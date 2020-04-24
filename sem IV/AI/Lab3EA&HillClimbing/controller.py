# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:23:19 2020

@author: Ioana
"""

from numpy import random

class Controller:
    def __init__(self,population,ea,noIt,k,hc,particles,pso):
        '''
        population: the populationof individuals  to be used
        ea: the class Ea
        hc: the class HillClimbing
        pso: the class PSO
        noIt: nr of iterations
        k: nr of individuals
        particles: the population of particles
        '''
        self._population=population
        self._ea=ea
        self._noIt=noIt
        self._k=k
        self._hc=hc
        self._pso=pso
        self._particles=particles
        
        
    def setData(self, newNoIt, newK):
        self._noIt=newNoIt
        self._k=newK
        
    def iteration(self):
        '''
        performes noIt iterations on the population(EA)
        returns the individual with the best fitness at the end of all iterations
        '''
        pop=[]
        pop=self._population.population()
        for i in range(self._noIt):
            poz1=0
            poz2=0
            while poz1==poz2:
                poz1=random.randint(1,self._k)
                poz2=random.randint(1,self._k)
            kid=self._ea.crossover(pop[poz1],pop[poz2])
            kid=self._ea.mutation(kid)
            fit1=self._population.fitness(pop[poz1])
            fit2=self._population.fitness(pop[poz2])
            fit3=self._population.fitness(kid)
            if fit1>fit2 and fit1>fit3:
                pop[poz1]=kid
            elif fit2>fit1 and fit2>fit3:
                pop[poz2]=kid
                
        minFit=self._population.fitness(pop[0])
        poz=0
        for i in range (self._k):
            if self._population.fitness(pop[i]) < minFit:
                minFit=self._population.fitness(pop[i]) 
                poz=i
       
        return (pop,pop[poz])
    
    def iterationHC(self):
        '''
        performes noIt iterations on the population(HillClimbing Algorithm)
        returns the individual with the best fitness at the end of all iterations
        '''
        ind=self._population.individual()
        ind2=self._hc.generateNeighbour(ind)
        for i in range (self._noIt):
            fit1=self._population.fitness(ind)
            fit2=self._population.fitness(ind2)
            if fit1>fit2:
                ind=self._hc.generateNeighbour(ind)
            else:
                ind2=self._hc.generateNeighbour(ind2)
        
        fit1=self._population.fitness(ind)
        fit2=self._population.fitness(ind2)
        if fit1>fit2:
            return ind
        else:
            return ind2
        
    def iterationPSO (self, w, c1, c2, nSize):
        '''
        one iteration: for each particle we update the velocity and the position
                        according to the particle's memory and the best neighbor's position 
        this functions performs noIt iterations
        nSize: size of the neighborhood
        '''
        
        bestNeighbors=[]
        neighbors = self._pso.chooseNeighbour(nSize)
        pop=self._particles.populationGenerate(self._k)
        
        for iteration in range (0, self._noIt):
        
            #determine the best neighbor for each particle
            for i in range(len(pop)):
                bestNeighbors.append(neighbors[i][0])
                for j in range(1,len(neighbors[i])):
                    if (pop[bestNeighbors[i]].fitness>pop[neighbors[i][j]].fitness):
                        bestNeighbors[i]=neighbors[i][j]
                        
            #update the velocity for each particle
            for i in range(len(pop)):
                for j in range(len(pop[0].velocity)):
                    newVelocity = w * pop[i].velocity[j]
                    newVelocity = newVelocity + c1*random()*(pop[bestNeighbors[i]].position[j]-pop[i].position[j])    
                    newVelocity = newVelocity + c2*random()*(pop[i].bestPosition[j]-pop[i].position[j])
                    pop[i].velocity[j]=newVelocity
            
            #update the position for each particle
            for i in range(len(pop)):
                newposition=[]
                for j in range(len(pop[0].velocity)):
                    newposition.append(pop[i].position[j]+pop[i].velocity[j])
                pop[i].position=newposition
                
        return pop
            

        

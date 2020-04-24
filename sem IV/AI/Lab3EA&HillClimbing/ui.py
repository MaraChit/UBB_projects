# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:39:12 2020

@author: Ioana
"""
from ea_method import EA
from hillClimbing import HillClimbing
from population import Population
from particlePopulation import ParticlePopulation
from pso import PSO
from controller import Controller

import numpy as np
import matplotlib.pyplot as plt

class UI:
    
    def printMenu(self):
        print("0. Exit")
        print("1. Use EA")
        print("2. Use HillClimbing")
        print("3. Show EA's validation test")
        print("4. Use PSO")
        print("5. Show PSO's validation test")
    
    def __init__(self):
        self._population = Population(2,2)
        self._ea = EA(2)
        self._hc = HillClimbing(2)
        self._particles=ParticlePopulation(2,2)
        self._pso=PSO(self._particles)
        self._controller = Controller(self._population,self._ea,0,0,self._hc, self._particles.populationGenerate,self._pso)
      
        
    def readData(self):
        f = open("inputData.txt")
        x=f.readline().split()
        n=int(x[0])
        k=int(x[1])
        noIt=int(x[2])
        w=float(x[3])
        c1= float(x[4])
        c2= float(x[5])
        nSize=int(x[6])
        f.close()
        
        self._population.setSize(n,k)
        self._ea.setSize(n)
        self._hc.setSize(n)
        self._particles.setData(n,k)
        self._pso=PSO(self._particles)
        self._controller.setData(noIt,k)
        
        return (w,c1,c2,nSize)
        
    def runEA(self):
        (x,pop) = self._controller.iteration()
        for l in pop:
            print(l)
            
    def runHC(self):
        ind= self._controller.iterationHC()
        for l in ind:
            print(l)
            
    def validationEA(self):
        '''
        displays a graphical evaluation of the EA algorithm
        '''
        pop=[]
        avg=[]
        std=[]
        n=self._population._n
        for i in range(0,30):
            pop.append([])
            self._population= Population(n,40)
            self._controller= Controller(self._population,self._ea,1000,40,self._hc,self._particles,self._pso)
            for j in range (0,10):
                (ind,x)=self._controller.iteration()
                for k in ind:
                    pop[i].append(self._population.fitness(k))
            std.append(np.std(pop[i]))
            avg.append(np.mean(pop[i]))
        std =plt.plot(std,color='b',label='Standard deviation')
        avg =plt.plot(avg,color='r',label='Average')
        #plt.legend(handles[std,avg])
        plt.show()
                
    
    def runPSO(self,w,c1,c2,nSize):
        pop=self._controller.iterationPSO(w,c1,c2,nSize)
        best=pop[0]
        for i in pop:
            if i.bestFit<best.bestFit:
                best=i
        for l in best:
            print(l)
            
    def run(self):
        (w,c1,c2,nSize)=self.readData()
        while True:
            self.printMenu()
            opt = input("Choose an option: ")
            if opt == "1":
                self.runEA()
            elif opt == "2":
                self.runHC()
            elif opt == "3":
                self.validationEA()
            elif opt == "4":
                self.runPSO(w,c1,c2,nSize)
            elif opt == "0":
                return
        
    
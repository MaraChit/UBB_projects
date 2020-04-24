# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:54:10 2020

@author: Ioana
"""
from controller import Controller
from pso import pso
class UI:
    def __init__(self):
        self._controller = None
        self.bestSol = None
    
   
    def run(self):
        self._controller = Controller()
        n=4
        popSize=100
        iterations = 500
        w=1.0
        c1=0.7
        c2=0.7
        PSO = pso(n, popSize,w,c1,c2)
        i = 0
        while iterations > 0:
            self._controller.runPSO(PSO,w,i)
            print(iterations)
            iterations = iterations-1
            i=i+1
        (f,p) = PSO.getSol()
        print("Fit: ",f)
        print(PSO.square(p))
        s = "Fit: "+str(f)+"\n"+PSO.square(p)
        self.bestSol = s
        self._controller.runPSOValidationTest(n)


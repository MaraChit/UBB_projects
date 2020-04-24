# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:35:07 2020

@author: Ioana
"""
import numpy as np
import matplotlib.pyplot as plt
from pso import pso


class Controller:
    
    def runPSO(self,PSO,w,i):
        PSO.iteration(w/(i+1))
        
    def runPSOValidationTest(self,n):
        res = []
        std = []
        avg = []
        nrRuns = 10
        iterations = 100
        popSize = 40
        print("here goes the statistic in ...")
        for k in range (nrRuns):
            print(k)
            res.append([])
            PSO = pso(n,popSize,1.0, 0.7, 0.75)
            for i in range(iterations):
                PSO.iteration(1.0/(i+1))
                for ind in PSO.getPop():
                    res[k].append(ind.fit)
            std.append(np.std(res[k]))
            avg.append(np.mean(res[k]))
        std, = plt.plot(std,color='m',label='Standard deviation')
        avg, = plt.plot(avg,color='y', label='Average')
        plt.legend(handles=[std,avg])
        plt.show()
        pass
            

from Ant import Ant
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt

class Controller:
    def __init__(self):
        '''
        constructor
        '''
        self._n = None
        self._noEpoch = None
        self._noAnts = None
        self._alpha = None
        self._beta = None
        self._rho = None
        self._q0 = None

    def fitness(self,matrix):
        
        if matrix == []:
            return 100
        
        errors = 0
        
        for line in matrix:
            indS = [0] * self._n
            indT = [0] * self._n
            for [i, j] in line:
                if i > 0:
                    indS[i - 1] = 1
                if j > 0:
                    indT[j - 1] = 1
            for i in range(len(indS)):
                if indS[i] == 0:
                    errors = errors + 1
                if indT[i] == 0:
                    errors = errors + 1
                    
        for i in range(self._n):
            indS = [0] * self._n
            indT = [0] * self._n
            for j in range(self._n):
                if matrix[j][i][0] > 0:
                    indS[matrix[j][i][0] - 1] = 1
                if matrix[j][i][1] > 0:
                    indT[matrix[j][i][1] - 1] = 1
            for k in range(len(indS)):
                if indS[k] == 0:
                    errors = errors + 1
                if indT[k] == 0:
                    errors = errors + 1
                    
        return errors

    def iteration(self, noAnts, n, trace, alpha, beta, q0, rho):
        
        antSet = [Ant(n) for i in range(noAnts)]
        
        for i in range(noAnts):
            for ant in antSet:
                ant.update(q0, trace, alpha, beta)
        dTrace = [ [1.0 / antSet[i].evaluate(),1.0 / antSet[i].evaluate()]  for i in range(noAnts)]
        
        for i in range(self._n):
            for j in range(self._n):
                trace[i][j][0] = (1-rho) * trace[i][j][0]
                trace[i][j][1] = (1-rho) * trace[i][j][1]
                
        for x in range(self._n):
            for y in range(self._n):
                trace[x][y][0] = trace[x][y][0] + dTrace[x][0]
                trace[x][y][1] = trace[x][y][1] + dTrace[x][1]
                
        lista = [[antSet[i].evaluate(), i] for i in range(noAnts)]
        lista.sort(key = lambda x : x[0])
        
        return antSet[lista[0][1]].path



    def runAlg(self):
        solution = []
        bestSolution = []
        bestFit = 100
        trace=[]
        trace = [[[1,1] for i in range(self._n)] for j in range(self._n)]

        for i in range(self._noEpoch):
            solution = deepcopy(self.iteration(self._noAnts, self._n, trace, self._alpha, self._beta, self._q0, self._rho))
            
            if self.fitness(solution) < self.fitness(bestSolution):
                bestSolution = deepcopy(solution)
                bestFit = self.fitness(bestSolution)
                
        return (bestFit, bestSolution)

    def validationTest(self, n, alpha, beta, q0, rho):
        '''
        validation test 
        '''
        res = []
        std = []
        avg = []
        nrRuns = 30
        iterations = 100
        noAnts = 40
        
        print("Validation test starts")
        for k in range(0,nrRuns):
            print(k)
            res.append([])
            trace = [[[1, 1] for i in range(self._n)] for j in range(self._n)]
            for _ in range(iterations):
                antSet = [Ant(n) for i in range(noAnts)]
                for i in range(noAnts):
                    for ant in antSet:
                        ant.update(q0, trace, alpha, beta)
                dTrace = [[1.0 / antSet[i].evaluate(), 1.0 / antSet[i].evaluate()] for i in range(noAnts)]
                for i in range(self._n):
                    for j in range(self._n):
                        trace[i][j][0] = (1 - rho) * trace[i][j][0]
                        trace[i][j][1] = (1 - rho) * trace[i][j][1]
                for x in range(self._n):
                    for y in range(self._n):
                        trace[x][y][0] = trace[x][y][0] + dTrace[x][0]
                        trace[x][y][1] = trace[x][y][1] + dTrace[x][1]
                for ant in antSet:
                    res[k].append(ant.evaluate())
            std.append(np.std(res[k]))
            avg.append(np.mean(res[k]))
            
        std, = plt.plot(std, color='b', label='Standard deviation')
        avg, = plt.plot(avg, color='r', label='Average')
        
        plt.legend(handles=[std, avg])
        plt.show()

    def runValidationTest(self):
        self.validationTest(self._n,self._alpha,self._beta,self._q0,self._rho)


    def loadParameters(self,p):
        self._n = p.n
        self._noAnts = p.noAnts
        self._noEpoch = p.noEpoch
        self._alpha = p.alpha
        self._beta = p.beta
        self._rho = p.rho
        self._q0 = p.q0

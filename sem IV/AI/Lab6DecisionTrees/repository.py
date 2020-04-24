# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:46:08 2020

@author: Ioana
"""
import numpy as np

class Repository:
    def __init__(self):
        '''
        constructor
        '''
        self.header = []
        self.data = []
        self.testingData = []
        self.trainingData = []
        self.readFile()

    def readFile(self):
        '''
        reads from file and randomly separates data into testing data and training data
        '''
        self.data = []
        f = open("decision.txt")
        for line in f:
            if line!='\n':
                res = []
                s = line.split(",")
                for i in range(1, len(s)):
                    res.append(int(s[i]))
                res.append(s[0])
                self.data.append(res)
            
        np.random.shuffle(self.data)
        
        n = int(np.random.randint(35, 40) * len(self.data) / 100)
        
        for i in range(n):
            self.trainingData.append(self.data[i])
            
        for i in range(n, len(self.data)):
            self.testingData.append(self.data[i])

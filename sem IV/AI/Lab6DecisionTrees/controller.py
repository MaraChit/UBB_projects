# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:44:08 2020

@author: Ioana
"""

from repository import Repository
from node import Node
from leaf import Leaf
from splitBy import SplitBy

class Controller:
    
    def __init__(self, repo):
        '''
        constructor
        '''
        self.repository = repo
    
    def getGini(self, rows):
        '''
        calculates gini
        '''
        counts = self.count(rows)
        gini = 1
        for c in counts:
            p = float(counts[c] / len(rows))
            gini = float(gini - p * p)
        return gini

    def getGain(self, yesRows, noRows, gini):
        '''
        calculates gain
        '''
        p = float(len(yesRows)) / (len(yesRows) + len(noRows))
        return gini - p * self.getGini(yesRows) - (1 - p) * self.getGini(noRows)
    
    def splitRows(self, rows, split):
        '''
        returns colums to be added on the yesBranch and those to be added on 
                the noBranch
        '''
        yesRow = []
        noRow = []
        
        for row in rows:
            if split.chooseYesBranch(row):
                yesRow.append(row)
            else:
                noRow.append(row)
        return yesRow, noRow
    
    def findBestSplit(self, rows):
        '''
        returns the best split and the best gain
        (we consider values 1 and 5 not worth splitting by)
        '''
        bestGain = 0
        bestSplit = None
        
        gini = self.getGini(rows)
        for i in range(len(rows[0]) - 1):
            values = set([row[i] for row in rows])
            for val in values:
                if val in [1, 5]:
                    continue
                split = SplitBy(i, val)
                yesRows, noRows = self.splitRows(rows, split)
                
                if len(yesRows) != 0 and len(noRows) != 0:
                    gain = self.getGain(yesRows, noRows, gini)
                    
                    if gain >= bestGain:
                        bestGain, bestSplit = gain, split
                        
        return bestGain, bestSplit

    def buildTree(self, rows):
        '''
        builds DT
        '''
        gain, split = self.findBestSplit(rows)

        if gain == 0:
            return Leaf(rows)

        yesRows, noRows = self.splitRows(rows, split)
        yesBranch = self.buildTree(yesRows)
        noBranch = self.buildTree(noRows)

        return Node(yesBranch, noBranch, split)

    def count(self, rows):
        
        counts = {}
        for row in rows:
            label = row[-1]
            if label not in counts:
                counts[label] = 0
            counts[label] = counts[label] + 1
        return counts

    def classify(self, row, node):
        '''
        iterates through the DT
        '''
        if isinstance(node, Leaf):
            return node.predictions
        
        if node.split.chooseYesBranch(row):
            return self.classify(row, node.yesBranch)
        
        return self.classify(row, node.noBranch)
    
    def runAlg(self):
        
        bestAcc = 0
        res = []
        
        for i in range(1000):
            self.repository = Repository()
            
            trainingData = self.repository.trainingData
            tree = self.buildTree(trainingData)
            testingData = self.repository.testingData
            total = 0
            correct = 0
            
            for row in testingData:
                expectedResult = row[-1]
                treeResult = list(self.classify(row, tree).keys())
                
                if expectedResult == treeResult[0]:
                    correct = correct + 1
                    
                total = total + 1
                
            accuracy = float((correct * 100)/total)
            res.append(accuracy)
            
            if accuracy > bestAcc:
                bestAcc = accuracy
                print("Accuracy: "+str(bestAcc)+"%","Iteration: ", i)
        
        print("DONE!")

    
    

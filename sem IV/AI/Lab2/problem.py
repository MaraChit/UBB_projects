# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:24:49 2020

@author: Ioana
"""


from state import State
from copy import deepcopy

class Problem:
    def __init__(self, initState:State):
        self._initState = initState
        self._values = None
        
   #retrun root
    def getRoot(self):
        return deepcopy(self._initState)
    
    #check if a matrix is valid 
    def isValid(self, matrix:State):
        for line in matrix.getValues():
            if sum(line) > 1:
                return False
            
        for i in range(len(matrix.getValues())):
            col = []
            for j in range(len(matrix.getValues())):
                col.append(matrix.getValues()[i][j])
            if sum(col) > 1:
                return False
            
        return True
    #return number of elems's in matrix
    def getNumberOfElems(self, matrix:list,elem:int):
        nr = 0
        for line in matrix:
            for el in line:
                if el == elem:
                    nr=nr+1
        return nr
    
    def getZeroPositions(self,matrix:list):
        empty = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 0:
                    empty.append((i,j))
        return empty
    
    def expand(self,currentState: State):
        values = currentState.getValues()
        positions = self.getZeroPositions(values)
        ones = self.getNumberOfElems(values,1)

        if ones >= len(values):
            return []
        result = []
        for t in positions:
            auxiState = deepcopy(currentState)
            auxiState.setOne(t[0],t[1])
            result.append(auxiState)
        return  result
    
    def isSolution(self,matrix: State):
        
        for line in matrix.getValues():
            if sum(line) != 1:
                return False
            
        for i in range(len(matrix.getValues())):
            col = []
            for j in range(len(matrix.getValues())):
                col.append(matrix.getValues()[j][i])
            if sum(col) != 1:
                return False

        vals = matrix.getValues()
        ones = self.getNumberOfElems(vals,1)
        
        if ones != len(vals):
            return False

        for i1 in range(len(vals)):
            for j1 in range(len(vals)):
                if vals[i1][j1] == 1:
                    for i2 in  range(len(vals)):
                        for j2 in range(len(vals)):
                            if i1!=i2 and j1!=j2:
                                if vals[i2][j2] == 1:
                                    if abs(i1-i2)-abs(j1-j2) == 0:
                                        return False
        return True

    def heuristic(self,matrix):
        if not self.isValid(matrix):
            return -1
        
        vals=matrix.getValues()
        return self.getNumberOfElems(vals, 0)


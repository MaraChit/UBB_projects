# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:23:42 2020

@author: Ioana
"""

class State:
    
    #initial state is empty matrix
    def __init__(self, size:int):
        self._size = size
        self._values=[]
        for x in range(size):
            self._values.append([0]*size)
            
    """
    get and set functions
    """
    
    def getSize(self):
        return self._size
    
    def setSize(self, newSize:int):
        self._size=newSize
            
    def getValues(self):
        value=[]
        for line in self._values:
            value.append(line)
        return value
    
    def setValues(self, val:list):
        self._size= len(val)
        value=[]
        for line in val:
            value.append(line)
        self._values = value
        
    #set on 1, one field from the matrix    
    def setOne(self,line: int,col: int):
        self._values[line][col] = 1
        
    #toString fct
    def __str__(self):
        matrix=""
        for line in self._values:
            for x in line:
                matrix = matrix + " " +str(x)
            matrix=matrix + '\n'
        return matrix
    
    
    #check-equality fct
    def __eq__(self, other):
        if not isinstance(other,State):
            return False
        
        instance = other.getValues()

        if len(instance) != self._size:
            return False

        for i in range(self._size):
            for j in range(self._size):
                if instance[i][j] != self._values[i][j]:
                    return False
        return True
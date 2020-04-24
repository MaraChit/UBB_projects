# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:26:22 2020

@author: Ioana
"""
from problem import Problem
from state import State

class Controller:

    def __init__(self):
        self._problem = Problem(State(4))
        self._states = [self._problem.getRoot()]
        
    def chooseSize(self, n):
        self._problem = Problem(State(n))
        self._states = [self._problem.getRoot()]
        
    def DFS(self):
        stk = [self._problem.getRoot()]
        visited = []

        while len(stk) > 0:
            node = stk.pop()
            if self._problem.isSolution(node):
                print("Solution")
                print(node)
                return
            visited.append(node)
            if self._problem.isValid(node):
                newStates = self._problem.expand(node)
                lst = []
                for newState in newStates:
                    if newState not in visited:
                        lst.append(newState)
                stk += lst

        print("No solution")

    
    def Greedy(self):
        visited = []
        toVisit = [self._problem.getRoot()]
        while len(toVisit) > 0:
            state = toVisit.pop(0)
            visited.append(state)
            if self._problem.isSolution(state):
                print("Solution")
                print(str(state))
                return
            elif self._problem.isValid(state):
                v = []
                nextNodes = self._problem.expand(state)
                for node  in nextNodes:
                    if node not in visited:
                        v.append((self._problem.heuristic(node), node))
                v.sort(key=lambda x : x[0])
                v = [x[1] for x in v]
                toVisit = v[:] + toVisit
        print("No solution")
    
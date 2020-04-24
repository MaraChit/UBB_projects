# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:25:52 2020

@author: Ioana
"""
from controller import Controller

class UI:
    
    def printMenu(self):
        print("0. Exit")
        print("1. Use DFS")
        print("2. Use Greedy")
        
    def __init__(self):
        self._controller = Controller()
        
    def chooseSize(self):
        f = open("input.txt")
        n = int(f.readline())
        f.close()
        self._controller.chooseSize(n)
        
    def runDFS(self):
        self._controller.DFS()
        
    def runGreedy(self):
        self._controller.Greedy()
        
    def run(self):
        self.chooseSize()
        while True:
            self.printMenu()
            opt = input("Choose an option: ")
            if opt == "1":
                self.runDFS()
            elif opt == "2":
                self.runGreedy()
            elif opt == "0":
                return


# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 08:08:03 2020

@author: Ioana
"""

class FA:
    def __init__(self):
        self.states=[]
        self.alphabet=[]
        self.initial = []
        self.final = []
        self.fa ={}
        self.readFromFile()

    def readFromFile(self):
        filename = "fa.txt"
        f = open(filename,"r")

        self.states = f.readline().split(" ")
        self.states[-1] = self.states[-1].strip("\n")

        self.alphabet = f.readline().split(" ")
        self.alphabet[-1] = self.alphabet[-1].strip("\n")

        self.initial = f.readline().split(" ")
        self.initial[-1] = self.initial[-1].strip("\n")
        if(len(self.initial)>1):
            print("Error! You can only have one initial state!")
            initial = self.initial[0]
            self.initial.clear()
            self.initial.append(initial)
            

        self.final = (f.readline().split(" "))
        self.final[-1] = self.final[-1].strip("\n")

        for line in f:
            elems=line[:-1].split(" ")
            if(len(elems)>2):
                self.fa[elems[0],elems[1]]=elems[2]
        

    def printMeniu(self):
        print()
        print("1 - Display states")
        print("2 - Display the alphabet")
        print("3 - Display initial state" )
        print("4 - Display final states")
        print("5 - Display transitions")
        print("0 - Exit")

    def displayStates(self):
        print("States:")
        for state in self.states:
            print(state)

    def displayAlphabet(self):
        print("The aplhabet:")
        for a in self.alphabet:
            print(a)

    def displayTransitions(self):
        print("Transitions:")
        for key in self.fa:
            print(key[0] + "->" + key[1] + ": " + self.fa[key[0],key[1]])

    def displayInititalState(self):
        print("Initial states:")
        for f in self.initial:
            print(f)

    def displayFinalStates(self):
        print("Final states:")
        for f in self.final:
            print(f)

    def start(self):
        com = -1
        while com != "0":
            self.printMeniu()
            com = input("Enter your command: ")
            if com == "1":
                self.displayStates()
            elif com == "2":
                self.displayAlphabet()
            elif com == "3":
                self.displayInititalState()
            elif com  == "4":
                self.displayFinalState()
            elif com == "5":
                self.displayTransitions()
            elif com == "0":
                print("Exit")
            else:
                print("Unknown command.Choose something from the menu")

fa = FA()
fa.start()

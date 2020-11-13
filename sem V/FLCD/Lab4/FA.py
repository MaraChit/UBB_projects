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
        self.dfa = True

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
                self.fa[elems[0],elems[1]]=(elems[2]).strip("\n")
                

    def printMeniu(self):
        print()
        print("1 - Display states")
        print("2 - Display the alphabet")
        print("3 - Display initial state" )
        print("4 - Display final states")
        print("5 - Display transitions")
        print("6 - Check sequence")
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

    def isDeterministic(self):
        visited = []
        for elem in self.fa:
            if elem[0] in visited:
                return False
            visited.append(elem[0])
        return True
    
    def verifySequence(self, sequence):
        
        if self.isDeterministic() == False:
            return False
        
        currentState = self.initial[0]
        lenSeq = len(sequence)
        ok = False
        
        for seq in sequence:
            ok = False
            for transition in self.fa.keys():
                if self.fa[transition] == seq and currentState == transition[0]:
                    ok = True
                    currentState = transition[1]
                    break
            if not ok:
                break
            else:
                lenSeq -= 1
                
        if currentState in self.final and lenSeq == 0:
            return True
        else:
            return False

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
            elif com== "6":
                print(fa.verifySequence("xyyx"))
                print(fa.verifySequence("xyy"))
                print(fa.verifySequence("xyyxyy"))
            else:
                print("Unknown command.Choose something from the menu")

fa = FA()
fa.start()

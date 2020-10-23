# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:45:06 2020

@author: Ioana
"""
import re
from hashtable import SymbolTable

class Scanner:
    
    def __init__(self, fileName):
        self.symbolTable = SymbolTable(10)
        self.programInternalForm = {}
        self.operators = ["Plus", "Minus", "Multiply", "Div", "Mod", "Equals", "Greater", "GreaterOrEqual",
                                "Smaller", "SmallerOrEqual", "EqualEqual", "Different"]
        self.separators = ['[', ']', '<', '>', ';', '(', ')', '"', " "]
        self.reservedWords = ["false", "true", "while", "int", "bool", "string",
                                    "get", "give", "start", "stop", "if", "else"]
        self.input = ""
        self.filename = fileName
        self.currentKeyPIF = 0
        
    def isConstant(self,token):
        if token[0] == 0 and len(token) != 1:
            return False
        for char in token:
            if char not in "1234567890":
                return False
        return True  
    
    def isValidIdentifier(self,token):
        print(token)
        if token[0] not in "qwertyuiopasdfghjklzxcvbnm":
            return False
        for char in token[1:]:
            if char not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890":
                return False
        return True
    
    def isSeparator(self,char):
        return char in self.separators

    def isOperator(self, token):
        return token in self.operators
    
    def isReservedWord(self, token):
        return token in self.reservedWords
    
    def detectTokens(self):
        return self.input.split()
        
    def classifyToken(self, tokenList, lineNo):
        for token in tokenList:
            tokens = re.split('<|>|;|\(|\)|\[|\]|\n|\t',token)
            for t in tokens:
                if t == '':
                    continue
                if self.isOperator(t):
                    self.programInternalForm[self.currentKeyPIF] = [t, -1]
                    self.currentKeyPIF += 1
                elif self.isReservedWord(t):
                    self.programInternalForm[self.currentKeyPIF] = [t, -1]
                    self.currentKeyPIF += 1
                elif self.isSeparator(t):
                    self.programInternalForm[self.currentKeyPIF] = [t, -1]
                    self.currentKeyPIF += 1
                elif self.isValidIdentifier(t):
                    if self.symbolTable.search(t) == -1:
                        poz = self.symbolTable.add(t)
                        self.programInternalForm[self.currentKeyPIF]=['Id', poz]
                        self.currentKeyPIF +=1
                    else:
                        poz = self.symbolTable.search(t)
                        self.programInternalForm[self.currentKeyPIF]=['Id', poz]
                        self.currentKeyPIF +=1
                elif self.isConstant(t):
                    if self.symbolTable.search(t) == -1:
                        poz = self.symbolTable.add(t)
                        print(poz)
                        self.programInternalForm[self.currentKeyPIF]=['Const', poz]
                        self.currentKeyPIF +=1
                    else:
                        poz = self.symbolTable.search(t)
                        self.programInternalForm[self.currentKeyPIF]=['Const', poz]
                        self.currentKeyPIF +=1
                else:
                    raise Exception("Lexical error found! Invalid token '"+ t +"'"+" at line "+ str(lineNo))
                        
    def scan(self):
        with open(self.filename, 'r') as file:
            lineNo = 0
            for line in file:
                lineNo = lineNo+1
                self.input = line
                tokenList = self.detectTokens()
                self.classifyToken(tokenList, lineNo)
                
        print(self.programInternalForm)
        print(self.symbolTable)
        

def testScan():
    scanner = Scanner("pb1_error.txt")
    scanner.scan()

        
  
testScan()                      
                
                
                
             
    
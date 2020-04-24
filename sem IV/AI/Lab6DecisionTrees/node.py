# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:19:37 2020

@author: Ioana
"""
class Node:
    
    def __init__(self, yesBranch, noBranch, split):
        '''
        constructor
        '''
        self.yesBranch = yesBranch
        self.noBranch = noBranch
        self.split = split
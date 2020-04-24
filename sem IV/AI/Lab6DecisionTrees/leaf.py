# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:38:19 2020

@author: Ioana
"""
class Leaf:
    
    def __init__(self, rows):
        self.predictions = self.count(rows)
        
    def count(self, rows):
        '''
        
        '''
        counts = {}
        for row in rows:
            i = row[-1]
            if i not in counts:
                counts[i]=0
            counts[i] = counts[i] + 1
        return counts

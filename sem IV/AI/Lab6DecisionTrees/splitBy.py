# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:00:25 2020

@author: Ioana
"""

class SplitBy:
    """
    class that defines splitting criteria
    """

    def __init__(self, col, value):
        '''
        constructor
        '''
        self.col = col
        self.value = value
        self.header = ['LW', 'LD', 'RW', 'RD', 'C']

    def chooseYesBranch(self, row):
        '''
        the Yes branch will be entered if the value from the column is greater or equal than the split value
        '''
        return row[self.col] >= self.value

    def __str__(self):
        
        return self.header[self.col] + ">=" + str(self.value)



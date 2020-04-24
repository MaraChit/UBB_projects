# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 21:23:57 2020

@author: Ioana
"""

class UI:
    def __init__(self, controller):
        self.controller = controller

    def run(self):
        self.controller.runAlg()
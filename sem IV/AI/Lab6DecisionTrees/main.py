# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 21:25:05 2020

@author: Ioana
"""
from controller import Controller
from repository import Repository
from ui import UI

def main():
    repository = Repository()
    controller = Controller(repository)
    ui = UI(controller)
    ui.run()
    
main()
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:13:20 2020

@author: Ioana
"""


import numpy as np
from matplotlib import pyplot as plt 

def normalDist():
    mu=int(input("Mean: "))
    sigma=float(input("Sigma: "))
    norm = np.random.normal(mu, sigma, 10000)
    count, bins, ignored = plt.hist(norm, 30, density=True)
    #plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)*2 / (2 * sigma*2) ), linewidth=3, color='b')
    plt.show()

def binomialDist():
    """
    n : int or array_like of ints ; n>=0
    p : float or array_like of floats ; 0<= p <= 1
    #size : int or tuple of ints, optional
    """
    n=int(input("n: "))
    p=float(input("p: "))
    size=int(input("size: "))
    bino=np.random.binomial(n, p,size)
    count, bins, ignored = plt.hist(bino, 30, density=True)
    plt.show()

def start():
    ok = True
    while ok== True:
        print("1.Normal")
        print("2.binomial")
        print("3. Exit")
        option = int(input("Option: "))
        if option == 1:
            normalDist()
        elif option == 2:
            binomialDist()
        elif option == 3:
            ok = False
            
start()
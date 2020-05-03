# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:24:19 2020

@author: Ioana
"""
import numpy as np
import matplotlib.pyplot as plt


def readFile():
    """
    reads from file,
    creates an X matrix with a column of 1 and one for each x
    creates (a one column)Y matrix with the y
    """
    f = open("database.txt", "r")
    x = []
    y = []
    for line in f:
        if line != "\n":
            inputValues = [float(value) for value in line.strip(" ").split(" ")]
            inputValues.insert(0, float(1))
            x.append(inputValues)
            realOutput = inputValues.pop()

            x[-1] = np.array(x[-1])

            y.append(realOutput)

    return np.array(x), np.array(y)


def gradientDescent(x, y, size, beta, alpha):
    """
    gradient descent method to find the coefficients
    returns the coefficients and the costs
    """

    costs = []
    coefficients = []
    predictions = []
    run = True
    minCost = 10000000
    costs.append(minCost)

    while run:
        prediction = np.dot(x, beta)
        predictions.append(prediction)

        error = prediction - y

        cost = 1 / size * np.dot(error.T, error)

        if cost < minCost:
            minCost = cost

        costs.append(cost)
        # print(cost)

        beta = beta - (alpha / size) * np.dot(x.T, error)

        coefficients.append(beta)

        if np.sqrt(cost) < 0.4:
            run = False

    return coefficients[-1], costs, minCost


def plotCosts(costs):
    '''
    plots graphic of cost evolution
    '''

    plt.title('Cost of the function')
    plt.xlabel('No. of iterations')
    plt.ylabel('Cost')
    plt.plot(costs)
    plt.show()


def main():
    '''
    read file
    '''
    x, y = readFile()

    '''
    Parameters required for Gradient Descent
    '''
    alpha = 0.0001  # learning rate
    size = len(y)  # no. of samples
    beta = np.random.rand(6)  # initializing beta with some random values

    beta, costs, minCost = gradientDescent(x, y, size, beta, alpha)

    print("The coefficients are:")
    print(beta)
    print("The minimum cost was:")
    print(minCost)
    plotCosts(costs)


main()

# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 12:26:13 2020

@author: Ioana
"""


import random
def shapes():
    lineShape = [(1,0),(1,0),(1,0)]
    lShape = [(0,1),(1,0),(1,0)]
    lRShape=[(1,0),(1,0),(0,1)]
    uShape=[(0,1),(1,0),(1,0),(0,-1)]
    tShape=[(1,-1),(0,1),(1,0)]
    return [lineShape,lShape,lRShape,uShape,tShape]

def shapesSize():
    lineSize=(3,0)
    lSize=(2,1)
    lRSize=(2,1)
    uSize=(2,1)
    tSize=(2,-1)
    return [lineSize,lSize,lRSize,uSize,tSize]

def shapeChr():
    return['-','l','r','u','t']

def initBoard():
    return [[0]*6, [0]*6, [0]*6, [0]*6, [0]*6]

def printBoard(board):
    s=""
    for row in board:
        for col in row:
            s+=str(col)+" "
        s+="\n"
    return s

def insertShape(board,shape,shapeSize, shapeChr, possibleCords):
    (x,y)=random.choice(possibleCords)
    while (x+shapeSize[0]>5 or y+shapeSize[1]>4):
        (x,y)=random.choice(possibleCords)
    possibleCords.remove((x,y))
    board[y][x] = shapeChr
    for coord in shape:
        x+=coord[0]
        y+=coord[1]
        if(x<0 or y<0):
            return 
        if board[y][x] == 0:
            board[y][x] = shapeChr
            possibleCords.remove((x,y))
        else:
            return
    return board

def boardTrial():
    board = initBoard()
    i = 0
    lshapesSize = shapesSize()
    chrs = shapeChr()
    possibleCords = []
    for i in range(6):
        for j in range(5):
            possibleCords.append((i,j))
    i=0
    for shape in shapes():
        if insertShape(board, shape, lshapesSize[i], chrs[i], possibleCords) == None:
            print("fail")
            return "fail"
        i+=1
    print(printBoard(board))
    

def main():
    n = int(input("Number of trials: "))
    while n>0:
        boardTrial()
        n=n-1
        
main()
from tkinter import *
from tkinter import messagebox
from Game import *
from Square import *

class GUI():
    def __init__(self):
        self.game=Game()
        self.Dobby=Tk()
        self.apa=[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8]
        self.apaInamic=[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8]
        self.deseneaza()

    def createButtonEU(self,i,j):
        stringvariable=StringVar()
        stringvariable.set("apa")
        button=Button(self.Dobby,textvariable=stringvariable,width=5,height=3)
        self.apa[i][j]=stringvariable
        button.grid(row=i,column=j)
    def createButton(self,i,j):
        stringvariable=StringVar()
        stringvariable.set("apa")
        button=Button(self.Dobby,textvariable=stringvariable,width=5,height=3,command=lambda:self.pressBt())
        self.apaInamic[i][j]=stringvariable
        button.grid(row=i,column=j+9)

    def pressBt(self):
        pass

    def deseneaza(self):
        for i in range (0,8):
            for j in range (0,8):
                self.createButtonEU(i,j)
        for i in range (0,8):
            for j in range (0,8):
                self.createButton(i,j)
        stringvariable=StringVar()
        stringvariable.set("vs")
        label=Label(self.Dobby,textvariable=stringvariable).grid(rowspan=8,column=8)
    def readMove(self):
        ok=0
        while ok==0:
            row=input("Give row(1-8)").strip()
            '''if row>='1' and row<='8':
                row=int(row)-1
                ok=1
            else:
                print("wrong row input")'''
            if row.isdigit():
                row=int(row)
                if row>=1 and row<=8:
                    row=row-1
                    ok=1
            else:
                print("wrong row input")
        OK=0
        while OK==0:
            col=input("Give col(a-h)").lower().strip()
            if col>='a' and col<='h':
                OK=1
                if col=='a':
                    col=0
                elif col=='b':
                    col=1
                elif col=='c':
                    col=2
                elif col=='d':
                    col=3
                elif col=='e':
                    col=4
                elif col=='f':
                    col=5
                elif col=='g':
                    col=6
                elif col=='h':
                    col=7
            else:
                print("wrong col input")

        return Square(row,col)
    def startGame(self):
        tabla=self.game.board
        tablacomp=self.game.compboard
        n=3
        while n:
            pr=self.readMove()
            ul=self.readMove()
            if tabla.placeShip(pr,ul)==True:
                n=n-1
        ##player-ul isi pune barcile
        self.game.ComputerPlacesShip()
        x=tablacomp.afisareTablaComputer()
        self.mainl()
    def mainl(self):
        mainloop()

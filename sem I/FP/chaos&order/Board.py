from texttable import Texttable
from Square import Square
import copy

class Board:
    def __init__(self):
        self._tabla=[[0]*6,[0]*6,[0]*6,[0]*6,[0]*6,[0]*6]

    def copy(self):
        b=Board()
        b._tabla=copy.deepcopy(self._tabla)
        return b

    def drawBoard(self):
    #def __str__(self):
        t=Texttable()
        d={0:" ",1:"x",2:"o"}
        for i in range (0,6):
            list=self._tabla[i][:]
            for j in range (0,6):
                list[j]=d[list[j]]
            t.add_row(list)
        return t.draw()

    def getEmptySquare(self):
        l=[]
        for i in range (0,6):
            for j in range (0,6):
                if self._tabla[i][j]==0:
                    l.append(Square(i,j))
        return l

    def Winn(self):
        b=self._tabla
        '''for i in [0,1,2,3,4,5]:
            if b[i][0]*b[i][1]*b[i][2]*b[i][3]*b[i][4]==1 or b[i][5]*b[i][1]*b[i][2]*b[i][3]*b[i][4]==1 or b[i][0]*b[i][1]*b[i][2]*b[i][3]*b[i][4]==32 or b[i][5]*b[i][1]*b[i][2]*b[i][3]*b[i][4]==32:
                return True
        for i in range(0,6):
            for j in range(0,2):
                p=1
                for c in range(0,5):
                    p*=b[i][j+c]
                if p==1 or p==32:
                    return True'''
        for i in [0,1,2,3,4,5]:
            if b[i][0]*b[i][1]*b[i][2]*b[i][3]*b[i][4] in [1,32] or b[i][5]*b[i][1]*b[i][2]*b[i][3]*b[i][4] in [1,32]: #vf linie
                return True
                '''
                verifica daca sunt 5 la fel pe linie
                '''
            if b[0][i]*b[1][i]*b[2][i]*b[3][i]*b[4][i] in [1,32] or b[5][i]*b[1][i]*b[2][i]*b[3][i]*b[4][i] in [1,32]:
                return True
                '''
                verifica daca sunt 5 in coloana
                '''
        for i in range (0,2):
            for j in range (0,2):
                p=1
                for k in range (0,5):
                    p*=b[i+k][j+k]
                if p==1 or p==32:
                    return True
        '''
        vf diagonala din stanga spre dreapta
        '''
        for i in range (0,2):
            for j in range (4,6):
                p=1
                for k in range (0,5):
                    p*=b[i+k][j-k]
                if p==1 or p==32:
                    return True
        '''
        vf diagonl din dr
        '''
        return False

    def ComputerWin(self):
        l=self.getEmptySquare()
        if l==[]:
            return True
        return False

    def Move(self,m,symbol):
        if self._tabla[m.row][m.col]==0:
            if symbol=='x':
                self._tabla[m.row][m.col]=1
                return 1
            if symbol=='o':
                self._tabla[m.row][m.col]=2
                return 1
        else:
            print("invalid move, square already full")
            return 0

from texttable import Texttable
from Square import Square
class Board():
    def __init__(self):
        'repr the board'
        self.tabla=[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8]
        self.cnt=9
        self.ok2=0
        self.ok3=0
        self.ok4=0

    def getEmptyS(self):#empty spaces+spaces where ships can be hit
        empty=[]
        for i in range(0,8):
            for j in range (0,8):
                if self.tabla[i][j]==0 or self.tabla[i][j]==1:
                    empty.append(Square(i,j))

        return empty

    def Win(self):
        if self.cnt==0:
            return True
        else :
            return False

    def placeShip(self,pr,ul):
        if pr.col==ul.col:
            if pr.row>ul.row:
                aux=pr.row
                pr.setrow(ul.row)
                ul.setrow(aux)
            n=ul.row-pr.row+1
            if n!=2 and n!=3 and n!=4:
                print (n)
                print (ul.row)
                print (pr.row)
                print('wrong input;incorect number of squares')
                return False
            elif n==2:
                if self.ok2==0:
                    for i in range (pr.row,ul.row+1):
                        if self.tabla[i][pr.col]==1:
                            return False
                    self.ok2=1
                    for i in range (pr.row,ul.row+1):
                        self.tabla[i][pr.col]=1
                    return True
                else:
                    return False
                    print("you already have a ship with 2 squares")
            elif n==3:
                if self.ok3==0:
                    for i in range (pr.row,ul.row+1):
                        if self.tabla[i][pr.col]==1:
                            return False
                    self.ok3=1
                    for i in range (pr.row,ul.row+1):
                        self.tabla[i][pr.col]=1
                    return True
                else:
                    return False
                    print("you already have a ship with 3 squares")
            else:
                if self.ok4==0:
                    for i in range (pr.row,ul.row+1):
                        if self.tabla[i][pr.col]==1:
                            return False
                    self.ok4=1
                    for i in range (pr.row,ul.row+1):
                        self.tabla[i][pr.col]=1
                    return True
                else:
                    return False
                    print("you already have a ship with 4 squares")
        elif pr.row==ul.row:
            if pr.col>ul.col:
                aux=pr.col
                pr.setcol(ul.col)
                ul.setcol(aux)
            n=ul.col-pr.col+1
            if n!=2 and n!=3 and n!=4:
                print('wrong input;incorect number of squares')
                return False
            elif n==2:
                if self.ok2==0:
                    for i in range (pr.col,ul.col+1):
                        if self.tabla[pr.row][i]==1:
                            return False
                    self.ok2=1
                    for i in range (pr.col,ul.col+1):
                        self.tabla[pr.row][i]=1
                    return True
                else:
                    return False
                    print("you already have a ship with 2 squares")
            elif n==3:
                if self.ok3==0:
                    for i in range (pr.col,ul.col+1):
                        if self.tabla[pr.row][i]==1:
                            return False
                    self.ok3=1
                    for i in range (pr.col,ul.col+1):
                        self.tabla[pr.row][i]=1
                    return True
                else:
                    return False
                    print("you already have a ship with 3 squares")
            else:
                if self.ok4==0:
                    for i in range (pr.col,ul.col+1):
                        if self.tabla[pr.row][i]==1:
                            return False
                    self.ok4=1
                    for i in range (pr.col,ul.col+1):
                        self.tabla[pr.row][i]=1
                    return True
                else:
                    return False
                    print("you already have a ship with 4 squares")
        else:
            print ("wrong input")
            return False

    def placeShipForComp(self,pr,ul):
        if pr.col==ul.col:
            if pr.row>ul.row:
                aux=pr.row
                pr.setrow(ul.row)
                ul.setrow(aux)
            n=ul.row-pr.row+1
            if n!=2 and n!=3 and n!=4:
                return False
            elif n==2:
                if self.ok2==0:
                    for i in range (pr.row,ul.row+1):
                        if self.tabla[i][pr.col]==1:
                            return False
                    self.ok2=1
                    for i in range (pr.row,ul.row+1):
                        self.tabla[i][pr.col]=1
                    return True
                else:
                    return False
            elif n==3:
                if self.ok3==0:
                    for i in range (pr.row,ul.row+1):
                        if self.tabla[i][pr.col]==1:
                            return False
                    self.ok3=1
                    for i in range (pr.row,ul.row+1):
                        self.tabla[i][pr.col]=1
                    return True
                else:
                    return False
            else:
                if self.ok4==0:
                    for i in range (pr.row,ul.row+1):
                        if self.tabla[i][pr.col]==1:
                            return False
                    self.ok4=1
                    for i in range (pr.row,ul.row+1):
                        self.tabla[i][pr.col]=1
                    return True
                else:
                    return False
        elif pr.row==ul.row:
            if pr.col>ul.col:
                aux=pr.col
                pr.setcol(ul.col)
                ul.setcol(aux)
            n=ul.col-pr.col+1
            if n!=2 and n!=3 and n!=4:
                return False
            elif n==2:
                if self.ok2==0:
                    for i in range (pr.col,ul.col+1):
                        if self.tabla[pr.row][i]==1:
                            return False
                    self.ok2=1
                    for i in range (pr.col,ul.col+1):
                        self.tabla[pr.row][i]=1
                    return True
                else:
                    return False
            elif n==3:
                if self.ok3==0:
                    for i in range (pr.col,ul.col+1):
                        if self.tabla[pr.row][i]==1:
                            return False
                    self.ok3=1
                    for i in range (pr.col,ul.col+1):
                        self.tabla[pr.row][i]=1
                    return True
                else:
                    return False
            else:
                if self.ok4==0:
                    for i in range (pr.col,ul.col+1):
                        if self.tabla[pr.row][i]==1:
                            return False
                    self.ok4=1
                    for i in range (pr.col,ul.col+1):
                        self.tabla[pr.row][i]=1
                    return True
                else:
                    return False
        else:
            return False

    def Move(self,hit):
        if self.tabla[hit.row][hit.col]!=2 and self.tabla[hit.row][hit.col]!=3:
            if self.tabla[hit.row][hit.col]==1:
                self.tabla[hit.row][hit.col]=3
                self.cnt=self.cnt-1
                return 10
            else:
                self.tabla[hit.row][hit.col]=2
                return -1
        else:
            print("Spot already hit")
            return 0

    def __str__(self):
        t=Texttable()
        d={0:" ",1:"s",2:"X",3:"o"} #x apare unde a lovit calculatorul barca si nu a nimerit
        for i in range (0,8):
            list=self.tabla[i][:]
            for j in range (0,8):
                list[j]=d[list[j]]
            t.add_row(list)
        return t.draw()

    def afisareTablaComputer(self):
        t=Texttable()
        d={0:" ",1:"h",2:"X",3:"o"} #o apare unde a lovit player-ul pe tabla computerului si a nimerit
        for i in range (0,8):
            list=self.tabla[i][:]
            for j in range (0,8):
                list[j]=d[list[j]]
            t.add_row(list)
        return t.draw()

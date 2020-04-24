from Board import Board
from Square import Square
from random import randint,choice

class Game():
    def __init__(self):
        self._board=Board()
        self._compboard=Board()
        self.prevhit=0
        self.direction=1 #1-jos,2-sus,3-dreapta,4-stanga
        self.cub=Square(0,0)
        self.reper=Square(0,0)
        self.schimba=0 #vf daca a putut face miscarea;daca da, schimba directia in aceeasi tura

    @property
    def board(self):
        return self._board

    def moveHuman(self,hit):
        ok=self._compboard.Move(hit)
        return ok

    def moveComputer(self):
        options=self._board.getEmptyS()
        if self.prevhit==0:
            hit=choice(options)
            if self._board.Move(hit)==10:
                self.prevhit=1
                self.cub=hit
                self.reper=self.cub
        else:
            #loveste jos,sus,stanga,dreapta
            #self.reper=self.cub
            self.schimba=0
            while self.schimba==0:
                if self.direction==1:
                    if self.reper.row<7:
                        hit=Square(self.reper.row+1,self.reper.col)
                        if cauta(options,hit)==True:
                            lovitura=self._board.Move(hit)
                            self.schimba=1
                            if lovitura==-1:
                                self.direction=2
                                self.reper=self.cub
                            elif lovitura==10:
                                self.reper=hit
                        else:
                            self.direction=2
                            self.reper=self.cub
                    else:
                        self.direction=2
                        self.reper=self.cub
                elif self.direction==2:
                    if self.reper.row>0:
                        hit=Square(self.reper.row-1,self.reper.col)
                        if cauta(options,hit)==True:
                            lovitura=self._board.Move(hit)
                            self.schimba=1
                            if lovitura==-1:
                                self.direction=3
                                self.reper=self.cub
                            elif lovitura==10:
                                self.reper=hit
                        else:
                            self.direction=3
                            self.reper=self.cub
                    else:
                        self.direction=3
                        self.reper=self.cub
                elif self.direction==3:
                    if self.reper.col<7:
                        hit=Square(self.reper.row,self.reper.col+1)
                        if cauta(options,hit)==True:
                            lovitura=self._board.Move(hit)
                            self.schimba=1
                            if lovitura==-1:
                                self.direction=4
                                self.reper=self.cub
                            elif lovitura==10:
                                self.reper=hit
                        else:
                            self.direction=4
                            self.reper=self.cub
                    else:
                        self.direction=4
                        self.reper=self.cub
                elif self.direction==4:
                    if self.reper.col>0:
                        hit=Square(self.reper.row,self.reper.col-1)
                        if cauta(options,hit)==True:
                            lovitura=self._board.Move(hit)
                            self.schimba=1
                            if lovitura==-1:
                                self.direction=1
                                self.prevhit=0
                            elif lovitura==10:
                                self.reper=hit
                        else:
                            self.direction=1
                            self.prevhit=0
                            hit=choice(options)
                            if self._board.Move(hit)==10:
                                self.prevhit=1
                                self.cub=hit
                    else:
                        self.direction=1
                        self.prevhit=0
                        hit=choice(options)
                        if self._board.Move(hit)==10:
                            self.prevhit=1
                            self.cub=hit


    @property
    def compboard(self):
        return self._compboard

    def ComputerPlacesShip(self):
        n=3
        while n:
            pr=Square(0,0)
            ul=Square(0,0)
            pr.setcol(randint(0,7))
            pr.setrow(randint(0,7))
            ok=randint(0,1)
            if ok==0:
                ul.setcol(pr.col)
                ul.setrow(randint(0,7))
            else:
                ul.setcol(randint(0,7))
                ul.setrow(pr.row)
            if self._compboard.placeShipForComp (pr,ul)==True:
                n=n-1


def cauta(l,hit):
    for i in l:
        if i.row==hit.row and i.col==hit.col:
            return True
    return False

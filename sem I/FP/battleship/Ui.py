from Square import *
class Ui():
    def __init__(self,game):
        self.game=game

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

    def start(self):
        tabla=self.game.board
        tablacomp=self.game.compboard
        n=3
        while n:
            pr=self.readMove()
            ul=self.readMove()
            if tabla.placeShip(pr,ul)==True:
                n=n-1
            print(tabla)
        ##player-ul isi pune barcile
        self.game.ComputerPlacesShip()
        x=tablacomp.afisareTablaComputer()
        print (x)
        ##computerul isi pune barcile
        while tabla.Win()!=True or tablacomp.Win()!=True:
            ok=0
            while ok==0:
                hit=self.readMove()
                ok=self.game.moveHuman(hit)
            x=tablacomp.afisareTablaComputer()
            print(x)
            if tablacomp.Win():
                print('you won!!!')
                break
            else:
                self.game.moveComputer()
                print (tabla)
                if tabla.Win():
                    print("computer won :(")
                    break

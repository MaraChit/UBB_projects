from Game import Game
from Board import Board
from Square import Square

class UI:
    def __init__(self, game):
        self._game=game

    def inputMove(self):
        ok=1
        while ok==1:
            row=input("Give row(1-6)").strip()
            if row.isdigit():
                row=int(row)
                if row>=1 and row<=6:
                    row=row-1
                    ok=0
            else:
                print("Wrong input for row")
        ok=1
        while ok==1:
            ok=0
            col=input("Give col(a-f)").strip().lower()
            if col>='a' and col<='h':
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
            else:
                print("wrong col input")
                ok=1

        return Square(row,col)

    def start(self):
        board=self._game.board
        print(board.drawBoard())
        while board.Winn()==False and board.ComputerWin()==False:
            ok=0
            while ok==0:
                m=self.inputMove()
                i=0
                while i==0:
                    symbol=input('Choose x or o').strip().lower()
                    if symbol=='o'or symbol=='x':
                        i=1
                    else:
                        print ("wrong symbol")
                ok=self._game.moveHuman(m,symbol)
            board=self._game.board
            print(board.drawBoard())
            if board.Winn()==True:
                print("You won!!!")
            else:
                self._game.moveComputer()
                board=self._game.board
                print(board.drawBoard())
                if board.ComputerWin()==True:
                    print("You loose")

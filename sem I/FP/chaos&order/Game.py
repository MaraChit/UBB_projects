from Board import Board
from Square import Square
from random import choice

class Game:
    def __init__(self):
        self._board=Board()

    @property
    def board(self):
        return self._board

    def moveHuman(self,m,symbol):
        ok=self._board.Move(m,symbol)
        return ok

    def moveComputer(self):
        options=self._board.getEmptySquare()
        ok=1
        for option in options:
            b=self.board.copy()
            b.Move(option,'x')
            if b.Winn()==True:
                self._board.Move(option,'o')
                ok=0
        if ok==1:
            for option in options:
                b=self.board.copy()
                b.Move(option,'o')
                if b.Winn()==True:
                    self._board.Move(option,"x")
                    ok=0
        if ok==1:
            s=choice(options)
            symbol=choice(['x','o'])
            self._board.Move(s,symbol)

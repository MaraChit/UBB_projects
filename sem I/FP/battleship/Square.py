class Square():
    'a square on the board'
    def __init__(self,row,col):
        self._row = row
        self._col = col

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    def setcol(self,new):
        self._col=new

    def setrow(self,new):
        self._row=new

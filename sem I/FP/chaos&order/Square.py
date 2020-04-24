class Square:
    def __init__(self,row,col):
        self._row=row
        self._col=col

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col
        

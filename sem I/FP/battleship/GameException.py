class GameException(Exception):
    def __init__(self,m):
        self._msg=m

    @property
    def message(self):
        return self._msg

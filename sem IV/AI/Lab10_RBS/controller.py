from capacity import Capacity
from ruler import Ruler
from texture import Texture

class Controller:
    
    def __init__(self, texture, capacity):
        
        self.rules = Ruler()
        self.texture = Texture(texture)
        self.capacity = Capacity(capacity)
        
    def writeData(self, data):
        f = open("output.txt", "a")
        f.write(data)
        f.write(" ")
        f.close()

    def solve(self):
        
        result = self.rules.evaluate(self.texture, self.capacity)
        
        #print(result)
         #print(sorted(list(result.items()), key = lambda x: x[1])[-1][0])
        data = sorted(list(result.items()), key = lambda x: x[1])[-1][0]
        self.writeData(data)
        print(data)
       

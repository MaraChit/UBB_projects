from Repository import Repository
from UI import UI
from Graph import Graph

operations = Repository()
ui = UI(operations)
ui.start()



"""grap=Graph.randomGraph(10,5)

#grap=Graph.loadFile()
print(grap)

grap.DFS()"""

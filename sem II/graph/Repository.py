from Graph import Graph

class Repository:
    def __init__(self):
        self.__graph = None

    def load_file(self,file_name="file_name.txt"):
        file = open(file_name,"r")
        text = file.read()
        text = text.split('\n')
        line = text[0]
        line = line.split(" ")
        del text[0]
        try:
            n = int(line[0])
            m = int(line[1])
        except:
            raise ValueError("Invalid file input!")
        self.__graph = Graph(n)
        for i in range(m):
            line = text[i].split(" ")
            if len(line) != 3:
                raise ValueError("Invalid file input")
            origin = int(line[0])
            target = int(line[1])
            cost = int(line[2])
            if origin>=n or target>=n:
                raise ValueError("Invalid file input!")

            self.__graph.add_edge(origin, target, cost)

    def find_edge(self, origin,target):
        return self.__graph.find_edge((origin,target))

    def get_nr_vertices(self):
        return self.__graph.get_vertices()

    def degreeVertex(self,vertex):
        return self.__graph.degree_vertex(vertex)

    def parseVertices(self):
        return self.__graph.parse_vertices()

    def parseOutbound(self,vertex):
        return self.__graph.parse_outbound(vertex)

    def parseInbound(self,vertex):
        return self.__graph.parse_inbound(vertex)

    def getCost(self,edge):
        return self.__graph.get_cost(edge)

    def setCost(self,edge,cost):
        return self.__graph.set_cost(edge, cost)

    def addVertex(self,vertex):
        return self.__graph.add_vertex(vertex)

    def removeVertex(self,vertex):
        return self.__graph.remove_vertex(vertex)

    def addEdge(self,origin,target,cost):
        return self.__graph.add_edge(origin, target, cost)

    def removeEdge(self,edge):
        return self.__graph.remove_edge(edge)

    def copyGraph(self):
        return self.__graph.copy()

    def getGraph(self):
        return self.__graph

    def BelmannFord(self,s,e):
        return self.__graph.BelmannFord(s,e)

    def DAG(self):
        return self.__graph.DAG()

    def timeActivity(self):
        return self.__graph.timeActivity()

    def Hamilton(self):
         return self.__graph.Hamilton()

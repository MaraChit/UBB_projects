class UI:
    def __init__(self,repo):
        self.__repository = repo

    @staticmethod
    def printMenu():
        print(" ")
        print("1. Print graph")
        print("2. Load file")
        print("3. Get the number of vertices")
        print("4. Parse the set of vertices")
        print("5. Find if there is an edge")
        print("6. Get in degree of vertex")
        print("7. Get out degree of vertex")
        print("8. Parse the set of outbound edges of vertex")
        print("9. Parse the set of inbound edges of vertex")
        print("10. Get the cost of an edge ")
        print("11. Change the cost")
        print("12. Add edge")
        print("13. Remove edge")
        print("14. Add vertex")
        print("15. Remove vertex")
        print("16. Exit")
        print("17. BF cost")
        print("18. DAG")
        print("19. timeActivity")
        print("20. Hamilton")
        print(" ")

    def printGraph(self):
        print(self.__repository.getGraph())

    def loadFile(self):
        filename = "file_name.txt"
        self.__repository.load_file(filename)
        print("File loaded!")

    def getVertices(self):
        print("The number of vertices is:" + str(self.__repository.get_nr_vertices()))

    def parseVertices(self):
        print(self.__repository.parseVertices())

    def findEdge(self):
        origin = int(input("Origin of the edge: "))
        target = int(input("Target of the edge: "))
        print(self.__repository.find_edge(origin,target))

    def get_in_degree(self):
        vertex = int(input("Number of vertex: "))
        print("The in degree is "+ str(self.__repository.degreeVertex(vertex)[0]))

    def get_out_degree(self):
        vertex = int(input("Number of vertex: "))
        print("The out degree is "+ str(self.__repository.degreeVertex(vertex)[1]))

    def parse_out(self):
        vertex = int(input("Number of vertex: "))
        l = self.__repository.parseOutbound(vertex)
        for i in range (0,len(l)):
            print(l[i])

    def parse_in(self):
        vertex = int(input("Number of vertex: "))
        l = self.__repository.parseInbound(vertex)
        for index in range (0,len(l)):
            print(l[index])
        if len(l)==0:
            print("Empty")


    def get_cost(self):
        origin = int(input("Origin of the edge: "))
        target = int(input("Target of the edge: "))
        edge = (origin,target)
        if self.__repository.getCost(edge) == None:
            print("The edge does not exist")
        else:
            print("Cost: "+str(self.__repository.getCost(edge)))

    def change_cost(self):
        origin = int(input("Origin of the edge: "))
        target = int(input("Target of the edge: "))
        cost = int(input("New cost:"))
        edge = (origin,target)

        valid = self.__repository.setCost(edge,cost)

        if valid == False:
            print("The edge does not exist")
        else:
            print("Cost changed!")

    def add_edge(self):
        origin = int(input("Origin of the edge: "))
        target = int(input("Target of the edge: "))
        cost = int(input("New cost:"))

        valid = self.__repository.addEdge(origin,target,cost)

        if valid == False:
            print("The origin/target does not exist")

    def remove_edge(self):
        origin = int(input("Origin of the edge: "))
        target = int(input("Target of the edge: "))
        edge=(origin,target)

        valid = str(self.__repository.removeEdge(edge))

        if valid == False:
            print("The edge does not exist")

    def add_vertex(self):
        vertex = int(input("Number of vertex: "))

        valid = self.__repository.addVertex(vertex)

        if valid == False:
            print("The vertex already exists")

    def remove_vertex(self):
        vertex = int(input("Number of vertex: "))

        valid = self.__repository.removeVertex(vertex)

        if valid == False:
            print("The vertex does not exist")

    def copy_graph(self):
        g = self.__repository.getGraph()
        self.__repository.copyGraph()

    def start(self):
        while True:
            try:
                sdnfsjds=input("Press any key to continue...")
                self.printMenu()
                command = int(input("Enter an option: "))
                if command == 1:
                    self.printGraph()
                elif command ==2:
                    self.loadFile()
                elif command ==3:
                    self.getVertices()
                elif command ==4:
                    self.parseVertices()
                elif command ==5:
                    self.findEdge()
                elif command ==6:
                    self.get_in_degree()
                elif command ==7:
                    self.get_out_degree()
                elif  command ==8:
                    self.parse_out()
                elif command ==9:
                    self.parse_in()
                elif command ==10:
                    self.get_cost()
                elif command ==11:
                    self.change_cost()
                elif command ==12:
                    self.add_edge()
                elif command ==13:
                    self.remove_edge()
                elif command ==14:
                    self.add_vertex()
                elif command ==15:
                    self.remove_vertex()
                #elif command ==18:
                #    pass
                    #self.copy_graph()
                elif command ==16:
                    break
                elif command ==17:
                    s=int(input ("Start vertex: "))
                    e=int(input("End vertex: "))
                    print(self.__repository.BelmannFord(s,e))
                elif command==18:
                    #print("BLA")
                    sortedDAG = self.__repository.DAG()
                    if sortedDAG != []:
                        print(sortedDAG)
                        print("Done computing topological sorting with dfs.")
                    else:
                        print("Graph is not DAG")
                elif command==19:
                        print(self.__repository.timeActivity())
                elif command==20:
                        self.__repository.Hamilton()
                else:
                    print("Invalid option")
            except Exception as e:
                print(e)

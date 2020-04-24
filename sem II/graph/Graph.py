from random import randint
import itertools

class Graph:
    def __init__(self, nrOfVertices):
        """
        Constructor for the directed graph using dictionary

        """
        self.__nr_vertices = nrOfVertices
        self.__out = {}
        self.__in = {}
        self.__cost = {}
        for i in range(nrOfVertices):
            self.__out[i] = []
            self.__in[i] = []


    def get_vertices(self):
        """
        Returns the number of vertices
        """
        return self.__nr_vertices

    def parse_vertices(self):
        """
        Parses the vertices
        Returns all vertices
        """
        return self.__out.keys()

    def find_edge(self,edge):
        """
        Finds if an edge exists
        Input: an edge
        Output: true- if the edge exists
                false - otherwise
        """
        if edge in self.__cost.keys():
            return True
        return False

    def degree_vertex(self,vertex):
        """
        Returns the in and out degree of a vertex
        None if the vertex does not exist
        """
        if vertex in self.__in.keys():
            return [len(self.__in[vertex]),len(self.__out[vertex])]
        return None

    def parse_outbound(self,vertex):
        """
        Returns the outbound vertices of a vertex
        Input: vertex
        """

        if vertex in self.__out.keys():
            return self.__out[vertex]

    def parse_inbound(self,vertex):
        """
        Returns the inbound vertices of a vertex
        Input: vertex
        """
        if vertex in self.__in.keys():
            return self.__in[vertex]


    def get_cost(self,edge):
        """
        Returns the cost of an edge
        Input: an edge
        Output: the cost of the edge
                none if the edge doesn't exist
        """
        if edge in self.__cost.keys():
            return self.__cost[edge]
        return None

    def set_cost(self,edge,new_cost):
        """
        Modifies the cost of an edge
        Input: edge and the new cost
        Output: true- if the cost is modified
                false otherwise
        """
        if edge in self.__cost.keys():
            self.__cost[edge] = new_cost
            return True
        return False


    def add_vertex(self,vertex):
        """
        Adds a vertex to the graph
        Input: vertex- the vertex to be added
        Output: true if the vertex is added
                false if the vertex already exists
        """
        if vertex in self.__in.keys():
            return False
        self.__nr_vertices +=1
        self.__in[vertex] = []
        self.__out[vertex] = []
        return True

    def remove_vertex(self,vertex):
        """
        Removes a vertex from the graph
        Input: vertex
        Output: true if the vertex is deleted
                false if the vertex does not exists
        """
        if vertex not in self.__in.keys():
            return False
        list = []
        for edge in self.__cost.keys():
            if vertex in edge:
                list.append(edge)
        for edge in list:
            self.remove_edge(edge)
            #del self.__cost[edge]
        del self.__in[vertex]
        del self.__out[vertex]
        self.__nr_vertices -= 1
        return True

    def add_edge(self,start,end,cost):
        """
        Adds an edge to the graph
        Input: start- the start of the edge
               end - the end of the edge
               cost - the cost of the edge
        Output: true - if the edge is added
                false - if start/end doesn't exist or the edge already exists
        """
        if start not in self.__in.keys():
            return False
        if end not in self.__out.keys():
            return False
        if (start,end) not in self.__cost.keys():
            self.__out[start].append(end)
            self.__in[end].append(start)
            self.__cost[(start,end)] = cost
            return True
        return False

    def remove_edge(self,edge):
        """
        Removes an edge from the graph
        Input: edge
        Output: false if the edge does not exist
                true if the edge is deleted
        """
        start = edge[0]
        end = edge[1]
        if edge not in self.__cost.keys():
            return False
        self.__out[start].remove(end)
        self.__in[end].remove(start)
        del self.__cost[edge]
        return True

    def copy(self):
        """
        Creates a deep copy of the graph
        returns: copy of the graph
        """
        g = Graph(self.__nr_vertices)
        for edge in self._cost.keys():
            g.append(edge[0],edge[1], self.__cost[edge])
        return g


    def __str__(self):
        """
        Print for the graph
        """
        message = "The number of vertices is: "+ str(self.__nr_vertices)+"\n"
        message+= "The edges are: " + "\n"
        for i in self.__cost.keys():
            message+= str(i)+ "->"+ str(self.__cost[i])+"\n"
        return message

    @staticmethod
    def randomGraph(nr_vertices,nr_edges):
        """
        Creates a random graph.
        input: nr_vertices = number of nr_vertices
               nr_edges = number of nr_edges
        returns: random graph
        """
        graph=Graph(nr_vertices)
        while nr_edges !=0 :
            start=randint(0,nr_vertices-1)
            end=randint(0,nr_vertices-1)
            cost=randint(0,500)
            if graph.add_edge(start,end,cost)==True:
                nr_edges-=1

        return graph

    def DFS_recursiv(self,actual,visited,comp):
        """
        Modifies values for visited and comp.
        input:
            actual: actual vertex
            visited: list with visited vertices
            comp: list with visited vertices for a new conex component
        """

        for i in self.parse_inbound(actual):
            if i not in visited:
                visited.append(i)
                comp.append(i)
                self.DFS_recursiv(i,visited,comp)
        for i in self.parse_outbound(actual):
            if i not in visited:
                visited.append(i)
                comp.append(i)
                self.DFS_recursiv(i,visited,comp)

    def DFS(self):
        """
        output: result = list of lists with the connected components of the graph
        """
        visited=[]
        result=[]
        nr_comp_conex=0
        for i in range(0,self.__nr_vertices):
            if i not in visited:
                l=[i]
                visited.append(i)
                self.DFS_recursiv(i,visited,l)
                nr_comp_conex+=1
                result.append(l)

        print(result)

    def BelmannFord(self,source,end):
        distance=dict()
        #predecessor=dict()
        inf=999999
        edges=list()
        next=dict()

        for v in self.parse_vertices():
            for vert in self.parse_outbound(v):
                edges.append((v,vert))

        for vertex in self.parse_vertices():
            if vertex==source: distance[vertex]=0
            else: distance[vertex]=inf;
            next[vertex]=None

        for i in range (1,len(self.parse_vertices())-1):
            for edge in edges:
                if distance[edge[1]]>distance[edge[0]]+self.get_cost((edge[0],edge[1])):
                    distance[edge[1]]=distance[edge[0]]+self.get_cost((edge[0],edge[1]))
                    next[edge[1]]=edge[0]
            #print(distance)


        for edge in edges:
            if distance[edge[1]] > distance[edge[0]] + self.get_cost((edge[0], edge[1])):
                raise Exception("Negative cost cycles\n")

        print(next)

        return distance[end]

    def topologicalSortWithDFS(self, x, sorted, fullyProcessed, inProcess):
        '''
        Function that sorts topologically the vertices
        Returns True if the vertex X was added to the sorted list and the fullyProcessed set
                False otherwise
        '''
        inProcess.add(x)
        for inboundNeighbour in self.parse_inbound(x):
            if inboundNeighbour in inProcess:
                return False
            else:
                if inboundNeighbour not in fullyProcessed:
                    ok = self.topologicalSortWithDFS(inboundNeighbour, sorted, fullyProcessed, inProcess)
                    if not ok:
                        print(sorted)
                        return False
        inProcess.remove(x)
        sorted.append(x)
        fullyProcessed.add(x)
        return True

    def DAG(self):
        """
        verifies if a graph is a DAG
        returns empty list if it's not a DAG
                topologically sorted list otherwise
        """
        sorted = []
        fullyProcessed = set()
        inProcess = set()
        for vertex in self.parse_vertices():
            if vertex not in fullyProcessed:
                ok = self.topologicalSortWithDFS(vertex, sorted, fullyProcessed, inProcess)
                if not ok:
                    return []
        return sorted[:]

    def timeActivity(self):
        """
        returns the earliest and the latest starting time for each activity and the critical activities
        """
        earlyStart=dict()
        earlyFinish = dict()

        sorted=self.DAG()
        duration={0:5, 1:3, 2:1, 3:0}

        for node in sorted:
            earlyStart[node]=0;
            for i in self.parse_inbound(node):
                earlyStart[node]=max(earlyStart[node],earlyStart[i]+duration[i])
            earlyFinish[node]=earlyStart[node]+duration[node]


        totalTime=0
        for x in self.parse_vertices():
            if earlyFinish[x]>totalTime:
                totalTime=earlyFinish[x]

        lateStart = dict()
        lateFinish = dict()

        for node in reversed(sorted):
            lateFinish[node]=totalTime
            for y in self.parse_outbound(node):
                lateFinish[node]=min(lateFinish[node],lateStart[y])
            lateStart[node]=lateFinish[node]-duration[node]


        critical=[]
        for x in self.parse_vertices():
            if lateStart[x]==earlyStart[x] and lateFinish[x]==earlyFinish[x]:
                critical.append(x)

        return { "earliest start ": earlyStart, "earliest finish ": earlyFinish, "total time": totalTime,
                 "latest start": lateStart,"late finish": lateFinish, "critical": critical }

    def Hamilton(self):
        list=[]
        minim=100000
        rezult=[]

        for x in self.parse_vertices():
            list.append(x)

        #for i in range(len(list)+1):
        for j in itertools.combinations(list,len(list)):
            #print (j)
            ok=True
            sum=0
            if len(j)>2:
                for k in range(0,len(j)-1):
                    if self.find_edge((j[k],j[k+1]))==False and self.find_edge((j[k+1],j[k]))==False:
                        ok=False

                if self.find_edge((j[0],j[len(j)-1]))==False and self.find_edge((j[len(j)-1],j[0]))==False:
                     ok=False
                #print(ok)
                #print(j)
                if ok==True:
                    for k in range(0,len(j)-1):
                        if self.find_edge((j[k],j[k+1]))==True:
                            sum=sum+self.get_cost((j[k],j[k+1]))
                        else:
                            sum=sum+self.get_cost((j[k+1],j[k]))
                    if self.find_edge((j[0],j[len(j)-1]))==True:
                        sum=sum+self.get_cost((j[0],j[len(j)-1]))
                    else:
                        sum=sum+self.get_cost((j[len(j)-1],j[0]))

                    if sum<minim:
                        minim=sum
                        rezult=j
                            #print(j)
        #rezult.append(rezult[0])
        print(rezult)
        print(minim)

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Graph {
    /*
    nodesNumber : int representing the number of nodes in the graph
    nodes: map with (key, value) pairs; key is the number of the node, value is a set of neighbour nodes
     */
    private int nodesNumber;
    private Map<Integer, Set<Integer>> nodes ;

    //constructor
    public Graph( int n){
        this.nodesNumber = n;

        nodes = new HashMap<>();
        for(int node=0; node< n; node++){
            nodes.put(node, new HashSet<>());
        }
    }

    //add a new edge (muchie) to the graph
    public boolean addEdge(int startNode, int endNode){
        return nodes.get(startNode).add(endNode);
    }

    //checks if there is an edge between startNode and endNode
    public boolean existsEdge(int startNode, int endNode){
        return nodes.get(startNode).contains(endNode);
    }

    public int getNodesNumber() { return nodesNumber; }

    public void setNodesNumber(int nodesNumber) { this.nodesNumber = nodesNumber; }

    public Map<Integer, Set<Integer>> getNodes() { return nodes; }

    public void setNodes(Map<Integer, Set<Integer>> nodes) { this.nodes = nodes; }

    @Override
    public String toString() {
        return "Graph{" +
                "nodesNumber=" + nodesNumber +
                ", nodes=" + nodes +
                '}';
    }
}

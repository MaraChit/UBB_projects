import javafx.util.Pair;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Graph {
    private List<Pair<Integer,Integer>> edges;
    private List<Integer> nodes;

    Graph(int n){
        this.edges = new ArrayList<>(n);
        this.nodes = new ArrayList<>();

        for(int i=1; i<= n; i++){
            this.nodes.add(i);
        }
    }

    public void addEdge(int node1, int node2){
        Pair<Integer,Integer> newNode = new Pair<>(node1,node2);
        this.edges.add(newNode);
    }

    public List<Integer> getNeighbours(int node){
        List<Integer> result = new ArrayList<>();
        for(int i=0; i< this.edges.size(); i++){
            if( this.edges.get(i).getKey()==node){
                result.add(this.edges.get(i).getValue());
            }
        }
        return result;
    }

    public int getSize(){
        return this.edges.size();
    }

    public void generateRandomGraph(int size){
        int min = 1, max = this.nodes.size();
        for(int i=0; i < size; i++){
            Random r = new Random();
            int value1=r.nextInt((max - min) + 1) + min;
            int value2 = r.nextInt((max - min) + 1) + min;
            while (this.edges.contains(new Pair<>(value1,value2))){
                value1=r.nextInt((max - min) + 1) + min;
                value2 = r.nextInt((max - min) + 1) + min;
            }
            addEdge(value1,value2);
        }
    }
    public void generateHamiltonian( ){
        java.util.Collections.shuffle(this.nodes);
        for (int i=1; i< nodes.size(); i++){
            addEdge(nodes.get(i-1), nodes.get(i));
        }
        addEdge(nodes.get(nodes.size()-1),nodes.get(0));
    }

    @Override
    public String toString() {
        String s = "";
        for(int i=0; i< this.edges.size(); i++){

            s += this.edges.get(i).getKey() + "->" +  this.edges.get(i).getValue() + "\n";

        }
        return s;
    }
}

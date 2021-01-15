import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.locks.Lock;

public class Task implements Runnable{
    private Graph graph;
    private int startingNode;
    private List<Integer> path;
    private Lock lock;
    private List<Integer> result;

    Task(Graph graph, int node, List<Integer> result, Lock lock) {
        this.graph = graph;
        this.startingNode = node;
        path = new ArrayList<>();
        this.lock = lock;
        this.result = result;
    }

    @Override
    public void run() {
        visit(startingNode);
    }

    private void visit(int node) {
        this.path.add(node);

        if(path.size() == graph.getSize()){
            if(graph.getNeighbours(node).contains(startingNode)){
                this.lock.lock();
                this.result.clear();
                this.result.addAll(this.path);
                this.lock.unlock();
            }
            return;
        }
        for(int neighbour: graph.getNeighbours(node)){
            if(!this.path.contains(neighbour)){
                visit(neighbour);
            }
        }
    }
}

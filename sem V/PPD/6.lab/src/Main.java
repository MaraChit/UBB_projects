import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Main {
    public static void main(String[] args) throws InterruptedException {

        for (int k=0; k<10;k++){
            Graph g = new Graph(6);
            g.generateRandomGraph(20);

            Graph g2 = new Graph(6);
            g2.generateHamiltonian();

            List<Integer> found1 = findCycle(g,4);
            List<Integer> found2 = findCycle(g2,4);

            System.out.println("Normal: ");
            System.out.println(found1);

            System.out.println("Hemiltonian: ");
            System.out.println(found2);

        }


    }
    private static List<Integer> findCycle(Graph g, int threadsCount) throws InterruptedException {
        ExecutorService pool = Executors.newFixedThreadPool(threadsCount);
        Lock lock = new ReentrantLock();

        List<Integer> result = new ArrayList<>(g.getSize());

        for(int i=0; i< g.getSize(); i++){
            pool.execute(new Task(g,i,result,lock));
        }
        pool.shutdown();

        pool.awaitTermination(10, TimeUnit.SECONDS);
        return result;
    }
}

import mpi.MPI;

public class Main {
    public static void main(String[] args) {
        MPI.Init(args);

        int rank = MPI.COMM_WORLD.Rank();
        int size = MPI.COMM_WORLD.Size();

        //example
        Graph graph2 = new Graph(5);
        graph2.addEdge(0,1);
        graph2.addEdge(1,2);
        graph2.addEdge(2,3);
        graph2.addEdge(3,4);
        graph2.addEdge(4,0);
        graph2.addEdge(2,0);
        graph2.addEdge(0,4);
        graph2.addEdge(4,3);
        graph2.addEdge(3,1);

        Colors colors2 = new Colors(3);
        colors2.addColor(0, "red");
        colors2.addColor(1, "green");
        colors2.addColor(2, "blue");

        if (rank==0){
            System.out.println("Main process");

            try{
                long start = System.nanoTime();

                System.out.println(GraphColoring.graphColoringMain(size,graph2,colors2));
                long stop = System.nanoTime();

                long time = stop - start;
                System.out.println("Time: " + (time / 1000) + " microsec.");
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        else {
            System.out.println("Process number: "+ rank);

            int colorsNumber = colors2.getColorsNumber();

            GraphColoring.graphColoringChild(rank, size, graph2, colorsNumber);
        }
        MPI.Finalize();

    }
}

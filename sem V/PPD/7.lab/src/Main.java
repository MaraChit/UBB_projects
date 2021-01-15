import mpi.*;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        MPI.Init(args);

        int rank = MPI.COMM_WORLD.Rank();
        int size = MPI.COMM_WORLD.Size();

        /*int[] first = new int[]{1};
        int[] second = new int[]{2};
     // int[] result = new int[]{2};
*/

        /*int[] first = new int[]{2, 1};
        int[] second = new int[]{4, 3};
        // int[] result = new int[]{8, 10, 3};*/

       /*int[] first = new int[]{4, 3, 2, 1};
       int[] second = new int[]{8, 7, 6, 5};
       //int[] result = new int[]{32, 52, 61, 60, 34, 16, 5};*/

        int[] first = new int[]{8, 7, 6, 5, 4, 3, 2, 1};
        int[] second = new int[]{16, 15, 14, 13, 12, 11, 10, 9};
        // int[] result = new int[]{128, 232, 313, 372, 410, 428, 427, 408, 308, 224, 155, 100, 58, 28, 9};

        Operations operations = new Operations(first, second);


        if (rank == 0) {
            System.out.println("Main");
            long start = System.nanoTime();
            operations.polyMultiplication(size);
            long stop = System.nanoTime();
            long time = stop - start;
            System.out.println("Time: " + (time / 1000) + " microsec.");
        }
        else {
            System.out.println("Rank "+rank+" from "+size);
            operations.polyMultiplicationChild(rank);
        }

        MPI.Finalize();
    }


}

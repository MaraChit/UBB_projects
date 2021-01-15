import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {

    public static void main(String[] args) throws InterruptedException {
        // For simplicity, we will work only on square matrices
        int size = 5;
        int tasks = 3;
        int threads = 3;

        List<List<Integer>> firstMatrix = MatrixHelper.generateRandomMatrix(size);
        List<List<Integer>> secondMatrix = MatrixHelper.generateRandomMatrix(size);

        List<List<Integer>> resultMatrix = MatrixHelper.generateEmptyMatrix(size);

        int elements = size * size / tasks;
        int extraElements = size * size % tasks;

        program1(firstMatrix,secondMatrix,resultMatrix,elements,extraElements,tasks);
        program2(firstMatrix,secondMatrix,resultMatrix,elements,extraElements,tasks);
        program3(firstMatrix,secondMatrix,resultMatrix,elements,extraElements,tasks);
        program1ThreadPool(firstMatrix,secondMatrix,resultMatrix,elements,extraElements,tasks,threads);
        program2ThreadPool(firstMatrix,secondMatrix,resultMatrix,elements,extraElements,tasks,threads);
        program3ThreadPool(firstMatrix,secondMatrix,resultMatrix,elements,extraElements,tasks,threads);
    }

    private static void program1(List<List<Integer>> firstMatrix, List<List<Integer>> secondMatrix, List<List<Integer>> resultMatrix, int elements, int extraElements, int tasks){
        // Individual thread start
        List<Thread> threads = new ArrayList<>();
        Long startTime = System.currentTimeMillis();

        for(int i = 0; i < tasks; i++){
            int startIndex = i * elements;
            int endIndex = (i + 1) * elements - 1;

            if (i == tasks-1) endIndex += extraElements;

            int finalEndIndex = endIndex;

            Thread t = new Thread(() -> MatrixHelper.computeMultiplicationResultElements(startIndex, finalEndIndex, firstMatrix, secondMatrix, resultMatrix));

            threads.add(t);
            t.start();
        }

        for(Thread thread: threads){
            try {
                thread.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        Long endTime = System.currentTimeMillis();
        Long runTime = (endTime - startTime);

        System.out.println("First program: ");
        System.out.println(firstMatrix.toString());
        System.out.println(secondMatrix.toString());
        System.out.println(resultMatrix.toString());
        System.out.println(runTime.toString());
        System.out.println("\n");
    }

    private static void program2(List<List<Integer>> firstMatrix, List<List<Integer>> secondMatrix, List<List<Integer>> resultMatrix, int elements, int extraElements, int tasks){
        // Individual thread start
        List<Thread> threads = new ArrayList<>();
        Long startTime = System.currentTimeMillis();

        for(int i = 0; i < tasks; i++){
            int startIndex = i * elements;
            int endIndex = (i + 1) * elements - 1;

            if (i == tasks-1) endIndex += extraElements;

            int finalEndIndex = endIndex;

            Thread t = new Thread(() -> MatrixHelper.computeMultiplicationResultElements2(startIndex, finalEndIndex, firstMatrix, secondMatrix, resultMatrix));

            threads.add(t);
            t.start();
        }

        for(Thread thread: threads){
            try {
                thread.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        Long endTime = System.currentTimeMillis();
        Long runTime = (endTime - startTime);

        System.out.println("Second program: ");
        System.out.println(firstMatrix.toString());
        System.out.println(secondMatrix.toString());
        System.out.println(resultMatrix.toString());
        System.out.println(runTime.toString());
        System.out.println("\n");
    }

    private static void program3(List<List<Integer>> firstMatrix, List<List<Integer>> secondMatrix, List<List<Integer>> resultMatrix, int elements, int extraElements, int tasks){
        // Individual thread start
        List<Thread> threads = new ArrayList<>();
        Long startTime = System.currentTimeMillis();

        for(int i = 0; i < tasks; i++){
            int startIndex = i * elements;
            int endIndex = (i + 1) * elements - 1;

            if (i == tasks-1) endIndex += extraElements;

            int finalEndIndex = endIndex;

            Thread t = new Thread(() -> MatrixHelper.computeMultiplicationResultElements3(startIndex, finalEndIndex, firstMatrix, secondMatrix, resultMatrix));

            threads.add(t);
            t.start();
        }

        for(Thread thread: threads){
            try {
                thread.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        Long endTime = System.currentTimeMillis();
        Long runTime = (endTime - startTime);

        System.out.println("Third program: ");
        System.out.println(firstMatrix.toString());
        System.out.println(secondMatrix.toString());
        System.out.println(resultMatrix.toString());
        System.out.println(runTime.toString());
        System.out.println("\n");
    }

    private static void program1ThreadPool(List<List<Integer>> firstMatrix, List<List<Integer>> secondMatrix, List<List<Integer>> resultMatrix, int elements, int extraElements, int tasks, int threads){
        // Thread pool
        List<Runnable> taskList = new ArrayList<>();
        ExecutorService pool = Executors.newFixedThreadPool(threads);

        Long startTime = System.currentTimeMillis();

        for(int i = 0; i < tasks; i++){
            int startIndex = i * elements;
            int endIndex = (i + 1) * elements - 1;

            if (i == tasks-1) endIndex += extraElements;

            int finalEndIndex = endIndex;

            Runnable r = new Runnable() {
                @Override
                public void run()
                {
                    MatrixHelper.computeMultiplicationResultElements(startIndex, finalEndIndex, firstMatrix, secondMatrix, resultMatrix);
                }
            };

            taskList.add(r);
        }

        for (Runnable task: taskList){
            pool.execute(task);
        }

        pool.shutdown();
        Long endTime = System.currentTimeMillis();
        Long runTime = (endTime - startTime);

        System.out.println("First program with thread pool: ");
        System.out.println(firstMatrix.toString());
        System.out.println(secondMatrix.toString());
        System.out.println(resultMatrix.toString());
        System.out.println(runTime.toString());
        System.out.println("\n");
    }

    private static void program2ThreadPool(List<List<Integer>> firstMatrix, List<List<Integer>> secondMatrix, List<List<Integer>> resultMatrix, int elements, int extraElements, int tasks, int threads){
        // Thread pool
        List<Runnable> taskList = new ArrayList<>();
        ExecutorService pool = Executors.newFixedThreadPool(threads);
        Long startTime = System.currentTimeMillis();

        for(int i = 0; i < tasks; i++){
            int startIndex = i * elements;
            int endIndex = (i + 1) * elements - 1;

            if (i == tasks-1) endIndex += extraElements;

            int finalEndIndex = endIndex;

            Runnable r = new Runnable() {
                @Override
                public void run()
                {
                    MatrixHelper.computeMultiplicationResultElements2(startIndex, finalEndIndex, firstMatrix, secondMatrix, resultMatrix);
                }
            };

            taskList.add(r);
        }

        for (Runnable task: taskList){
            pool.execute(task);
        }

        pool.shutdown();
        Long endTime = System.currentTimeMillis();
        Long runTime = (endTime - startTime);

        System.out.println("Second program with thread pool: ");
        System.out.println(firstMatrix.toString());
        System.out.println(secondMatrix.toString());
        System.out.println(resultMatrix.toString());
        System.out.println(runTime.toString());
        System.out.println("\n");
    }

    private static void program3ThreadPool(List<List<Integer>> firstMatrix, List<List<Integer>> secondMatrix, List<List<Integer>> resultMatrix, int elements, int extraElements, int tasks, int threads){
        // Thread pool
        List<Runnable> taskList = new ArrayList<>();
        ExecutorService pool = Executors.newFixedThreadPool(threads);
        Long startTime = System.currentTimeMillis();

        for(int i = 0; i < tasks; i++){
            int startIndex = i * elements;
            int endIndex = (i + 1) * elements - 1;

            if (i == tasks-1) endIndex += extraElements;

            int finalEndIndex = endIndex;

            Runnable r = new Runnable() {
                @Override
                public void run()
                {
                    MatrixHelper.computeMultiplicationResultElements3(startIndex, finalEndIndex, firstMatrix, secondMatrix, resultMatrix);
                }
            };

            taskList.add(r);
        }

        for (Runnable task: taskList){
            pool.execute(task);
        }

        pool.shutdown();
        Long endTime = System.currentTimeMillis();
        Long runTime = (endTime - startTime);

        System.out.println("Third program with thread pool: ");
        System.out.println(firstMatrix.toString());
        System.out.println(secondMatrix.toString());
        System.out.println(resultMatrix.toString());
        System.out.println(runTime.toString());
        System.out.println("\n");
    }
}
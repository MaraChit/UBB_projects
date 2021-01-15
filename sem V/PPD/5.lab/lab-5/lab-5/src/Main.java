import java.util.concurrent.ExecutionException;

public class Main {
    public static void main(String[] args) throws InterruptedException, ExecutionException {

        // The following array represents
        // polynomial 5 + 10x^2 + 6x^3
        int A[] = {5,0,10,6};
        int m = A.length;
        Polynomial poly1 = new Polynomial(m);
        poly1.setPolynomial(A);

        // The following array represents
        // polynomial 1 + 2x + 4x^2
        int B[] = {1,2,4};
        int n = B.length;
        Polynomial poly2 = new Polynomial(n);
        poly2.setPolynomial(B);

        //Print the polynomials
        System.out.println("First polynomial is: ");
        poly1.printPoly();
        System.out.println("\nSecond polynomial is:");
        poly2.printPoly();
        System.out.println(" ");

        Operations operations = new Operations();

        System.out.println("\nApply classic multiplication: ");
        long startTime = System.currentTimeMillis();
        Polynomial prod = operations.multiplyClassic(poly1, poly2);
        prod.printPoly();
        long endTime = System.currentTimeMillis();
        System.out.println("\nExecution time : " + (endTime - startTime) + " ms \n");

        long startTime2 = System.currentTimeMillis();
        System.out.println("Apply Karatsuba:");
        Polynomial prod2 = operations.karatsuba(poly1, poly2);
        prod2.printPoly();
        long endTime2 = System.currentTimeMillis();
        System.out.println("\nExecution time : " + (endTime2 - startTime2) + " ms \n");

        long startTime3 = System.currentTimeMillis();
        System.out.println("\nParalelized classic multiplication:");
        Polynomial prod3 = operations.multiplyParallelizedForm(poly1,poly2,5);
        prod3.printPoly();
        long endTime3 = System.currentTimeMillis();
        System.out.println("\nExecution time : " + (endTime3 - startTime3) + " ms \n");

        long startTime4 = System.currentTimeMillis();
        System.out.println("\nParalelized Karatsuba: ");
        Polynomial prod4 = operations.karatsubaParallelizedForm(poly1, poly2);
        prod4.printPoly();
        long endTime4 = System.currentTimeMillis();
        System.out.println("\nExecution time : " + (endTime4 - startTime4) + " ms \n");
    }
}

import java.util.concurrent.*;

public class Operations {

    public Polynomial multiplyClassic(Polynomial poly1, Polynomial poly2)
    {
        int m = poly1.getSize();
        int n = poly2.getSize();

        // Initialize the product polynomial
        Polynomial poly = new Polynomial(m+n-1);
        int[] prod = poly.getPolynomial();

        // Multiply two polynomials term by term
        // Take ever term of first polynomial
        int[] p1 = poly1.getPolynomial();
        int[] p2 = poly2.getPolynomial();
        for (int i = 0; i < m; i++)
        {
            // Multiply the current term of first polynomial
            // with every term of second polynomial.
            for (int j = 0; j < n; j++)
            {
                prod[i + j] += p1[i] * p2[j];
            }
        }
        poly.setPolynomial(prod);
        return poly;
    }

    public Polynomial multiplyParallelizedForm(Polynomial p1, Polynomial p2, int nrOfThreads) throws  InterruptedException
    {
        //initialize result polynomial with coefficients = 0
        int sizeOfResultCoefficientList = p1.getSize() + p2.getSize() -1;
        Polynomial result = new Polynomial(sizeOfResultCoefficientList);

        //calculate the coefficients

        ThreadPoolExecutor executor = (ThreadPoolExecutor) Executors.newFixedThreadPool(nrOfThreads);
        int step = result.getSize() / nrOfThreads;
        if (step == 0) {
            step = 1;
        }

        int end;
        for (int i = 0; i < result.getSize(); i += step) {
            end = i + step;
            MultiplicationTask task = new MultiplicationTask(i, end, p1, p2, result);
            executor.execute(task);
        }

        executor.shutdown();
        executor.awaitTermination(50, TimeUnit.SECONDS);

        return result;
    }

    public Polynomial karatsuba(Polynomial poly1, Polynomial poly2){

        int sizePoly1 = poly1.getSize();
        int sizePoly2 = poly2.getSize();

        if (sizePoly1 > sizePoly2)
        {
            Polynomial temp = new Polynomial(sizePoly1);
            poly2 = add(temp,poly2);
        }

        if (sizePoly2>sizePoly1){
            Polynomial temp = new Polynomial(sizePoly2);
            poly1 = add(temp,poly1);
        }

        int degreePoly1 = sizePoly1-1;
        int degreePoly2 = sizePoly2-1;

        if (degreePoly1<2 || degreePoly2<2){
            return multiplyClassic(poly1, poly2);
        }

        //int len = Math.max(sizePoly1,sizePoly2)/2;
        int len = sizePoly1/2;

        Polynomial lowP1 = new Polynomial(poly1.getSubPoly(0,len));
        Polynomial highP1 = new Polynomial(poly1.getSubPoly(len, sizePoly1));
        Polynomial lowP2 = new Polynomial(poly2.getSubPoly(0,len));
        Polynomial highP2 = new Polynomial(poly2.getSubPoly(len, sizePoly2));

        //Step 1
        Polynomial p1 = karatsuba(lowP1, lowP2);
        //Step2
        Polynomial p2 = karatsuba(highP1,highP2);
        //Step3
        Polynomial p3 = karatsuba(add(lowP1,highP1), add(lowP2,highP2));
        //Step4
        //p3-p2-p1
        Polynomial p4 = substract(p3,add(p1,p2));
        //Step 5: p1+len*2 zerouri
        //        [lenp1-lenp2]*zerouri + p2
        //         p4 + len*zero
        Polynomial pExtended = new Polynomial(p1.getSize()+2*len);
        Polynomial p1Extended = new Polynomial(p1.getSize()+2*len);
        p1Extended = add(p1,p1Extended);

        Polynomial p2Extended = new Polynomial(p1.getSize()+2*len);
        int poz = 0;
        for(int i=p1Extended.getSize() - p1.getSize(); i<p1Extended.getSize(); i++){
            p2Extended.getPolynomial()[i] = p2.getPolynomial()[poz];
            poz++;
        }

        Polynomial p4Extended = new Polynomial(p4.getSize()+len);
        p4Extended = add(p4,p4Extended);
        poz=0;
        for (int i=pExtended.getSize()-p4Extended.getSize(); i<pExtended.getSize();i++){
            pExtended.getPolynomial()[i]=p4Extended.getPolynomial()[poz];
            poz++;
        }
        Polynomial result = add(add(p1Extended,p2Extended),pExtended);

        return result;
    }

    public Polynomial karatsubaParallelizedForm(Polynomial poly1, Polynomial poly2) throws ExecutionException, InterruptedException {

        int sizePoly1 = poly1.getSize();
        int sizePoly2 = poly2.getSize();

        if (sizePoly1 > sizePoly2)
        {
            Polynomial temp = new Polynomial(sizePoly1);
            poly2 = add(temp,poly2);
        }

        if (sizePoly2>sizePoly1){
            Polynomial temp = new Polynomial(sizePoly2);
            poly1 = add(temp,poly1);
        }

        int degreePoly1 = sizePoly1-1;
        int degreePoly2 = sizePoly2-1;

        if (degreePoly1<2 || degreePoly2<2){
            return multiplyClassic(poly1, poly2);
        }

        //int len = Math.max(sizePoly1,sizePoly2)/2;
        int len = sizePoly1/2;

        Polynomial lowP1 = new Polynomial(poly1.getSubPoly(0,len));
        Polynomial highP1 = new Polynomial(poly1.getSubPoly(len, sizePoly1));
        Polynomial lowP2 = new Polynomial(poly2.getSubPoly(0,len));
        Polynomial highP2 = new Polynomial(poly2.getSubPoly(len, sizePoly2));

        ThreadPoolExecutor executor = (ThreadPoolExecutor) Executors.newCachedThreadPool();
        Callable<Polynomial> task1 = () -> karatsubaParallelizedForm(lowP1, lowP2);
        Callable<Polynomial> task2 = () -> karatsubaParallelizedForm(highP1, highP2);
        Callable<Polynomial> task3 = () -> karatsubaParallelizedForm(add(lowP1, highP1), add(lowP2, highP2));

        Future<Polynomial> future1 = executor.submit(task1);
        Future<Polynomial> future2 = executor.submit(task2);
        Future<Polynomial> future3 = executor.submit(task3);

        executor.shutdown();

        Polynomial p1 = future1.get();
        Polynomial p2 = future2.get();
        Polynomial p3 = future3.get();

        executor.awaitTermination(60, TimeUnit.SECONDS);

        Polynomial p4 = substract(p3,add(p1,p2));
        //Step 5: p1+len*2 zerouri
        //        [lenp1-lenp2]*zerouri + p2
        //         p4 + len*zero
        Polynomial pExtended = new Polynomial(p1.getSize()+2*len);
        Polynomial p1Extended = new Polynomial(p1.getSize()+2*len);
        p1Extended = add(p1,p1Extended);

        Polynomial p2Extended = new Polynomial(p1.getSize()+2*len);
        int poz = 0;
        for(int i=p1Extended.getSize() - p1.getSize(); i<p1Extended.getSize(); i++){
            p2Extended.getPolynomial()[i] = p2.getPolynomial()[poz];
            poz++;
        }

        Polynomial p4Extended = new Polynomial(p4.getSize()+len);
        p4Extended = add(p4,p4Extended);
        poz=0;
        for (int i=pExtended.getSize()-p4Extended.getSize(); i<pExtended.getSize();i++){
            pExtended.getPolynomial()[i]=p4Extended.getPolynomial()[poz];
            poz++;
        }
        Polynomial result = add(add(p1Extended,p2Extended),pExtended);

        return result;
    }

    private Polynomial add(Polynomial poly1, Polynomial poly2){
        int sizePoly1 = poly1.getSize();
        int sizePoly2 = poly2.getSize();

        int degreePoly1 = sizePoly1-1;
        int degreePoly2 = sizePoly2-1;

        int minDegree = Math.min(degreePoly1,degreePoly2);
        int maxDegree = Math.max(degreePoly1,degreePoly2);

        int[] result = new int[maxDegree+1];

        //Add two polynomials
        for (int i=0;i<= minDegree; i++){
            result[i] = poly1.getPolynomial()[i] + poly2.getPolynomial()[i];
        }

        //Add remaining coefficients
        if(minDegree!= maxDegree){
            if(maxDegree == degreePoly1){
                for (int i=minDegree+1; i<= maxDegree; i++){
                    result[i] = poly1.getPolynomial()[i] ;
                }
            }
            else {
                for (int i=minDegree+1; i<= maxDegree; i++){
                    result[i] = poly2.getPolynomial()[i] ;
                }
            }
        }
        return new Polynomial(result);

    }

    private Polynomial substract(Polynomial poly1, Polynomial poly2){
        int sizePoly1 = poly1.getSize();
        int sizePoly2 = poly2.getSize();

        int degreePoly1 = sizePoly1-1;
        int degreePoly2 = sizePoly2-1;

        int minDegree = Math.min(degreePoly1,degreePoly2);
        int maxDegree = Math.max(degreePoly1,degreePoly2);

        int[] result = new int[maxDegree+1];

        //Substract two polynomials
        for (int i=0;i<= minDegree; i++){
            result[i] = poly1.getPolynomial()[i] - poly2.getPolynomial()[i];
        }

        //Add remaining coefficients
        if(minDegree!= maxDegree){
            if(maxDegree == degreePoly1){
                for (int i=minDegree+1; i<= maxDegree; i++){
                    result[i] = poly1.getPolynomial()[i] ;
                }
            }
            else {
                for (int i=minDegree+1; i<= maxDegree; i++){
                    result[i] = poly2.getPolynomial()[i] ;
                }
            }
        }

        int i = result.length-1;
        int zero = 0;
        while(result[i]==0 && i>0){
            zero++;
            i--;
        }

        int[] fin = new int[result.length-zero];
        for(int k=0; k< result.length-zero;k++){
            fin[k]=result[k];
        }

        Polynomial fini = new Polynomial(fin);
        return fini;
    }
}

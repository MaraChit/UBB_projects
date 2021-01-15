public class Polynomial {
    private int[] polynomial;

    public Polynomial(int n) {
        this.polynomial = this.generateEmptyPoly(n);
    }

    public Polynomial(int[] poly){
        this.polynomial = poly;
    }

    public int[] getPolynomial() {
        return polynomial;
    }

    public void setPolynomial(int[] polynomial) {
        this.polynomial = polynomial;
    }

    public int[] generateEmptyPoly( int n){
        int[] a = new int[n];
        for(int i=0; i<n; i++) {
            a[i]= 0;
        }
        return a;
    }

    public int getSize(){
        return this.polynomial.length;
    }

    void printPoly()
    {
        int n = this.polynomial.length;
        for (int i = 0; i < n; i++)
        {
            System.out.print(this.polynomial[i]);
            if (i != 0)
            {
                System.out.print("x^" + i);
            }
            if (i != n - 1)
            {
                System.out.print(" + ");
            }
        }
    }

    public int[] getSubPoly (int start, int end){

        int[] subPoly = new int[end-start];
        int poz = 0;
        for (int i = start; i<end; i++){
            subPoly[poz]=this.polynomial[i];
            poz++;
        }

        return subPoly;
    }


}

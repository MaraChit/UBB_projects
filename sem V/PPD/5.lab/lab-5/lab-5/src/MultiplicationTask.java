public class MultiplicationTask implements Runnable {
    private int start;
    private int end;
    private Polynomial p1, p2, result;

    public MultiplicationTask(int start, int end, Polynomial p1, Polynomial p2, Polynomial result) {
        this.start = start;
        this.end = end;
        this.p1 = p1;
        this.p2 = p2;
        this.result = result;
    }

    /**
     * Calculate coefficients from the result in the interval: [starting index, ending index])
     */
    @Override
    public void run() {
        for (int index = start; index < end; index++) {
            //case - no more elements to calculate
            if (index > result.getSize()) {
                return;
            }
            //find all the pairs that we add to obtain the value of a result coefficient
            for (int j = 0; j <= index; j++) {
                if (j < p1.getSize() && (index - j) < p2.getSize()) {
                    int value = p1.getPolynomial()[j] * p2.getPolynomial()[index - j];
                    result.getPolynomial()[index] = result.getPolynomial()[index]+value;
                }
            }
        }
    }
}

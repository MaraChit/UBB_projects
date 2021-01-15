import mpi.MPI;

import java.util.Arrays;

public  class Operations {

    private int[] first;
    private int[] second;

    public  Operations(int[] first, int[] second){
        this.first = first;
        this.second = second;
    }

    public  void polyMultiplication(int mpiSize) {
        //main
        int size = first.length;

        int[] result = polyMultiplicationRec(size, first, second, 0, mpiSize, 0);
        System.out.println("RESULT= " + Arrays.toString(result));
    }

    private static int[] polyMultiplicationRec(int size, int[] first, int[] second, int mpiRank, int mpiSize, int power) {
        //MPI destinations
        int coefficient = (int) Math.pow(4, power);
        int firstDest = mpiRank + coefficient;
        int secondDest = mpiRank + coefficient * 2;
        int thirdDest = mpiRank + coefficient * 3;

        if (size <= 1) {
            //stop MPI child hosts
            int[] returnMetadata = new int[]{-1, -1, -1};
            if (firstDest < mpiSize) {
                MPI.COMM_WORLD.Send(returnMetadata, 0, returnMetadata.length, MPI.INT, firstDest, 0);
            }
            if (secondDest < mpiSize) {
                MPI.COMM_WORLD.Send(returnMetadata, 0, returnMetadata.length, MPI.INT, secondDest, 0);
            }
            if (thirdDest < mpiSize) {
                MPI.COMM_WORLD.Send(returnMetadata, 0, returnMetadata.length, MPI.INT, thirdDest, 0);
            }

            if (size <= 0) {
                return new int[]{0};
            }
            return new int[]{first[0] * second[0]};
        }

        int middleSize = size / 2;
        int[] metadata = new int[]{mpiRank, middleSize, power + 1};

        //split polynomials
        int[] firstLower = getSubarray(first, 0, middleSize);
        int[] firstUpper = getSubarray(first, middleSize, size);
        int[] secondLower = getSubarray(second, 0, middleSize);
        int[] secondUpper = getSubarray(second, middleSize, size);

        //multiplications
        /*
        Step 1: a*c
        Step 2: b*d
        Step 3: (a+b)(c+d)
        Step 4: Step3 - Step2- Step1 = ad + bc
         */

        //firstMul = ac
        int[] firstMultiply = polyMultiplicationRec(middleSize, firstUpper, secondUpper, mpiRank, mpiSize, power + 1);

        int[] secondMultiply = null;
        int[] thirdMultiply = null;
        int[] fourthMultiply = null;

        // secondMul = ad
        if (firstDest < mpiSize) {
            MPI.COMM_WORLD.Send(metadata, 0, metadata.length, MPI.INT, firstDest, 0);

            MPI.COMM_WORLD.Send(firstUpper, 0, middleSize, MPI.INT, firstDest, 0);
            MPI.COMM_WORLD.Send(secondLower, 0, middleSize, MPI.INT, firstDest, 0);
        }
        else {
            secondMultiply = polyMultiplicationRec(middleSize, firstUpper, secondLower, mpiRank + coefficient, mpiSize, power + 1);
        }

        //thirdMul = bc
        if (secondDest < mpiSize) {
            MPI.COMM_WORLD.Send(metadata, 0, metadata.length, MPI.INT, secondDest, 0);

            MPI.COMM_WORLD.Send(firstLower, 0, middleSize, MPI.INT, secondDest, 0);
            MPI.COMM_WORLD.Send(secondUpper, 0, middleSize, MPI.INT, secondDest, 0);
        }
        else {
            thirdMultiply = polyMultiplicationRec(middleSize, firstLower, secondUpper, secondDest, mpiSize, power + 1);
        }

        //fourthMul = bd
        if (thirdDest < mpiSize) {
            MPI.COMM_WORLD.Send(metadata, 0, metadata.length, MPI.INT, thirdDest, 0);

            MPI.COMM_WORLD.Send(firstLower, 0, middleSize, MPI.INT, thirdDest, 0);
            MPI.COMM_WORLD.Send(secondLower, 0, middleSize, MPI.INT, thirdDest, 0);
        }
        else {
            fourthMultiply = polyMultiplicationRec(middleSize, firstLower, secondLower, thirdDest, mpiSize, power + 1);
        }

        //receive multiplication results from child hosts
        if (firstDest < mpiSize) {
            int[] multiplicationSize = new int[1];
            MPI.COMM_WORLD.Recv(multiplicationSize, 0, multiplicationSize.length, MPI.INT, firstDest, MPI.ANY_TAG);

            secondMultiply = new int[multiplicationSize[0]];
            MPI.COMM_WORLD.Recv(secondMultiply, 0, multiplicationSize[0], MPI.INT, firstDest, MPI.ANY_TAG);
        }
        if (secondDest < mpiSize) {
            int[] multiplicationSize = new int[1];
            MPI.COMM_WORLD.Recv(multiplicationSize, 0, multiplicationSize.length, MPI.INT, secondDest, MPI.ANY_TAG);

            thirdMultiply = new int[multiplicationSize[0]];
            MPI.COMM_WORLD.Recv(thirdMultiply, 0, multiplicationSize[0], MPI.INT, secondDest, MPI.ANY_TAG);
        }
        if (thirdDest < mpiSize) {
            int[] multiplicationSize = new int[1];
            MPI.COMM_WORLD.Recv(multiplicationSize, 0, multiplicationSize.length, MPI.INT, thirdDest, MPI.ANY_TAG);

            fourthMultiply = new int[multiplicationSize[0]];
            MPI.COMM_WORLD.Recv(fourthMultiply, 0, multiplicationSize[0], MPI.INT, thirdDest, MPI.ANY_TAG);
        }

        //terms
        int[] firstTerm = addAtTheBeginning(firstMultiply, 0, size);
        int[] secondTerm = addAtTheBeginning(
                addArrays(secondMultiply, thirdMultiply),
                0,
                middleSize
        );
        int[] thirdTerm = fourthMultiply;

        return addArrays(
                firstTerm,
                addArrays(
                        secondTerm,
                        thirdTerm
                )
        );
    }

    public static void polyMultiplicationChild(int mpiRank) {
        //RECV
        //metadata
        int[] metadata = new int[3];
        MPI.COMM_WORLD.Recv(metadata, 0, 3, MPI.INT, MPI.ANY_SOURCE, MPI.ANY_TAG);

        int parent = metadata[0];
        int size = metadata[1];
        int power = metadata[2];

        //stop if result already computed
        if (parent == -1) {
            return;
        }

        //polynomials
        int[] first = new int[size];
        int[] second = new int[size];

        MPI.COMM_WORLD.Recv(first, 0, size, MPI.INT, MPI.ANY_SOURCE, MPI.ANY_TAG);
        MPI.COMM_WORLD.Recv(second, 0, size, MPI.INT, MPI.ANY_SOURCE, MPI.ANY_TAG);

        //SEND
        int[] multiply = polyMultiplicationRec(size, first, second, mpiRank, MPI.COMM_WORLD.Size(), power);
        int[] multiplicationSize = new int[]{multiply.length};

        MPI.COMM_WORLD.Send(multiplicationSize, 0, multiplicationSize.length, MPI.INT, parent, 0);
        MPI.COMM_WORLD.Send(multiply, 0, multiply.length, MPI.INT, parent, 0);
    }

    private static int[] getSubarray(int[] array, int startInclusive, int endExclusive) {
        return Arrays.copyOfRange(array, startInclusive, endExclusive);
    }

    private static int[] addAtTheBeginning(int[] array, int value, int count) {
        int[] newArray = new int[array.length + count];

        for (int index = 0; index < count; index++) {
            newArray[index] = value;
        }
        for (int index = 0; index < array.length; index++) {
            newArray[index + count] = array[index];
        }

        return newArray;
    }

    private static int[] addArrays(int[] first, int[] second) {
        int[] newArray = new int[Math.max(first.length, second.length)];

        for (int index = 0; index < newArray.length; index++) {
            newArray[index] =
                    (index < first.length ? first[index] : 0) +
                            (index < second.length ? second[index] : 0);
        }

        return newArray;
    }
}

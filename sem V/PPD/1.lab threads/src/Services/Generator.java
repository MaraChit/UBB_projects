package Services;

import java.util.Random;


public class Generator {
    private static final Random random = new Random();

    public Generator() {

    }

    private static final String CHAR_LIST =
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
    private static final int RANDOM_STRING_LENGTH = 10;

    public static String generateRandomString(){
        StringBuilder randStr = new StringBuilder();
        for(int i=0; i<RANDOM_STRING_LENGTH; i++){
            int number = generateRandomInt(0,RANDOM_STRING_LENGTH);
            char ch = CHAR_LIST.charAt(number);
            randStr.append(ch);
        }
        return randStr.toString();
    }

    public static int generateRandomInt(int low, int high){
        return random.ints(low, high).limit(1).sum();
    }
}


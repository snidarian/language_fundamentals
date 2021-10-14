import java.util.Random;


public class ArraysInJava {
    
    public static void main(String[] args) {

        // an array of strings
        String[] a = new String[10];

        a[0] = "Hey. how's it going?";
        a[1] = "Java is great isn't it?";
        a[2] = "What do you think about java?";


        for(int i=0;i < a.length;i++) {
            System.out.println(a[i]);
        }

        // an integer array

        int[] b = new int[5];

        b[0] = 15;
        b[1] = 55;
        b[2] = 75;
        b[3] = 25;
        b[4] = 5;


        // The "more C-like" way to make an array:

        int[] c = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};


        // an array of arrays in java

        int[][] d = { {1, 2, 3}, {4, 5, 6}, {6, 7, 8}, {9, 10, 11}, {12, 13, 14} };

        // if I wanted to access the number nine in the above array
        System.out.println("Item accessed from the array of arrays: "+d[3][0]);


        // printint the average of all the values in the 2d 'd' array
        System.out.println("Printing the average of the d array");

        int elementCount = 0;
        int sum = 0;
        for(int i0=0;i0<d.length;i0++) {
            for(int i1=0;i1<d[i0].length;i1++) {
                System.out.println(d[i0][i1]);
                elementCount += 1;
                sum += d[i0][i1];
            }
        }

        // printing out the average of all the items in the array
        System.out.println("The total average of the d array is "+ (sum / elementCount));


    }
}

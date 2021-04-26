// properly using the scanner class to get user input

import java.util.Scanner;

public class gettingInputWithScannerClass {
    // creating a scanner object from Scanner class to use in program
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args)
    {
        System.out.print("Enter and integer: ");
        int x = sc.nextInt(); // nextin() method converts input to primitive integer data type
        System.out.println("You entered " + x + ".");
    }
}

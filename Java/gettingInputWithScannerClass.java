// properly using the scanner class to get user input

import java.util.Scanner;

public class gettingInputWithScannerClass {
    // creating a scanner object from Scanner class to use in program
    // To create a Scanner object, you use the 'new' keyword followed by a call to the Scanner class constructor
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args)
    {
        System.out.print("Enter and integer: ");
        int x = sc.nextInt(); // nextin() method converts input to primitive integer data type
        System.out.println("You entered " + x + ".");
        
        // now the same thing but with a string. Notice the use of of a different method this time
        System.out.print("Enter a string: ");
        String str = sc.next();
        System.out.println(str);
    }
}

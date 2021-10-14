import java.util.Scanner;

public class ElseIfElseStatements {
    

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int number = sc.nextInt();


        // Determine if number is positive, negative or zero
        if (number > 0) {
            System.out.println("Number is positive");
        }
        else if (number == 0) {
            System.out.println("Number is not positive or negative");
        }
        else {
            System.out.println("Number is negative");
        }

        // Determine if number is even or odd
        if ((number % 2) == 0) {
            System.out.println("Number is even");
        }
        else {
            System.out.println("Number is odd");
        }


        sc.close();

    }
}

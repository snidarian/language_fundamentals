
import java.util.Scanner;


public class GettingInput {
    
    public static void main(String[] args) {
        

        // You can use other inputs (ie a file) instead of System.in
        Scanner scanning_object = new Scanner(System.in);


        // here's a sample program that takes two integers as input and performs all the arithmetic operations on them
        int g = scanning_object.nextInt();
        int p = scanning_object.nextInt();


        System.out.println("You typed: " + g + " and " + p);

        System.out.print("" + g + " + " + p + " = "); System.out.println(g+p);
        System.out.print("" + g + " - " + p + " = "); System.out.println(g-p);
        System.out.print("" + g + " * " + p + " = "); System.out.println(g*p);
        System.out.print("" + g + " / " + p + " = "); System.out.println(g/p);
        System.out.print("" + g + " % " + p + " = "); System.out.println(g%p);
        


        scanning_object.close();


    }
}

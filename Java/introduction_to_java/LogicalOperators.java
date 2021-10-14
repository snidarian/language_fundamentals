import java.util.Scanner;


public class LogicalOperators {
    
    public static void main(String[] args) {

        /* LOGICAL OPERATORS
        &&
        ||
        !
        */

        boolean t = true;
        boolean f = false;


        System.out.println(t && f);

        Scanner sc = new Scanner(System.in);


        boolean first = sc.nextBoolean();
        boolean second = sc.nextBoolean();

        boolean andOperator = first && second;
        boolean orOperator = first || second;


        System.out.println(first + " && "+ second +" = "+ andOperator);
        System.out.println(first + " || "+ second +" = "+ orOperator);


    }
}

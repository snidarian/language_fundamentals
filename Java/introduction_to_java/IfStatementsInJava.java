import java.util.Scanner;


public class IfStatementsInJava {
    
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();

        if (a > 5) {
            System.out.println("a is more than 5");
            System.out.println("a = "+a);
            
        }
        else {
            System.out.println("a is not more than 5");
            System.out.println("a = "+a);
        }

        

        sc.close();



    }
}

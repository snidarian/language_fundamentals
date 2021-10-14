public class NonNumericDataTypes {

    public static void main(String[] args) {

        /*
        There are two non-numeric data types:
        */

        // Booleans are created with the boolean keyword


        boolean a = true;
        boolean b = false;

        System.out.println(a);
        System.out.println(b);

        // chars

        char c = 'c';
        int d = 100;

        // integer representation of letter c = 99
        System.out.println((int)c);
        // character representation of letter d = 100
        System.out.println((char)d);



        // How you can create strings by adding various variable values together in a print statement
        System.out.println(a + " " + c + (char)d + b + "whatever...");
    }
}

public class Recursion {
    


    public static int recursivelyCountToZero(int startingNumber) {

        // print the current value of starting number
        System.out.print(startingNumber+", ");
        // This if statement ensures that the numbers will be in columns of ten
        if (startingNumber % 10 == 0){
            System.out.println(" ");
        }
        if (startingNumber != 0) {
            return recursivelyCountToZero(startingNumber-1);
        }
        else {
            return 0;
        }
    }


    public static void main(String[] args) {


        recursivelyCountToZero(300);

    }


}

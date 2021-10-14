// first method
import java.lang.Math;
// Second method
import java.util.Random;
// third method
import java.util.concurrent.ThreadLocalRandom;


public class RandomNumbers {
    
    public static void main(String[] args) {


        // ####################################################################
        // getting random numbers using the java.lang.Math class
        int min = 100;
        int max = 500;

        double a = Math.random()*(max-min+1)+min;

        System.out.println("Random number: "+a);


        // #################################################################
        // getting random numbers using the Random() class

        // Instantiate and object from the Random() class
        Random random_object = new Random();

        // Generate random integer from 0 to 50
        System.out.println(random_object.nextInt(50));

        // Generate random integer from 0 to 1000
        System.out.println(random_object.nextInt(1000));

        // Generate random long integer
        System.out.println(random_object.nextLong());

        // Generate Random float values from 0 to 1
        System.out.println(random_object.nextFloat());

        // Generate Random double values from 0 to 1
        System.out.println(random_object.nextDouble());

        // Generate Random boolean value
        System.out.println(random_object.nextBoolean());



        // #############################################################################################
        // Getting random numbers using java.util.concurrent.ThreadLocalRandom

        int firstRandomNumber = ThreadLocalRandom.current().nextInt(110, 119);
        int secondRandomNumber = ThreadLocalRandom.current().nextInt(110, 119);
        int thirdRandomNumber = ThreadLocalRandom.current().nextInt(110, 119);


        System.out.println(firstRandomNumber);
        System.out.println(secondRandomNumber);
        System.out.println(thirdRandomNumber);



        

        






    }
}

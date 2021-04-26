public class cast_operators {
    public static void main(String[] args) {
        // say you have double like the one below
        double number0 = 4.563409;
        // now say you want to change the above number to an int.
        int number0_converted;
        number0_converted = (int) number0;
        System.out.println(number0_converted);
        // When number0_converted is printed it simply prints '4'
        // this is because data is lost here when we convert a double into an integer.

        // say that you have a float you want to convert to a byte
        float float0 = 47.52F;
        byte byte0;
        byte0 = (byte) float0;
        System.out.println(byte0);
    }
}

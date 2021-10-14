

public class WorkingWithStrings {
    
    // Strings are a complex data type, not a primitive data type
    public static void main(String[] args) {

        // a string is a collection or list of characters
        int a = 12;
        String hw = "The price is " + a;

        System.out.println(hw);
        

        // String methods
        System.out.println(hw.length());
        // returns false since the string does no equal hi
        System.out.println(hw.equals("hi"));
        // returns the index value of the first given character
        System.out.println(hw.indexOf("i"));
        // returns the char value that is at the specified index value
        System.out.println(hw.charAt(0));
        // Returns a substring from value startindex to value endindex
        System.out.println(hw.substring(0, 5));
        // Replace first given value with second given value
        System.out.println(hw.replace('p', 'P'));
        // returns true if the specified string contains the method's argument sequence
        System.out.println(hw.contains("The"));
        // transforms the string to lowercase
        System.out.println(hw.toLowerCase());

    }
}

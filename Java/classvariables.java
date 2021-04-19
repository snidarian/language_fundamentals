// Class variables are variables that can be used by the methods of a class
// There two rules when declaring class variables:
// 1. You must place the variable declaration within the body of the class
// (but not within any of the class methods.)

// 2. You must include the word 'static' in the declaration.
// (the word static comes before the variable type)

// You can either place class declarations at the beginning or end of a class definition

public class classvariables {    
    static String helloMessage = "hello, world";
    public static void main(String[] args) {
        System.out.println(helloMessage);
    }
}


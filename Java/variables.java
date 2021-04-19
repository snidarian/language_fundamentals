

public class variables {

    /*
    The general rules for constructing names for variables (unique identifiers) are:

    Names can contain letters, digits, underscores, and dollar signs
    Names must begin with a letter
    Names should start with a lowercase letter and it cannot contain whitespace
    Names can also begin with $ and _ (but we will not use it in this tutorial)
    Names are case sensitive ("myVar" and "myvar" are different variables)
    Reserved words (like Java keywords, such as int or boolean) cannot be used as names
    */
    
    public static void main(String[] args) {
        
        // primitive data type examples
        int a = 0;
        String b = "name";
        // Just like golang intellisense engine - java intellisense throws lint errors for unused variables.
        int c = 45;
        // final keyword creates immutable variable (read only)
        final int d = 55;
        // notice the f after the float number.
        float e = 14.99f;
        // char just like in C
        char f = 'K';
        boolean g = true;
        boolean h = false;


        //many variables can be declared in a single line
        int x = 5, y = 4, z = 3;
        System.out.println(x + y + z);



        System.out.println(g);
        System.out.println(h);
        
        // This print statement highlights Java's weakness with regard to supporting calculations of decimal data.
        System.out.println(e + c);
        System.out.println(a + c + d);
        System.out.println(b);
        System.out.println(f);

        // Abstract data type - object
        
    }


    


}

// Declaring instance variables.

// The keyword static defines the method or variable of a class as
// dissassociated from the instantiated objects of that class.

// for that reason:
// You can't use an instance variable in a static method.
// (That include the main method)


// The following program won't compile because
// non-static variables cannot be referenced from a static context


public class instance_variables_in_nonstatic_context {
    
    String strvar = "alsdjflakhsjdf";

    public static void main(String[] args) {
        //System.out.println(strvar);
    }



}


// The output when this program tries to compile is:
// "Cannot make a static reference to the non-static field strvar"




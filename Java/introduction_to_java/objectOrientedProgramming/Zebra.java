package objectOrientedProgramming;

// Here by including 'extends' we make Zebra the inheritor of static variables of the horse class
public class Zebra extends Horse {
    

    // Here's a static method. It can be accessed by both static and not static methods
    public static String makeZebraWinny() {
        return "Neiiggggghhhhh!";
    }

    // This would be true of all Zebras so it would make sense to make this a static variable of the class
    public static boolean hasStripes = true;

    double weight;
    double height;
    String name;
    int zebraFitnessLevel;


    // These non-static methods may only be accessed by non-static methods
    public String returnZebraName() {
        return name;
    }

    public void printZebraName() {
        System.out.println(name);
    }


}

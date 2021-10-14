package objectOrientedProgramming;

public class Horse extends Mammal {

    public static boolean hasFourLegs = true;
    public static boolean hasHooves = true;
    public static boolean canGallop = true;
    public static boolean eatsHay = true;



    public static void canCarryAHuman() {
        System.out.println("CAN carry a human with or without a saddle");
    }

    public String produceManure(String Hay) {
        
        // digestion of Hay produces manure
        String manure = "manure";
        
        return manure;
    }
    
}

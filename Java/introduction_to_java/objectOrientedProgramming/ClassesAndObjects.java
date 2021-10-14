package objectOrientedProgramming;


public class ClassesAndObjects {


    public static void main(String[] args) {
        
        // create zebra object from the Zebra class template
        Zebra zebraObject = new Zebra();

        // assign values to the attributes of an object of the Zebra class
        zebraObject.height = 5.0;
        zebraObject.weight = 400.45;
        zebraObject.name = "Zanders";
        zebraObject.zebraFitnessLevel = 8;

        // Printing out those attributes
        System.out.println(zebraObject.height);
        System.out.println(zebraObject.weight);

    
        // You can access a static method of a class from its instantiated object but the IDE tells you not to
        System.out.println(zebraObject.makeZebraWinny());

        zebraObject.printZebraName();

        System.out.println("What is the name of your zebra? is it "+ zebraObject.returnZebraName()+ "?");

        // accessing a static method in a static context by using the methods class
        System.out.println(Zebra.makeZebraWinny());


        // hasStripes is a static variable that is defined in the class definition
        
        // You can reach the value in a static and non-static context
        
        // static
        System.out.println(Zebra.hasStripes);
        // non-static
        System.out.println(zebraObject.hasStripes);

        
        // Let's test if Zebra inherits common traits from the Horse class in Horse.java
        System.out.println("Do Zebras have four legs like Horses? "+Zebra.hasFourLegs);
        System.out.println("Do Zebras have hooves like Horses? " +Zebra.hasHooves);


        // if we create a horse object we can use its non-static "produceManure" method
        Horse horseObject = new Horse();

        horseObject.produceManure("Grass");

        // A zebra object can also use non-static methods inherited from the Horse class.
        System.out.println(zebraObject.produceManure("Hey"));


        // a zebra object can also use the non-static methods from the Mammal class which Horse Extends
        zebraObject.breathe();
    
        

    }

    

}




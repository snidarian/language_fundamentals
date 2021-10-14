import java.util.Scanner;


public class SwitchCaseStatements {
    
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String favoriteFruit = sc.nextLine();

        switch(favoriteFruit) {
            case "apple": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "apricot": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "banana": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "blueberry": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "cantaloupe": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "dragonfruit": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "durian": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "horned melon": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "jackfruit": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "kiwi": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "lemon": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "mandarin orange": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "olive": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "orange": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "papaya": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "rambutan": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "tamarind": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "vanilla": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            case "watermelon": 
            System.out.println("Your favorite fruit is "+ favoriteFruit); break;
            default : 
            System.out.println("You didn't select one of the available fruits"); break;

        }


        sc.close();

    }
}

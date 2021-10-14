public class Methods {
    
    
    public static void printArrayForwards(int[] arrayName) {
        for (int i = 0; i < arrayName.length;i++) {
            System.out.println(arrayName[i]);
        }
    }

    public static void printArrayBackwards(int[] arrayName) {
        for (int i = arrayName.length-1; i >= 0; i--) {
            System.out.println(arrayName[i]);
        }
    }

    public static void printArrayInAscendingOrder(int[] arrayName) {
        for(int i = 0; i < arrayName.length-1; i++) {
            for(int i1 = 0; i1 < arrayName.length-1; i1++) {
                if (arrayName[i1] > arrayName[i1+1]) {
                    int temporaryValue = arrayName[i1+1];
                    arrayName[i1+1] = arrayName[i1];
                    arrayName[i1] = temporaryValue;
                }
            }
        }
        for(int j = 0; j < arrayName.length; j++) {
            System.out.println(arrayName[j]);
        }
    }

    // Here to get descending order were just sorting the array in ascending order and then printing it backwards.
    public static void printArrayInDescendingOrder(int[] arrayName) {
        for(int i = 0; i < arrayName.length-1; i++) {
            for(int i1 = 0; i1 < arrayName.length-1; i1++) {
                if (arrayName[i1] > arrayName[i1+1]) {
                    int temporaryValue = arrayName[i1+1];
                    arrayName[i1+1] = arrayName[i1];
                    arrayName[i1] = temporaryValue;
                }
            }
        }
        for(int j = arrayName.length-1; j >= 0; j--) {
            System.out.println(arrayName[j]);
        }
    }

    public static void printOnlyEvens(int[] arrayName) {
        // sort array into ascending order
        for(int i = 0; i < arrayName.length-1; i++) {
            for(int i1 = 0; i1 < arrayName.length-1; i1++) {
                if (arrayName[i1] > arrayName[i1+1]) {
                    int temporaryValue = arrayName[i1+1];
                    arrayName[i1+1] = arrayName[i1];
                    arrayName[i1] = temporaryValue;
                }
            }
        }
        for(int i = 0; i < arrayName.length; i++) {
            if ((arrayName[i] % 2) == 0) {
                System.out.println(arrayName[i]);
            }
        }
    }

    public static void printOnlyOdds(int[] arrayName) {
        // sort array into ascending order
        for(int i = 0; i < arrayName.length-1; i++) {
            for(int i1 = 0; i1 < arrayName.length-1; i1++) {
                if (arrayName[i1] > arrayName[i1+1]) {
                    int temporaryValue = arrayName[i1+1];
                    arrayName[i1+1] = arrayName[i1];
                    arrayName[i1] = temporaryValue;
                }
            }
        }
        for(int i = 0; i < arrayName.length; i++) {
            if ((arrayName[i] % 2) != 0) {
                System.out.println(arrayName[i]);
            }
        }
    }

    
    public static void main(String[] args) {

        int[] a = {12, 4, 10, 102, 249, 120, 259, 140, 119, 10003, 52, 45, 69, 73, 84};


        System.out.println("Forwards: ");
        printArrayForwards(a);
        System.out.println("Backwards: ");
        printArrayBackwards(a);
        System.out.println("Ascending order: ");
        printArrayInAscendingOrder(a);
        System.out.println("Descending order: ");
        printArrayInDescendingOrder(a);
        System.out.println("Print only evens: ");
        printOnlyEvens(a);
        System.out.println("Print only odds: ");
        printOnlyOdds(a);

    }
}

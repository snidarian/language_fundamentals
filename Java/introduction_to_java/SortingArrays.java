public class SortingArrays {
    
    public static void main(String[] args) {

        int[] a = {4, 2, 5, 7, 3, 5, 4, 3, 2, 1};

        // ##########################################
        //bubble sort (ascending)
        System.out.println("Bubble sort ascending");
        for(int i = 0; i < a.length;i++) {
            for(int i1 = 0; i1 < a.length-1;i1++) {
                if (a[i1] > a[i1+1]) {
                    // save the number at i1 index to a temporary variable
                    int temp = a[i1];
                    a[i1] = a[i1+1];
                    // use the temp and save it to a[i1+1]
                    a[i1+1] = temp;
                }
            }
        }

        // print the array an see what order its in
        for(int j=0;j<a.length;j++){
            System.out.println(a[j]);
        }


        int[] b = {1, 5, 6, 8, 3, 3, 5, 3, 7, 3, 111, 3, 231, 9, 5, 7, 3, 5};


        System.out.println("Bubble sort descending");
        //###########################################
        //bubble sort (descending)
        for(int i = 0; i < b.length;i++) {
            for(int i1 = 0; i1 < b.length-1;i1++) {
                if (b[i1] < b[i1+1]) {
                    // save the number at i1 index to a temporary variable
                    int temp = b[i1+1];
                    b[i1+1] = b[i1];
                    // use the temp and save it to a[i1+1]
                    b[i1] = temp;
                }
            }
        }

        // print the array an see what order its in
        for(int j=0;j<b.length;j++){
            System.out.println(b[j]);
        }




    }
}

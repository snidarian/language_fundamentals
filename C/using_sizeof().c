// Concisely illustrating the use of sizeof() operator/function

#include <stdio.h> 



int main() 
{ 


    /*
    1. When operand is a Data Type.
    When sizeof() is used with the data types such as int, float, char… etc it simply returns the amount of memory is allocated to that data types.
    
    Note sizeof() may give different output when used on standard data types on a machine by machine basis
    
    */

    printf("char = %lu\n", sizeof(char)); 
    printf("int = %lu\n", sizeof(int)); 
    printf("float = %lu\n", sizeof(float)); 
    printf("double = %lu\n", sizeof(double)); 
    


    /*
    2. When operand is an expression.
    When sizeof() is used with the expression, it returns size of the expression. Let see example:
    */

    // result of sizeof(int + double) returns the size of a double.
    int a = 0;
    double d = 10.21;
    printf("Addition of int and double yields double of size: %lu bytes\n", sizeof(a + d));


    /*
    Need of Sizeof
    1. To find out number of elements in a array.
    Sizeof can be used to calculate number of elements of the array automatically. Let see Example :
    */

    int arr[] = { 1, 2, 3, 4, 7, 98, 0, 12, 35, 99, 14 }; 
    printf("Number of elements = %lu \n", sizeof(arr) / sizeof(arr[0])); 
    printf("each element in this array is %d bytes\n", sizeof(arr[0]));

    /*
    2. To allocate a block of memory dynamically
    sizeof is greatly used in dynamic memory allocation. For example, if we want to allocate memory for which is sufficient to hold 10
    integers and we don't know the sizeof(int) in that particular machine. We can allocate with the help of sizeof.
    */

    // int* ptr = (int*)malloc(10 * sizeof(int));



    return 0;

} 









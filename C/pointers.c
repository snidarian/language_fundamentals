
/*
some rules regarding arithmetic for pointers in C:

    A pointer variable can be assigned to the address of an ordinary variable.
    Pointers can be initialized or assigned as NULL; NULL is the symbolic representation of zero.
    An integer type variable can be added or subtracted from a pointer variable.
    Pointers in C can’t be divided or subtracted by a constant.
    Two pointer variables can’t be added.
    C pointers cannot be assigned to an ordinary variable.
*/

#include <stdio.h>


int main()
{
    // initialization of a pointer
    int* pointer;
    // initialization of non-pointer variable
    int number = 45;

    // You initialize a pointer variable by assigning the name reference of another variable (with &) to it
    pointer = &number;


    printf("The pointer will display address of number variable as it's value\n"); // and the number variable will display its own value
    //  Below we are asking to see the value of the pointer and the address of the variable "number"
    printf("pointer value = %d, number address = %d\n", pointer, &number);
    // Below we are asking for the pointers actual address, not its value which is the address of the variable it points to
    printf("pointers actual address = %d\n", &pointer);

    return 0;
}



// simple program illustrating the use of variables in C
// C is a statically types langauge - meaning the type of each variable is known at the time of compilation

#include <stdio.h>

int main()
{
    // The bytes of ints, shorts and longs are all machine dependant BUT:
    // on a given machine, ints >= shorts and longs > shorts/ints
    int a = 5; // %d
    short int b = 10; // %d
    long int c = 15; // %ld
    
    float d = 65.5;
    double e = 100.45693;
    char f = 'f';
    char g[30] = "string_of_chars";


    printf("%d\n", a);
    printf("%d\n", b);



    return 0;

}



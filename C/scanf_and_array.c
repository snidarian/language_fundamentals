// This is just a C file to practice with using arrays in C programming
// uses scanf to reive 10 items of input and then outputs the items.

#include <stdio.h>
#include <stdlib.h>

int main() {
    
    int selectIndex = 3;
    int i;

    // Initialization of values within an array. Note that this requires the curly brackets below. Belows sets every element to the value between {}
    int a[10] = {0};
    int b[20] = {1};
    int c[30] = {2};
    int d[40] = {3};

    for (i = 0; i < 10 ; i++)
        printf("enter a number: \n") && scanf("%d", &a[i]);
        // A first I typed printf and scanf statements on two separate lines. It didn't wait for scanf to take input but...
        // Then I fixed this by putting an AND statment between the printf and scanf which fixed the problem.
for (i=0;i<10;i++) {
    printf("%d\n", a[i]);
}

    return 0;

}




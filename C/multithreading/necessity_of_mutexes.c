// C program demonstrating use of multiple threads

#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <pthread.h> 


int global = 0;


void *thread_function(void *vargp)
{
    int *myid = (int *)vargp;

    static int s = 0;

    ++s; ++global;

    printf("Thread ID: %d, static: %d, Global: %d\n", *myid, s, global);
}

int main()
{
    int i;
    pthread_t id0;
    pthread_t id1;
    pthread_t id2;

        pthread_create(&id0, NULL, thread_function, (void *)&id0);
        pthread_create(&id1, NULL, thread_function, (void *)&id1);
        pthread_create(&id2, NULL, thread_function, (void *)&id2);
    

    pthread_exit(NULL);
    return 0;
}


// What is the problem with this program?

// There are three thread accessing the same global variable. Generally this is a bad idea.
// If multiple threads really must access a single global variable the use of a 'mutex' is required for coherent results.




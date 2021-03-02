// Basic c file demonstrating implementation of multithreading
// compile with -lpthread option to add the pthread.h header

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void *thread_function(void *vargp) 
{ 
    sleep(1); 
    printf("Printing a text message from thread \n"); 
    return NULL; 
} 
   
int main() 
{ 
    // pthread_t is a data type
    pthread_t thread_id; 
    printf("Before Thread\n");

    // After declaring thread_id, pthread_create() function creates the thread
    /* pthread_create() takes 4 args:
    1. pointer to thread_id which is set by this function
    2. specifies attributes, if NULL then default attributes are set
    3. name of function to be executed for the thread to be created
    4. 4th arg is used to pass arguments to the function
    */
    pthread_create(&thread_id, NULL, thread_function, NULL); 
    
    // pthread_join() function is the equivalent of wait() for processess.
    // A call to pthread_join blocks the calling thread until thread with identifier equal to the first argument terminates
    pthread_join(thread_id, NULL); 
    
    printf("After Thread\n"); 
    
    exit(0); 
}


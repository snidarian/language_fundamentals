// Basic c file demonstrating implementation of multithreading

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
    pthread_t thread_id; 
    printf("Before Thread\n");

    pthread_create(&thread_id, NULL, thread_function, NULL); 
    pthread_join(thread_id, NULL); 
    
    printf("After Thread\n"); 
    
    exit(0); 
}


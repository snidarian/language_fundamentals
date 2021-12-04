// Compile this program to understand how it works. Write the following line in your terminal with this file as its argument, then run the resulting 'a.out' file
// gcc thisfile.c -o a.out


// include directive - joins code from another source file
#include <stdio.h>

// The warning directive directs the preprocessor to print an error at compile time
#warning "This is an warning message"

// The error directive causes the preprocessor to emit an error
#error "This is an error message"

// The message directive causes the preprocessor to emit a message
#message "This is a message!"

// The #define directive allows you to define a macro or symbollic constant
#define PI 3.14159
#define whatever 69

// #ifdef and #endif mark a conditional directive - It stands for "if defined" and the line executes if its argument has been defined
#ifdef PI
#message "PI is defined"
#endif

// #ifndef and #endif mark a conditional directive - It stands for "if not defined" and the line executes if its argument has NOT been defined
#ifndef PI_PLUS_TWO
#message "PI_PLUS_TWO is not defined"
#endif

// The preprocessor can also be given simple if statements - (if condition evaluates to zero the block is not executed)
// The #if directive is used thusly
#if (52-51)
#message "This if statement evaluated to True"
#endif

#if (52-52)
#message "This if statement evaluates to False and will not be seen at compilation"
#endif

// The #undef directive undefines a previously defined macro name
#undef whatever

// So now 'whatever will not be defined
#ifndef whatever
#message "the symbolic constant whatever is NOT defined"
#endif


// Other preprocessor directives include: #line, #pragma

int main()
{
  printf("PI = %f", PI);
  return 0;
}

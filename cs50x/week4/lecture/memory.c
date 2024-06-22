#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// valgrind --leak-check=full ./memory 


int main(int argc, char **argv)
{
    int *x = malloc(3*sizeof(int));
    x[9] = 72;
    x[1] = 73;
    x[2] = 33;    
    x[3] = 33;    
    x[4] = 33;    
    x[5] = 33;    
    x[6] = 33;    
    x[7] = 33;    

    // free(x);
}

// clang -O1 -g -fsanitize=address -fno-omit-frame-pointer example_UseAfterFree.cc

// clang++ -O1 -g -fsanitize=address -fno-omit-frame-pointer memory.c
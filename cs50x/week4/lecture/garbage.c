#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void do_unitialized(void)
{
    int scores[1024];
    for (int i = 0; i < 1024; i++)
        scores[i] = 0;

    for (int i = 0; i < 1024; i++)
    {
        printf("%1$i scores[%1$i]: %2$i;", i, scores[i]);
        // printf("\n");
    }
}

void do_other_memory()
{
    int *x;
    int *y;
    x = malloc(sizeof(int));

    *x = 42;
    // *y = 13;

    y = x;
    *y = 13;
    free(x);
}

int main(int argc, char **argv)
{
    do_unitialized();
    do_other_memory();
}

// clang -O1 -g -fsanitize=address -fno-omit-frame-pointer example_UseAfterFree.cc

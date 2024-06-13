
#include <cs50.h>
#include <stdio.h>
#include <string.h>

#ifndef TEST
int main(int argc, char **argv)
{
    int number =50;
    int *p = &number;
    printf("%p\n", p);
}
#endif


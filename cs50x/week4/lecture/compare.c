#include <cs50.h>
#include <stdio.h>
#include <string.h>

#ifndef TEST
int main(int argc, char **argv)
{
    char *i = get_string("i: ");
    char *k = get_string("k: ");

    printf("\n");
    printf("%1$s: \t %1$p\n", i);
    printf("%1$s: \t %1$p\n", k);


    string proof = "";

    if (i != k)
    {
        proof = "not ";
    }

    printf("'%s' and '%s' are %sthe same.\n", i, k, proof);

    proof = "";
    if (strcmp(i, k) != 0)
    {
        proof = "not ";
    }
    printf("'%s' and '%s' are %sthe same.\n", i, k, proof);
}
#endif

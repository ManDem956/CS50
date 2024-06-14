#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifndef TEST
int main(int argc, char **argv)
{
    char *s = get_string("s: ");
    if (s == NULL)
    {
        return 1;
    }

    char *t = malloc(strlen(s)+1);
    if (t == NULL)
    {
        return 1;
    }
    strcpy(t, s);

    printf("\n");

    if (strlen(t) > 0)
        t[0] = toupper(t[0]);

    // t[3] = 0;

    printf("%s\n", s);
    printf("%s\n", t);

    free(t);
    return 0;
}
#endif
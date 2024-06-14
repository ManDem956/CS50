#include <stdio.h>
#include <string.h>

void int_pointers()
{
    int number = 50;
    int *p = &number;
    printf("&number:\t\t%p\n", &number);
    printf("p:\t\t\t%p\n", p);
    printf("*p:\t\t\t%i\n", *p);
}

void str_pointers()
{
    char *s = "HI!";
    printf("s: \t\t\t%s\n", s);
    printf("s pointer: \t\t%p\n", s);
    for (int i = 0, len = strlen(s); i < len; i++)
    {
        printf("s[%i]: %c = %d pointer: \t%p\n", i, s[i], s[i], &s[i]);
    }

    for (int i = 0, len = strlen(s); i < len; i++)
    {
        printf("s[%i]: %c = %d pointer: \t%c\n", i, s[i], s[i], *(s+i));
    }


}

#ifndef TEST
int main(int argc, char **argv)
{
    int_pointers();
    str_pointers();
}
#endif

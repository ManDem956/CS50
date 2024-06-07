#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *build_str(int length, string filler)
{
    string str = malloc(length + 1);
    memset(str, *filler, length);
    str[length] = '\0';
    return str;
}

int main(void)
{
    int count = 0;
    do
    {
        count = get_int("Height: ");
    } 
    while (0 >= count || count > 8);

    for (int i = 1; i < count + 1; i++)
    {
        int rest = count - i;
        char *spaces = build_str(rest, " ");
        char *str = build_str(i, "#");

        printf("%s%s  %s\n", spaces, str, str);
    }
}
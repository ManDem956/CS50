#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#define __STDC_WANT_LIB_EXT1__ 1
#include <string.h>

char *create_string(int length, const char *filler)
{
    char *str = malloc(length + 1);
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
        char *spaces = create_string(rest, " ");
        char *str = create_string(i, "#");

        printf("%s%s  %s\n", spaces, str, str);

        free(spaces);
        free(str);
    }
}
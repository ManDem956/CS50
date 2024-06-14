#include <stdio.h>
#include <stdlib.h>

int getint(char *prompt);
char *getstr(char *prompt);

int main(int argc, char **argv)
{
    int n = getint("Integer value");
    printf("n: %i\n", n);

    printf("User's input: %s\n", getstr("String value"));
}


// bug: does not validate input, attempt to convert alpha to int
int getint(char *prompt)
{
    int result;
    printf("%s: ", prompt);
    scanf("%i", &result);
    return result;
}

// bug; mo proper memory allocation, 
// string get cut off at nearest whitespace at least
char* getstr(char *prompt)
{    
    // char result[4];
    char *result = malloc(3 * sizeof(char));
    printf("%s: ", prompt);
    scanf("%s", result);
    return result;
}
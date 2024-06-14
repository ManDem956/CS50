#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

#define HEADER "name,phone"

int main(int argc, char **argv)
{
    FILE *file = fopen("phonebook.csv", "w");
    fprintf(file, "%s\n", HEADER);
    fclose(file);

    char *name = get_string("Name: ");
    char *number = get_string("phone: ");

    file = fopen("phonebook.csv", "a");

    while ((name != NULL) || (number != NULL))
    {
        fprintf(file, "%s,%s\n", name, number);
        name = get_string("Name: ");
        number = get_string("phone: ");
    } 
    printf("\n");

    fclose(file);
}


#ifndef INHERITANCE_H
#define INHERITANCE_H

#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct person
{
    struct person *parents[2];
    char alleles[2];
} person;

const int GENERATIONS = 3;
const int INDENT_LENGTH = 4;

person *create_family(int generations);
void print_family(person *p, int generation);
void free_family(person *p);
char random_allele();

#endif //INHERITANCE_H


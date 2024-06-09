#ifndef READABILITY_H
#define READABILITY_H

#include <cs50.h>
#include <regex.h>

void match(regex_t regex, string text, int *result);

void stats(string pattern, string text, int cflags, int *buff);

int getAStat(string regex_expr, string text, int idx);

int calculate(int wordCount, int letterCount, int sentenceCount);

#endif

#include <cs50.h>
#include <math.h>
#include <regex.h>
#include <stdio.h>
#include <string.h>

// const string REG_WORDS = "[[a-zA-Z0-9]'-]*[\\,.!?:;\\)]?";
const string REG_WORDS = "[a-z0-9-]+[^ \n\r]*[a-z0-9-]*";
const string REG_LETTERS = "[a-z0-9]+";
const string REG_SENTENCES = "[.!?]";

void match(regex_t regex, string text, int *result)
{
    int eflags = 0;
    regoff_t offset = 0;
    size_t length = strlen(text);
    regmatch_t whole_match;

    while (regexec(&regex, text + offset, 1, &whole_match, eflags) == 0)
    {
        eflags = REG_NOTBOL;
        regoff_t end = offset + whole_match.rm_eo;
        regoff_t start = offset + whole_match.rm_so;

        result[0] += 1;

        regoff_t len = end - start;
        result[1] += len;
        // char substr[len + 1];
        // strncpy(substr, text + start, len);
        // substr[len] = 0;

        // printf("range %i - %i : %i: %s\n", start, end, end - start, substr);
        offset += whole_match.rm_eo;

        if (offset >= length)
        {
            break;
        }
    }
}

void stats(string pattern, string text, int cflags, int *buff)
{
    regex_t regex;
    int result = regcomp(&regex, pattern, cflags);

    if (result != 0)
    {
        printf("regcomp: %d\n", result);
    }
    match(regex, text, buff);
}

int calculate(int wordCount, int letterCount, int sentenceCount)
{
    float letterPerWords = ((float) letterCount / (float) wordCount) * 100;
    float sentencePerWords = ((float) sentenceCount / (float) wordCount) * 100;
    float CLI = 0.0588 * letterPerWords - 0.296 * sentencePerWords - 15.8;

    // printf("Words: %i\nLetters: %i\nSentences: %i\n", wordCount, letterCount,
    //        sentenceCount);
    // printf("L: %f\nS: %f\nCLI: %f\n", letterPerWords, sentencePerWords, CLI);

    return round(CLI);
}

int main(void)
{
    string text = get_string("Text: ");

    int match_stats[] = {0, 0};

    stats(REG_WORDS, text, REG_EXTENDED | REG_ICASE, match_stats);
    int wordCount = match_stats[0];

    match_stats[0] = match_stats[1] = 0;
    stats(REG_LETTERS, text, REG_EXTENDED | REG_ICASE, match_stats);
    int letterCount = match_stats[1];

    match_stats[0] = match_stats[1] = 0;
    stats(REG_SENTENCES, text, REG_EXTENDED | REG_ICASE, match_stats);
    int sentenceCount = match_stats[0];

    int CLI = calculate(wordCount, letterCount, sentenceCount);

    if (CLI < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (CLI > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) CLI);
    }
}

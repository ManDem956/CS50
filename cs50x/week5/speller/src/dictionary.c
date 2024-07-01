// Implements a dictionary's functionality

#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// hash data
const unsigned int M_MOD = 10000019; // 664580-th prime number
const unsigned char PRIME = 31;
unsigned int hashLength = 12;
unsigned long long *primePowersCache;
unsigned int (*charHashMruCache)[26];

// stats *wordLengths;

// Choose number of buckets in hash table
// Number of buckets can not be larger than the mod remainder
const unsigned int N = M_MOD;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{

    unsigned int result = 0;

    // choose current hash length, can not be longer than the length o0f the original word
    unsigned char length = hashLength > strlen(word) - 1 ? strlen(word) - 1 : hashLength;

    for (int i = length; i > 0; i--)
    {
        char current = tolower(word[i]);
        if (current != '\'')
        {
            unsigned char char_value = current - 'a' + 1;

            // Check the MRU cache first
            if (charHashMruCache[char_value][i] > 0)
                return charHashMruCache[char_value][i];

            // Hash is calculated as
            // (s[0] + s[1]*p + s[2]*p^2 + ... + s[n-1]*p^(n-1) + s[n]*p^(n)) mod m
            // where
            // - p = 31 (a prime number closest to number of lowercased characters in english ABC)
            // - m = 10000009 (la)
            result = (result + char_value * primePowersCache[i]) % M_MOD;
            charHashMruCache[char_value][i] = result;
        }
    }

    return result;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *fp = fopen(dictionary, "rt");
    initHashSettings(fp);

    char line[LENGTH + 1];
    while (!feof(fp))
    {
        if (fgets(line, LENGTH + 1, fp))
        {
            unsigned int currentHash = hash(line);
            node *new = calloc(1, sizeof(node));
            if (new == NULL)
            {
                for (char bucket = 0; bucket < 26; bucket++)
                    unload();
                return 1;
            }

            strcpy(new->word, line);
            // new->word = line;
            new->next = table[currentHash];

            table[currentHash] = new;
        }
    }
    fclose(fp);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

bool unload_bucket(node *list)
{
    while (list != NULL)
    {
        node *tmp = list->next;
        free(list);
        list = tmp;
    }
    return (list == NULL);
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO

    for (int i = 0; i < N; i++)
    {
        unload_bucket(table[i]);
    }
    free(primePowersCache);
    free(charHashMruCache);
    return false;
}

void statFile(FILE *fp, stats *wordLengths)
{
    rewind(fp);
    unsigned int count = 0;
    char line[LENGTH + 1];
    while (!feof(fp))
    {
        if (fgets(line, LENGTH + 1, fp))
        {
            int length = strlen(line);
            if (length > 0)
            {
                wordLengths[length].length = length;
                wordLengths[length].count++;
                count++;
            }
        }
    }
    rewind(fp);

    for (int i = 0; i < LENGTH + 1; i++)
    {
        float ratio = wordLengths[i].count / (float) count;
        wordLengths[i].ratio = ratio;
        float lengthWeight = round(ratio * 100) > 0 ? (float) LENGTH / wordLengths[i].length : 0;
        wordLengths[i].weight =
            round(((lengthWeight * ratio) * 0.6) * 1000 + wordLengths[i].ratio * 1000 * 0.4);
    }
    do_sort(LENGTH + 1, wordLengths);
}

void initHashSettings(FILE *fp)
{
    stats *wordLengths = calloc((LENGTH + 1), sizeof(stats));
    statFile(fp, wordLengths);
    hashLength = checkMaxHashLength(wordLengths[0].length);
    free(wordLengths);

    primePowersCache = calloc(hashLength, sizeof(*primePowersCache));
    charHashMruCache = calloc(hashLength, sizeof(charHashMruCache[26]));
    unsigned long long pPow = 1;
    for (int i = 0; i < hashLength; i++)
        pPow = (pPow * PRIME) % M_MOD;
}

unsigned int checkMaxHashLength(unsigned int currentLength)
{
    unsigned long long pPow = 1;
    unsigned int result = currentLength;
    for (int i = 0; i < currentLength + 1; i++)
    {
        unsigned long long value;
        if (__builtin_umulll_overflow(pPow, PRIME, &value))
        {
            // Overflow detected
            result = i;
            break;
        }
        pPow = value;
    }
    return result;
}

void swap(stats *left, stats *right)
{
    stats temp = *left;
    *left = *right;
    *right = temp;
}

void do_sort(size_t size, stats n[])
{
    int i;
    bool swapped;
    do
    {
        i = size - 1;
        swapped = false;
        while (i > 0)
        {
            if (n[i - 1].weight < n[i].weight)
            {
                swap(&n[i - 1], &n[i]);
                swapped = true;
            }
            i--;
        }
    }
    while (swapped);
}

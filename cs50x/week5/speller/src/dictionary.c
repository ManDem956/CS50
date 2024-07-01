// Implements a dictionary's functionality

#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// hash data
const unsigned int M_MOD = 10000019 + 1; // 664580-th prime number
const unsigned char PRIME = 31;
unsigned int hashLength = 12;
unsigned long long *primePowersCache;

unsigned int dictionarySize = 0;

// stats *wordLengths;

// Choose number of buckets in hash table
// Number of buckets can not be larger than the mod remainder
const unsigned int N = M_MOD;

// Hash table
node *table[N];

// local function prototypes
bool unload_bucket(node *list);

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // for ( ; *word; ++word) *word = tolower(*word);
    unsigned int currentHash = hash(word);
    // if (table[currentHash] != NULL)
    // {

    const char *lastPart = &word[0];
    if (strlen(word) > hashLength)
        lastPart = &word[hashLength];

    node *currentWord = table[currentHash];
    while (currentWord != NULL)
    {
        // if (wordLength < hashLength)
        //     return true;
        const char *currentLastPart = &(currentWord->word)[0];
        if (strlen(currentWord->word) > hashLength)
            currentLastPart = &(currentWord->word)[hashLength];

        if (strcasecmp(lastPart, currentLastPart) == 0)
            return true;
        currentWord = currentWord->next;
    }
    // }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Hash is calculated as
    // (s[0] + s[1]*p + s[2]*p^2 + ... + s[n-1]*p^(n-1) + s[n]*p^(n)) mod m
    // where
    // - p = 31 (a prime number closest to number of lowercased characters in english ABC)
    // - m = 10000009 (la)

    unsigned int result = 0;

    // choose current hash length, can not be longer than the length of the original word
    unsigned char length = hashLength > strlen(word) ? strlen(word) : hashLength;

    for (int i = 0; i < length; i++)
    {
        char current = tolower(word[i]);

        unsigned char char_value = current - 'a';
        unsigned int charHash = (char_value + 1) * primePowersCache[i];
        result = (result + charHash) % M_MOD;
    }

    return result;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *fp = fopen(dictionary, "rt");
    hashLength = 5;
    // initHashSettings(fp);
    initPrimePowerCache();

    char line[LENGTH + 1];
    while (!feof(fp))
    {
        if (fgets(line, LENGTH + 1, fp))
        {
            line[strcspn(line, "\n\r")] = 0;
            if (strlen(line) <= 0)
                continue;

            dictionarySize++;

            for (int i = 0; line[i]; i++)
            {
                line[i] = tolower(line[i]);
            }

            unsigned int currentHash = hash(line);
            node *new = calloc(1, sizeof(node));
            if (new == NULL)
            {
                for (unsigned int bucket = 0; bucket < ABCLENGTH; bucket++)
                    unload_bucket(table[bucket]);
                return 1;
            }

            strcpy(new->word, line);
            // new->word = line;
            new->next = table[currentHash];

            table[currentHash] = new;
        }
    }
    fclose(fp);

    // print_buckets();

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return dictionarySize;
}

bool unload_bucket(node *list)
{
    while (list != NULL)
    {
        node *tmp = list->next;
        // printf("Freeing pointer : %p\n", list);
        free(list);
        list = tmp;
    }
    return (list == NULL);
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    bool result = true;
    // printf("Unloading.....\n");
    for (int i = 0; i < N; i++)
    {

        if (table[i] != NULL)
        {
            // printf("Bucket # %i : %p\n", i, table[i]);
            result = unload_bucket(table[i]);
        }
    }
    free(primePowersCache);
    return result;
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
        float lengthWeight = round(ratio * 100) > 0 ? (float) LENGTH / wordLengths[i].length : 0;
        wordLengths[i].weight = round((lengthWeight * 0.1) * 1000 + ratio * 1000 * 1.9);
    }
    do_sort(LENGTH + 1, wordLengths);
}

void initPrimePowerCache()
{
    primePowersCache = malloc(hashLength * sizeof(*primePowersCache));
    unsigned long long pPow = 1;
    for (int i = 0; i < hashLength; i++)
    {
        primePowersCache[i] = pPow;
        pPow = (pPow * PRIME) % M_MOD;
    }
}

void initHashSettings(FILE *fp)
{
    stats *wordLengths = calloc((LENGTH + 1), sizeof(stats));
    statFile(fp, wordLengths);
    hashLength = checkMaxHashLength(wordLengths[0].length);
    free(wordLengths);
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

void print_buckets(void)
{
    unsigned long sum_sq = 0;
    int num_words = (int)size();

    // use dynamic memory allocation instead of the stack for these arrays,
    // in order to prevent a possible stack overflow
    int *collisionCount = calloc(num_words, sizeof *collisionCount);
    int *bucketCounter  = calloc(N, sizeof *bucketCounter);
    if (bucketCounter == NULL || collisionCount == NULL)
    {
        printf("Memory allocation error!\n");
        exit(EXIT_FAILURE);
    }

    // fill bucketCounter array
    for (int i = 0; i < N; i++)
    {
        for (node *p = table[i]; p != NULL; p = p->next)
        {
            bucketCounter[i]++;
        }
    }

    // fill collisionCount array
    for (int i = 0; i < N; i++)
    {
        collisionCount[bucketCounter[i]]++;
    }

    // print content of collisionCount array and update sum_sq
    for (int i = 0; i < num_words; i++)
    {
        if (collisionCount[i])
        {
            sum_sq += (long) i * i * collisionCount[i];
            printf("Buckets with %i nodes: %i\n", i, collisionCount[i]);
        }
    }

    // print final information
    printf("\n");
    printf("Sum  of squares: %lu\n",  sum_sq);
    printf("Mean of squares: %.3f\n", (double)sum_sq / num_words);

    // Exit the program prematurely, so that you can see the diagnostic output
    // instead of the misspelled words. Exiting prematurely will cause memory leaks,
    // so don't run this function with valgrind.
    exit(EXIT_SUCCESS);
}
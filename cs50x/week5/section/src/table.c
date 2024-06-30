#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
    string phrase;
    struct node *next;
} node;

node *table[26];

int hash(string phrase);
bool unload(node *list);
void visualizer(node *list);

int main(void)
{
    // Add items
    for (int i = 0; i < 3; i++)
    {
        string phrase = get_string("Enter a new phrase: ");

        // Find phrase bucket
        int bucket = hash(phrase);
        printf("%s hashes to %i\n", phrase, bucket);
        node *new = malloc(sizeof(node));
        if (new == NULL)
        {
            for (char bucket = 0; bucket < 26; bucket++)
                unload(table[bucket]);
            return 1;
        }

        new->phrase = phrase;
        new->next = table[bucket];

        table[bucket] = new;
    }

    for (char bucket = 'A'; bucket < 'Z'; bucket++)
    {

        if (table[bucket - 'A'] != NULL)
        {
            printf("Bucket of [%c]:\n", toupper(bucket));
            visualizer(table[bucket - 'A']);
        }
    }

    for (char bucket = 0; bucket < 26; bucket++)
        unload(table[bucket]);
}

// return the correct bucket for a given phrase
int hash(string phrase)
{
    int result = toupper(phrase[0]) - 'A';
    if ((0 <= result) && (result <= 26))
        return result;
    return -1;
}

bool unload(node *list)
{
    while (list != NULL)
    {
        node *tmp = list->next;
        free(list);
        list = tmp;
    }
    return (list == NULL);
}

void visualizer(node *list)
{
    if (list == NULL)
        return;

    printf("\n+-- List Visualizer --+\n\n");
    while (list != NULL)
    {
        printf("Location %p\nPhrase: \"%s\"\nNext: %p\n\n", list, list->phrase, list->next);
        list = list->next;
    }
    printf("+---------------------+\n\n");
}
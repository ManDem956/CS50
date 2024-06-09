
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *encode(string s, int key)
{
    string result = malloc(sizeof(char) * strlen(s) + 1);
    strcpy(result, s);
    // make sure key is a remainder of 26
    key = key % 26;

    // for decoding purposes, we reverse the key value
    if (key < 0)
    {
        key = 26 + key;
    }

    for (int i = 0; i < strlen(s); i++)
    {
        // avoiding multiple if statements - treat everything as uppercase
        char upper = toupper(result[i]);
        if ('A' <= upper && upper <= 'Z')
        {
            // store the diff between lowercase and uppercase character
            // We need this to factor in both lowercase and uppercase inputs
            int diff = result[i] - upper;

            result[i] = (upper - 'A' + key) % 26 + 'A' + diff;
        }
    }
    return result;
}

char *decode(string s, int key)
{
    return encode(s, key * -1);
}

void do_run(int key)
{
    string text = get_string("Text: ");

    printf("plaintext: %s\n", text);
    printf("ciphertext: %s\n", encode(text, key));
    printf("decoded: %s\n", decode(encode(text, key), key));
}

int main(int argc, char **argv)
{
    if ((argc != 2) || (!(strspn(argv[1], "-+0123456789") == strlen(argv[1]))))
    {
        printf("Usage: ./caesar key\n\t key: an integer value to shift the "
               "sypher on.\n");
        return 1;
    }

    int key = atoi(argv[1]);
    do_run(key);
}

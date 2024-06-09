
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>


#define MAX_KEY_LENGTH 26
#define VALIDATE "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

// const string VALIDATE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

char *to_upper(string s);

char *encode(string s, string key)
{
    string result = malloc(sizeof(char) * strlen(s) + 1);
    strcpy(result, s);
    key = to_upper(key);
    for (int i = 0; i < strlen(s); i++)
    {
        // avoiding multiple if statements - treat everything as uppercase
        char upper = toupper(result[i]);

        if ('A' <= upper && upper <= 'Z')
        {
            // store the diff between lowercase and uppercase character
            // We need this to factor in both lowercase and uppercase inputs
            int diff = result[i] - upper;

            result[i] = key[upper - 'A'] + diff;
        }
    }
    return result;
}

char *to_upper(string s){
    string result = malloc(sizeof(char) * strlen(s) + 1);
    strcpy(result, s);
    for (int i = 0; i < strlen(result); i++){
        result[i] = toupper(result[i]);
    }
    return result;

}

void do_run(string key)
{
    string text = get_string("plaintext: ");
    printf("ciphertext: %s\n", encode(text, to_upper(key)));
}

// int main(int argc, char **argv)
// {
//     if ((argc != 2) ||
//         (strlen(argv[1]) != MAX_KEY_LENGTH) && (strspn(argv[1], VALIDATE) != MAX_KEY_LENGTH))
//     {
//         printf("Usage: ./caesar key\n\t key: a string of length 26 to base the "
//                "substitution cipher on.\n");
//         return 1;
//     }

//     string key = argv[1];
//     do_run(key);
// }

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

const int NUM_PLAYERS = 2;
const int values[] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                      1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int calculate_score(string word)
{
    int result = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        int idx = toupper(word[i]) - 'A';
        if (idx >= 0 && idx < 26)
        {
            result += values[idx];
        }
    }
    return result;
}

int main(void)
{
    int player_scores[NUM_PLAYERS];
    int max_score[2] = {0, 0};

    for (int i = 0; i < NUM_PLAYERS; i++)
    {
        string word = get_string("Player %i, What is your word? ", i + 1);
        player_scores[i] = calculate_score(word);
    }

    for (int i = 0; i < NUM_PLAYERS; i++)
    {
        int score = player_scores[i];
        // printf("Player %i score: %i\n", i + 1,
        // player_scores[i]);
        if (max_score[1] < score)
        {
            max_score[0] = i + 1;
            max_score[1] = score;
        }
        else if (max_score[1] == score)
        {
            max_score[0] = 0;
        }
    }

    if (max_score[0] > 0)
    {
        printf("Player %i wins!\n", max_score[0], max_score[1]);
    }
    else
    {
        printf("It's a tie!\n");
    }
}
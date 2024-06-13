#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    for (int idx_cnd = 0; idx_cnd < candidate_count; idx_cnd++)
    {
        if (strcmp(candidates[idx_cnd], name) == 0)
        {
            ranks[rank] = idx_cnd;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int idx_winner = 0; idx_winner < (candidate_count - 1); idx_winner++)
    {
        for (int idx_loser = idx_winner + 1; idx_loser < candidate_count; idx_loser++)
        {
            int winner = ranks[idx_winner];
            int loser = ranks[idx_loser];
            preferences[winner][loser] += 1;
        }
    }
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    pair_count = 0;
    for (int idx_left = 0; idx_left < (candidate_count - 1); idx_left++)
    {
        for (int idx_right = idx_left + 1; idx_right < candidate_count; idx_right++)
        {
            // Store winner and loser in a candidate pair
            if (preferences[idx_left][idx_right] != preferences[idx_right][idx_left])
            {
                if (preferences[idx_left][idx_right] > preferences[idx_right][idx_left])
                {
                    pairs[pair_count].winner = idx_left;
                    pairs[pair_count].loser = idx_right;
                }
                else
                {
                    pairs[pair_count].winner = idx_right;
                    pairs[pair_count].loser = idx_left;
                }
                pair_count += 1;
            }
        }
    }
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    bool swapped;
    do
    {
        int idx = pair_count - 1;
        swapped = false;
        while (idx > 0)
        {
            if (preferences[pairs[idx - 1].winner][pairs[idx - 1].loser] <
                preferences[pairs[idx].winner][pairs[idx].loser])
            {
                pair temp = pairs[idx - 1];
                pairs[idx - 1] = pairs[idx];
                pairs[idx] = temp;
                swapped = true;
            }
            idx -= 1;
        }
    }
    while (swapped);
}

int is_a_path(int winner, int loser)
{
    if (locked[winner][loser])
    {
        return true;
    }

    for (int idx_cnd = 0; idx_cnd < candidate_count; idx_cnd++)
    {
        if ((locked[winner][idx_cnd]) && is_a_path(idx_cnd, loser))
        {
            return true;
        }
    }

    return false;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    for (int idx_pair = 0; idx_pair < pair_count; idx_pair++)
    {
        int winner = pairs[idx_pair].winner;
        int loser = pairs[idx_pair].loser;
        locked[winner][loser] = !is_a_path(loser, winner);
    }
}

string get_winner()
{
    for (int idx_win_cndt = 0; idx_win_cndt < candidate_count; idx_win_cndt++)
    {
        // check if the second loop uncovers a winner over current candidate
        // if it is not than this is the root node
        bool winner = true;
        for (int idx_winner = 0; idx_winner < candidate_count; idx_winner++)
        {
            if (locked[idx_winner][idx_win_cndt])
            {
                winner = false;
            }
        }
        if (winner)
        {
            return candidates[idx_win_cndt];
        }
    }
    return NULL;
}

// Print the winner of the election
void print_winner(void)
{
    printf("%s\n", get_winner());
}

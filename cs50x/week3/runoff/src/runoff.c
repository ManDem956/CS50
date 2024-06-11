#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
} candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    int idx_candidate = 0;
    while (idx_candidate < candidate_count)
    {
        if (strcmp(candidates[idx_candidate].name, name) == 0)
        {
            preferences[voter][rank] = idx_candidate;
            return true;
        }
        idx_candidate++;
    }
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    for (int idx_vote = 0; idx_vote < voter_count; idx_vote++)
    {
        for (int idx_pref = 0; idx_pref< candidate_count; idx_pref++){
            int idx_candidate = preferences[idx_vote][idx_pref];
            if (!candidates[idx_candidate].eliminated){
                candidates[idx_candidate].votes+=1;
                break;
            }
        }

    }
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    int win_rate = voter_count / 2 + 1;
    int votes_pool = voter_count;
    int idx_candidate = 0;
    while ((votes_pool >= win_rate) && (idx_candidate < candidate_count))
    {
        if (candidates[idx_candidate].votes >= win_rate)
        {
            printf("%s\n", candidates[idx_candidate].name);
            return true;
        }
        votes_pool -= candidates[idx_candidate].votes;
        idx_candidate += 1;
    }
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    int result = INT_MAX;
    for (int idx_candidate = 0; idx_candidate < candidate_count;
         idx_candidate++)
    {
        if (candidates[idx_candidate].eliminated == false)
        {
            if (result > candidates[idx_candidate].votes)
            {
                result = candidates[idx_candidate].votes;
            }
        }
    }
    return result;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    for (int idx_candidate = 0; idx_candidate < candidate_count;
         idx_candidate++)
    {
        if ((!candidates[idx_candidate].eliminated) && candidates[idx_candidate].votes != min)
        {
            return false;
        }
    }
    return true;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    for (int idx_candidate = 0; idx_candidate < candidate_count;
         idx_candidate++)
    {
        if (candidates[idx_candidate].votes == min)
        {
            candidates[idx_candidate].eliminated = true;
        }
    }
}

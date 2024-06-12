
#ifndef TIDEMAN_H
#define TIDEMAN_H

#include <cs50.h>
#include <stdio.h>
#include <string.h>

#define MAX 9


// preferences[i][j] is number of voters who prefer i over j
extern int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
// extern bool locked[][];

// Array of candidates
extern string candidates[MAX];

extern int pair_count;
extern int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

#endif //TIDEMAN_H


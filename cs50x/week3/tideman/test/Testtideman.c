
#include <cs50.h>
#include <stdio.h>
#include <string.h>

#include "../src/tideman.h"

#include "../unity/src/unity.h"

#define MAX 3
#define VOTES 5

string votes[VOTES][MAX];

void test_vote(void)
{
    int ranks[2];
    // TEST_ASSERT_EQUAL_STRING(candidates[3], "David");
    TEST_ASSERT_EQUAL(true, vote(0, candidates[0], ranks));
    TEST_ASSERT_EQUAL(false, vote(0, "WHOAMI", ranks));
    // TEST_ASSERT_EQUAL_INT16(10, pair_count);
}

void test_record_preferences(void)
{

    for (int idx_vote=0; idx_vote < VOTES; idx_vote++){
        int ranks[candidate_count];
        for (int idx_cnd=0; idx_cnd< candidate_count; idx_cnd++){
            vote(idx_cnd, candidates[idx_cnd], ranks);
        }
        record_preferences(ranks);
    }    
    TEST_ASSERT_EQUAL(5, preferences[0][1]);
    TEST_ASSERT_EQUAL(5, preferences[0][2]);
    TEST_ASSERT_EQUAL(0, preferences[1][0]);
    TEST_ASSERT_EQUAL(0, preferences[2][0]);
    TEST_ASSERT_EQUAL(5, preferences[1][2]);
    TEST_ASSERT_EQUAL(0, preferences[2][1]);

}

void test_add_pairs(void)
{

    for (int idx_vote=0; idx_vote < VOTES; idx_vote++){
        int ranks[candidate_count];
        for (int idx_cnd=0; idx_cnd< candidate_count; idx_cnd++){
            vote(idx_cnd, candidates[idx_cnd], ranks);
        }
        record_preferences(ranks);
    }    

    add_pairs();
    

}

void setUp(void)
{

    candidate_count = 3;

    candidates[0] = "Alice";
    candidates[1] = "Bob";
    candidates[2] = "Charlie";

}

void tearDown(void)
{
}

int main(int argc, char **argv)
{
    UNITY_BEGIN();
    setUp();
    RUN_TEST(test_vote);
    RUN_TEST(test_record_preferences);

    UNITY_END();
}

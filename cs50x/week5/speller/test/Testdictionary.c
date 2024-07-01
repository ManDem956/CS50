
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "../src/dictionary.h"
#include "../unity/src/unity.h"

void test_dummy(void)
{
    FILE *fp = fopen("src/dictionaries/large", "rt");
    // statFile("src/dictionaries/large");
    // statFile("src/dictionaries/small");
    stats *wordLengths = calloc((LENGTH + 1),sizeof(stats));
    statFile(fp, wordLengths);
    for (int i = 0; i <LENGTH+1; i++)
    {
        if (wordLengths[i].length > 0)
            printf("%i: %i: %i : %f :: %i\n", i, wordLengths[i].length, wordLengths[i].count,
                   wordLengths[i].ratio, wordLengths[i].weight);
    }
    fclose(fp);
    free(wordLengths);
}

void test_max_length(void)
{
    unsigned int test = checkMaxHashLength(100);
    TEST_ASSERT_EQUAL(12,test);
    // UNITY_TEST_ASSERT_EQUAL_UINT16(12,test);
}

void setUp(void)
{
}

void tearDown(void)
{
}

int main(int argc, char **argv)
{
    UNITY_BEGIN();
    RUN_TEST(test_dummy);
    RUN_TEST(test_max_length);    
    UNITY_END();
}


#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../src/substitution.h"
#include "../unity/src/unity.h"

void test_encode_hello2(void)
{
    TEST_ASSERT_EQUAL_STRING("Ehbbq!",
                             encode("Hello!", "YTNSHKVEFXRBAUQZCLWDMIPGJO"));
}

void test_encode_hello(void)
{
    TEST_ASSERT_EQUAL_STRING("FOLLE",
                             encode("HELLO", "NQXPOMAFTRHLZGECYJIUWSKDVB"));
}

void test_encode_fox(void)
{
    string test = "the quick brown fox jumps over thirteen lazy dogs";
    string key = "zyxwvutsrqponmlkjihgfedcba";
    string expected = "gsv jfrxp yildm ulc qfnkh levi gsrigvvm ozab wlth";
    TEST_ASSERT_EQUAL_STRING(expected,encode(test, key));
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
    RUN_TEST(test_encode_hello);
    RUN_TEST(test_encode_hello2);
    RUN_TEST(test_encode_fox);    
    UNITY_END();
}

// ZYXWVUTSRQPONMLKJIHGFEDCBA
// zyxwvutsrqponmlkjihgfedcba
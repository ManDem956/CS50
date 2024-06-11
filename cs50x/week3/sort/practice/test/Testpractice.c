
#include <cs50.h>
#include <stdio.h>
#include <string.h>

#include "../src/practice.h"
#include "../unity/src/unity.h"

void test_dummy(void)
{
    TEST_ASSERT_EQUAL_STRING("test", "test");
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
    UNITY_END();
}



#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../src/caesar.h"
#include "../unity/src/unity.h"

void test_encode_hi_there(void)
{
    string text = "Hi there!";
    string result = encode(text, 13);
    TEST_ASSERT_EQUAL_STRING("Uv gurer!", result);
    free(result);
}
void test_encode_hi_there_no_encode(void)
{
    string text = "Hi there!";
    string result = encode(text, 26);
    TEST_ASSERT_EQUAL_STRING(text, result);
    free(result);
}

void test_decode_hi_there_1(void)
{
    string text = "Hi there!";
    TEST_ASSERT_EQUAL_STRING(text, decode(encode(text, 1), 1));
}

void test_decode_hi_there_10(void)
{
    string text = "Hi there!";
    TEST_ASSERT_EQUAL_STRING(text, decode(encode(text, 10), 10));
}

void test_decode_hi_there_13(void)
{
    string text = "Hi there!";
    TEST_ASSERT_EQUAL_STRING(text, decode(encode(text, 13), 13));
}

void test_encode_long_text_7(void){
    string test = "If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out.";
    string expected = "Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba.";
    TEST_ASSERT_EQUAL_STRING(expected, encode(test, 7));
}

void test_encode_decode_long_text_7(void){
    string test = "If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out.";
    int key = 7;
    TEST_ASSERT_EQUAL_STRING(test, decode(encode(test, key),key));
}

void test_encode_decode_large_key(void){
    string test = "Hi there!";
    int key = 100;
    TEST_ASSERT_EQUAL_STRING(encode(test, key), encode(test, 22));
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
    RUN_TEST(test_encode_hi_there);
    RUN_TEST(test_encode_hi_there_no_encode);
    RUN_TEST(test_decode_hi_there_1);
    RUN_TEST(test_decode_hi_there_13);
    RUN_TEST(test_decode_hi_there_10);
    RUN_TEST(test_encode_long_text_7);
    RUN_TEST(test_encode_decode_long_text_7);
    RUN_TEST(test_encode_decode_large_key);    
        
    UNITY_END();
}

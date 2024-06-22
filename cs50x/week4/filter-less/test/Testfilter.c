
#include <cs50.h>
#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../src/helpers.h"
#include "../unity/src/unity.h"

int height = 3;
int width = 3;

RGBTRIPLE (*image)[3];

void test_dummy(void)
{
    // 25 22 17
    sepia(height, width, image);

    //

    TEST_ASSERT_EQUAL_UINT8(25, image[0][0].rgbtRed);
    TEST_ASSERT_EQUAL_UINT8(22, image[0][0].rgbtGreen);
    TEST_ASSERT_EQUAL_UINT8(17, image[0][0].rgbtBlue);

    //	66 58 45
    TEST_ASSERT_EQUAL_UINT8(66, image[0][1].rgbtRed);
    TEST_ASSERT_EQUAL_UINT8(58, image[0][1].rgbtGreen);
    TEST_ASSERT_EQUAL_UINT8(45, image[0][1].rgbtBlue);
    //	106 94 74
    TEST_ASSERT_EQUAL_UINT8(106, image[0][2].rgbtRed);
    TEST_ASSERT_EQUAL_UINT8(94, image[0][2].rgbtGreen);
    TEST_ASSERT_EQUAL_UINT8(74, image[0][2].rgbtBlue);
    //	170 151 118
    TEST_ASSERT_EQUAL_UINT8(170, image[1][0].rgbtRed);
    TEST_ASSERT_EQUAL_UINT8(151, image[1][0].rgbtGreen);
    TEST_ASSERT_EQUAL_UINT8(118, image[1][0].rgbtBlue);
    //	183 163 127
    TEST_ASSERT_EQUAL_UINT8(183, image[1][1].rgbtRed);
    TEST_ASSERT_EQUAL_UINT8(163, image[1][1].rgbtGreen);
    TEST_ASSERT_EQUAL_UINT8(127, image[1][1].rgbtBlue);
    //	197 175 136
    TEST_ASSERT_EQUAL_UINT8(197, image[1][2].rgbtRed);
    TEST_ASSERT_EQUAL_UINT8(175, image[1][2].rgbtGreen);
    TEST_ASSERT_EQUAL_UINT8(136, image[1][2].rgbtBlue);
    //	255 251 195
    TEST_ASSERT_EQUAL_UINT8(255, image[2][0].rgbtRed);
    TEST_ASSERT_EQUAL_UINT8(251, image[2][0].rgbtGreen);
    TEST_ASSERT_EQUAL_UINT8(195, image[2][0].rgbtBlue);
    //	255 255 214
    TEST_ASSERT_EQUAL_UINT8(255, image[2][1].rgbtRed);
    TEST_ASSERT_EQUAL_UINT8(255, image[2][1].rgbtGreen);
    TEST_ASSERT_EQUAL_UINT8(214, image[2][1].rgbtBlue);
    //	255 255 232
    TEST_ASSERT_EQUAL_UINT8(255, image[2][2].rgbtRed);
    TEST_ASSERT_EQUAL_UINT8(255, image[2][2].rgbtGreen);
    TEST_ASSERT_EQUAL_UINT8(232, image[2][2].rgbtBlue);
}

void setUp(void)
{
    int height = 3;
    int width = 3;

    // Allocate memory for image
    RGBTRIPLE(*image)[width] = calloc(height, width * sizeof(RGBTRIPLE));
    if (image == NULL)
    {
        printf("Failed to allocate memory for image.");
        exit(1);
    }

    // Initialize image
    image[0][0].rgbtRed = 10;
    image[0][0].rgbtGreen = 20;
    image[0][0].rgbtBlue = 30;

    image[0][1].rgbtRed = 40;
    image[0][1].rgbtGreen = 50;
    image[0][1].rgbtBlue = 60;

    image[0][2].rgbtRed = 70;
    image[0][2].rgbtGreen = 80;
    image[0][2].rgbtBlue = 90;

    image[1][0].rgbtRed = 110;
    image[1][0].rgbtGreen = 130;
    image[1][0].rgbtBlue = 140;

    image[1][1].rgbtRed = 120;
    image[1][1].rgbtGreen = 140;
    image[1][1].rgbtBlue = 150;

    image[1][2].rgbtRed = 130;
    image[1][2].rgbtGreen = 150;
    image[1][2].rgbtBlue = 160;

    image[2][0].rgbtRed = 200;
    image[2][0].rgbtGreen = 210;
    image[2][0].rgbtBlue = 220;

    image[2][1].rgbtRed = 220;
    image[2][1].rgbtGreen = 230;
    image[2][1].rgbtBlue = 240;

    image[2][2].rgbtRed = 240;
    image[2][2].rgbtGreen = 250;
    image[2][2].rgbtBlue = 255;
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

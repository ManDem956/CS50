
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

void check_image_pixel(RGBTRIPLE image[3][3], int row, int col, uint8_t expectedRed,
                       uint8_t expectedGreen, uint8_t expectedBlue);
void initializeImagePixels(RGBTRIPLE image[3][3], int numRows, int numColumns);

void test_sepia_filter()
{
    if (image == NULL)
    {
        TEST_FAIL_MESSAGE("Image is not initialized.");
    }

    if (height < 3 || width < 3)
    {
        TEST_FAIL_MESSAGE("Invalid image dimensions.");
    }

    sepia(height, width, image);

    check_image_pixel(image, 0, 0, 25, 22, 17);
    check_image_pixel(image, 0, 1, 66, 58, 45);
    check_image_pixel(image, 0, 2, 106, 94, 74);
    check_image_pixel(image, 1, 0, 170, 151, 118);
    check_image_pixel(image, 1, 1, 183, 163, 127);
    check_image_pixel(image, 1, 2, 197, 175, 136);
    check_image_pixel(image, 2, 0, 255, 251, 195);
    check_image_pixel(image, 2, 1, 255, 255, 214);
    check_image_pixel(image, 2, 2, 255, 255, 232);
}

void check_image_pixel(RGBTRIPLE image[3][3], int row, int col, uint8_t expectedRed,
                       uint8_t expectedGreen, uint8_t expectedBlue)
{
    TEST_ASSERT_EQUAL_UINT8(expectedRed, image[row][col].rgbtRed);
    TEST_ASSERT_EQUAL_UINT8(expectedGreen, image[row][col].rgbtGreen);
    TEST_ASSERT_EQUAL_UINT8(expectedBlue, image[row][col].rgbtBlue);
}

void test_blur_filter(void)
{
    // Check if image is initialized before using it
    if (image == NULL)
    {
        TEST_FAIL_MESSAGE("Image is not initialized.\n");
    }

    // Check if image is not out of bounds
    if (height < 3 || width < 3)
    {
        TEST_FAIL_MESSAGE("Image dimensions are invalid.\n");
    }

    blur(height, width, image);
    check_image_pixel(image, 1, 1, 127, 140, 149);
}

void setUp(void)
{
    int numRows = 3;
    int numColumns = 3;

    image = calloc(numRows, numColumns * sizeof(RGBTRIPLE));
    if (image == NULL)
    {
        printf("Failed to allocate memory for image.\n");
        exit(1);
    }

    initializeImagePixels(image, numRows, numColumns);
}

void initializeImagePixels(RGBTRIPLE image[3][3], int numRows, int numColumns)
{
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
    RUN_TEST(test_sepia_filter);
    RUN_TEST(test_blur_filter);
    UNITY_END();
}

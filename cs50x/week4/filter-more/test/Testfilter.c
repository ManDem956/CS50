
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
void initializeImagePixels_blur(RGBTRIPLE image[3][3], int numRows, int numColumns);
void initializeImagePixels_edges(RGBTRIPLE image[3][3]);

void test_edges_filter()
{
    initializeImagePixels_edges(image);

    if (image == NULL)
    {
        TEST_FAIL_MESSAGE("Image is not initialized.");
    }

    if (height < 3 || width < 3)
    {
        TEST_FAIL_MESSAGE("Invalid image dimensions.");
    }

    edges(height, width, image);
    // check_image_pixel(image, 0, 1, 213, 228, 255);
    check_image_pixel(image, 1, 1, 210, 150, 60);
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
    initializeImagePixels_blur(image, height, width);
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
}

void initializeImagePixels_blur(RGBTRIPLE image[3][3], int rows, int cols)
{
    // first row: (10, 20, 30), (40, 50, 60), (70, 80, 90)
    // second row: (110, 130, 140), (120, 140, 150), (130, 150, 160)
    // third row: (200, 210, 220), (220, 230, 240), (240, 250, 255)
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
void initializeImagePixels_edges(RGBTRIPLE image[3][3])
{
    // first row: (0, 10, 25), (0, 10, 30), (40, 60, 80)
    // second row: (20, 30, 90), (30, 40, 100), (80, 70, 90)
    // third row: (20, 20, 40), (30, 10, 30), (50, 40, 10)

    // Define colors for each pixel
    // (0, 10, 25);
    image[0][0].rgbtRed = 0;
    image[0][0].rgbtGreen = 10;
    image[0][0].rgbtBlue = 25;

    // (0, 10, 30)
    image[0][1].rgbtRed = 0;
    image[0][1].rgbtGreen = 10;
    image[0][1].rgbtBlue = 30;
    // (40, 60, 80)
    image[0][2].rgbtRed = 40;
    image[0][2].rgbtGreen = 60;
    image[0][2].rgbtBlue = 80;
    // (20, 30, 90)
    image[1][0].rgbtRed = 20;
    image[1][0].rgbtGreen = 30;
    image[1][0].rgbtBlue = 90;
    // (30, 40, 100),
    image[1][1].rgbtRed = 30;
    image[1][1].rgbtGreen = 40;
    image[1][1].rgbtBlue = 100;
    // (80, 70, 90)
    image[1][2].rgbtRed = 80;
    image[1][2].rgbtGreen = 70;
    image[1][2].rgbtBlue = 90;
    // (20, 20, 40),
    image[2][0].rgbtRed = 20;
    image[2][0].rgbtGreen = 20;
    image[2][0].rgbtBlue = 40;
    // (30, 10, 30), (50, 40, 10)
    image[2][1].rgbtRed = 30;
    image[2][1].rgbtGreen = 10;
    image[2][1].rgbtBlue = 30;
    // (50, 40, 10)
    image[2][2].rgbtRed = 50;
    image[2][2].rgbtGreen = 40;
    image[2][2].rgbtBlue = 10;
}

void tearDown(void)
{
}

int main(int argc, char **argv)
{
    UNITY_BEGIN();
    RUN_TEST(test_edges_filter);
    RUN_TEST(test_blur_filter);
    UNITY_END();
}

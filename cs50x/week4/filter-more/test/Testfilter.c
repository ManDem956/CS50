
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

void initializeImagePixels_blur(RGBTRIPLE image[3][3], int height, int width)
{
    int row, col;
    int red[] = {10, 40, 70, 110, 120, 130, 200, 220, 240};
    int green[] = {20, 50, 80, 130, 140, 150, 210, 230, 250};
    int blue[] = {30, 60, 90, 140, 150, 160, 220, 240, 255};

    for (row = 0; row < height; row++)
    {
        for (col = 0; col < width; col++)
        {
            image[row][col].rgbtRed = red[row * width + col];
            image[row][col].rgbtGreen = green[row * width + col];
            image[row][col].rgbtBlue = blue[row * width + col];
        }
    }
}
void initializeImagePixels_edges(RGBTRIPLE image[3][3])
{
    // Define colors for each pixel
    image[0][0] = (RGBTRIPLE){25, 10, 0};
    image[0][1] = (RGBTRIPLE){30, 10, 0};
    image[0][2] = (RGBTRIPLE){80, 60, 40};
    image[1][0] = (RGBTRIPLE){90, 30, 20};
    image[1][1] = (RGBTRIPLE){100, 40, 30};
    image[1][2] = (RGBTRIPLE){90, 70, 80};
    image[2][0] = (RGBTRIPLE){40, 20, 20};
    image[2][1] = (RGBTRIPLE){30, 10, 30};
    image[2][2] = (RGBTRIPLE){10, 40, 50};
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

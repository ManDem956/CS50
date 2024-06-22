#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            BYTE rgbtAverage =
                round((image[h][w].rgbtBlue + image[h][w].rgbtGreen + image[h][w].rgbtRed) / 3.0);
            image[h][w].rgbtBlue = image[h][w].rgbtGreen = image[h][w].rgbtRed = rgbtAverage;
        }
    }
}

RGBTRIPLE sepialize(RGBTRIPLE pixel)
{

    RGBTRIPLE result;
    double sepiaRed = 0.393 * pixel.rgbtRed + 0.769 * pixel.rgbtGreen + 0.189 * pixel.rgbtBlue;
    double sepiaGreen = 0.349 * pixel.rgbtRed + 0.686 * pixel.rgbtGreen + 0.168 * pixel.rgbtBlue;
    double sepiaBlue = 0.272 * pixel.rgbtRed + 0.534 * pixel.rgbtGreen + 0.131 * pixel.rgbtBlue;

    result.rgbtRed = (sepiaRed > 255.0) ? 255 : round(sepiaRed);
    result.rgbtGreen = (sepiaGreen > 255.0) ? 255 : round(sepiaGreen);
    result.rgbtBlue = (sepiaBlue > 255.0) ? 255 : round(sepiaBlue);

    return result;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            RGBTRIPLE target = sepialize(image[h][w]);
            image[h][w] = target;
        }
    }
}

void swap(RGBTRIPLE *left, RGBTRIPLE *right)
{
    RGBTRIPLE tmp = *left;
    *left = *right;
    *right = tmp;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int h = 0; h < height; h++)
    {
        int left = 0;
        int right = width - 1;
        while (left < right)
        {
            swap(&image[h][left], &image[h][right]);
            left++;
            right--;
        }
    }
}

RGBTRIPLE blur_pixel(int height, int width, RGBTRIPLE image[height][width], int row, int col)
{
    RGBTRIPLE result = {0, 0, 0};    
    double red = 0;
    double green = 0;
    double blue = 0;

    int pixelCount = 0;

    for (int i = -1; i <= 1; i++)
    {
        for (int j = -1; j <= 1; j++)
        {
            int currentRow = row + i;
            int currentCol = col + j;

            if (currentRow >= 0 && currentRow < height && currentCol >= 0 && currentCol < width)
            {
                red += image[currentRow][currentCol].rgbtRed;
                green += image[currentRow][currentCol].rgbtGreen;
                blue += image[currentRow][currentCol].rgbtBlue;

                pixelCount++;
            }
        }
    }

    result.rgbtRed = round(red / (double)pixelCount);
    result.rgbtGreen = round(green / (double)pixelCount);
    result.rgbtBlue = round(blue / (double)pixelCount);

    return result;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp[height][width];
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            tmp[h][w] = blur_pixel(height, width, image, h, w);
        }
    }

    // Swap the image and tmp array
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            image[h][w] = tmp[h][w];
        }
    }
}

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

// Swaps the RGBTRIPLE values pointed to by left and right pointers.
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

/**
 * Calculates the blurred pixel value by averaging the RGB values of the surrounding pixels.
 *
 * @param height The height of the image.
 * @param width The width of the image.
 * @param image The image matrix.
 * @param row The row index of the pixel to blur.
 * @param col The column index of the pixel to blur.
 *
 * @return The RGBTRIPLE structure representing the blurred pixel value.
 *
 * @throws None.
 */
RGBTRIPLE blurPixel(int height, int width, RGBTRIPLE image[height][width], int row, int col)
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
                RGBTRIPLE current_pixel = image[currentRow][currentCol];
                red += current_pixel.rgbtRed;
                green += current_pixel.rgbtGreen;
                blue += current_pixel.rgbtBlue;

                pixelCount++;
            }
        }
    }

    result.rgbtRed = round(red / (double) pixelCount);
    result.rgbtGreen = round(green / (double) pixelCount);
    result.rgbtBlue = round(blue / (double) pixelCount);

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
            tmp[h][w] = blurPixel(height, width, image, h, w);
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

// Calculates the Sobel operator for a given pixel in the image matrix based on the gradient 
// in the x and y directions.
// Parameters:
//  - height: The height of the image.
//  - width: The width of the image.
//  - image: The image matrix containing RGBTRIPLE pixels.
//  - row: The row index of the pixel to process.
//  - col: The column index of the pixel to process.
// Returns:
//  - The RGBTRIPLE structure representing the result of the Sobel operator for the specified pixel.
RGBTRIPLE sobelSum(int height, int width, RGBTRIPLE image[height][width], int row, int col)
{
    RGBTRIPLE result = {0, 0, 0};
    int gx_kernel[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int gy_kernel[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    double gx_red = 0;
    double gx_green = 0;
    double gx_blue = 0;

    double gy_red = 0;
    double gy_green = 0;
    double gy_blue = 0;

    for (int i = -1; i <= 1; i++)
    {
        for (int j = -1; j <= 1; j++)
        {
            int currentRow = row + i;
            int currentCol = col + j;

            double red = 0;
            double green = 0;
            double blue = 0;
            if (currentRow >= 0 && currentRow < height && currentCol >= 0 && currentCol < width)
            {
                RGBTRIPLE current_pixel = image[currentRow][currentCol];
                gx_red += gx_kernel[i + 1][j + 1] * current_pixel.rgbtRed;
                gx_green += gx_kernel[i + 1][j + 1] * current_pixel.rgbtGreen;
                gx_blue += gx_kernel[i + 1][j + 1] * current_pixel.rgbtBlue;

                gy_red += gy_kernel[i + 1][j + 1] * current_pixel.rgbtRed;
                gy_green += gy_kernel[i + 1][j + 1] * current_pixel.rgbtGreen;
                gy_blue += gy_kernel[i + 1][j + 1] * current_pixel.rgbtBlue;
            }
        }
    }
    double g_root_red = sqrt(gx_red * gx_red + gy_red * gy_red);
    double g_root_green = sqrt(gx_green * gx_green + gy_green * gy_green);
    double g_root_blue = sqrt(gx_blue * gx_blue + gy_blue * gy_blue);

    result.rgbtRed = (g_root_red > 255) ? 255 : round(g_root_red);
    result.rgbtGreen = (g_root_green > 255) ? 255 : round(g_root_green);
    result.rgbtBlue = (g_root_blue > 255) ? 255 : round(g_root_blue);

    return result;
}
// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp[height][width];
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            tmp[h][w] = sobelSum(height, width, image, h, w);
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

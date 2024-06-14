#include <stdio.h>

void swap(int left, int right);
void swap_real(int *left, int *right);


int main(int argc, char **argv)
{
    int x = 1;
    int y = 2;

    printf("x: %i, y:%i\n", x,y);
    swap(x, y);
    printf("swap result:\r\tx: %i, y:%i\n", x,y);
    swap_real(&x, &y);
    printf("swap_real result:\r\tx: %i, y:%i\n", x,y);
}

void swap(int left, int right)
{
    int tmp = left;
    left = right;
    right = tmp;
}

void swap_real(int *left, int *right)
{
    int tmp = *left;
    *left = *right;
    *right = tmp;
}
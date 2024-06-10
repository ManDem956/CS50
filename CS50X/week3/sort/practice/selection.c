
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void printArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

void do_sort(size_t size, int n[])
{
    int i, j, min_idx;

    for (i = 0; i < size; i++)
    {
        min_idx = i;
        for (j = i + 1; j < size; j++)
            if (n[j] < n[min_idx])
                min_idx = j;

        if (min_idx != i)
            swap(&n[min_idx], &n[i]);
    }
}


void merge(){
    
}

void do_run()
{
    int arr[100] = {99, 56, 14, 0,  11, 74, 4,  85, 88, 10, 12, 45, 30, 2,  3,
                    86, 44, 82, 79, 61, 78, 59, 19, 95, 23, 97, 1,  64, 62, 31,
                    8,  81, 69, 76, 65, 5,  34, 52, 35, 93, 41, 77, 87, 54, 22,
                    17, 15, 68, 89, 29, 33, 42, 73, 32, 60, 96, 21, 9,  57, 24,
                    90, 92, 91, 70, 39, 37, 13, 48, 47, 50, 66, 40, 38, 16, 63,
                    43, 46, 94, 36, 49, 67, 28, 72, 58, 25, 53, 20, 84, 7,  83,
                    75, 6,  98, 27, 51, 55, 26, 18, 80, 71};

    printArray(arr, 100);

    do_sort(100, arr);

    printArray(arr, 100);
}

int main(int argc, char **argv)
{
    do_run();
}
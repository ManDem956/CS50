
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
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

void merge(int arr[], int size, int left, int mid, int right)
{
    int idx_left, idx_right, idx_result;
    int size_left = mid - left + 1;
    int size_right = right - mid;

    int left_array[size_left], right_array[size_right];

    for (idx_left = 0; idx_left < size_left; idx_left++)
    {
        left_array[idx_left] = arr[left + idx_left];
    }
    for (idx_right = 0; idx_right < size_right; idx_right++)
    {
        right_array[idx_right] = arr[mid + 1 + idx_right];
    }

    idx_left = 0;
    idx_right = 0;
    idx_result = left;
    while (idx_left < size_left && idx_right < size_right)
    {
        if (left_array[idx_left] <= right_array[idx_right])
        {
            arr[idx_result] = left_array[idx_left];
            idx_left++;
        }
        else
        {
            arr[idx_result] = right_array[idx_right];
            idx_right++;
        }
        idx_result++;
    }

    while (idx_left < size_left)
    {
        arr[idx_result] = left_array[idx_left];
        idx_left++;
        idx_result++;
    }
    while (idx_right < size_right)
    {
        arr[idx_result] = right_array[idx_right];
        idx_right++;
        idx_result++;
    }
}

void mergesort(int arr[], int size, int left, int right)
{
    if (left < right)
    {
        int mid = (left + right) / 2;
        mergesort(arr, size, left, mid);
        mergesort(arr, size, mid + 1, right);
        merge(arr, size, left, mid, right);
    }
}

void do_sort(size_t size, int n[])
{
    mergesort(n, size, 0, size - 1);
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
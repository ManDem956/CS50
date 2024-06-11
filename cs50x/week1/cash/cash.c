#include <cs50.h>
#include <stdio.h>

// no need to calculate modulus of 1, it will always be a remainder
const int change[] = {25, 10, 5};

int main(void)
{
    int count = 0;
    size_t n = sizeof(change) / sizeof(change[0]);
    int coins;
    do
    {
        coins = get_int("Change owed: ");
    }
    while (coins < 0);

    for (int i = 0; i < n; i++)
    {
        count += coins / change[i];
        coins %= change[i];
    }

    count += coins;
    printf("%i\n", count);
}
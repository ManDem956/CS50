#include <cs50.h>
#include <regex.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool validate_card(string number)
{
    int sum = 0;
    for (int i = 0; i < strlen(number); i++)
    {
        // This is really cool way to convert string to int;
        // ASCII values of digits are sequential, starting from '0' (48) to '9' (57).
        // So, subtracting the ASCII value of a digit character from '0' will give us its numeric value.
        int digit = number[i] - '0';
        if (i % 2 == 0)
        {
            digit *= 2;
            if (digit > 9)
            {
                // e.g. is 9*2 = 18, 1+8 = 9 <=> 18 - 9, or if 6*2 = 12, then 1+2=3 <=> 12-9
                digit -= 9;
            }
        }
        sum += digit;
    }
    return sum % 10 == 0;
}

bool validate_input(regex_t regex, string number)
{
    int result = regexec(&regex, number, 0, NULL, 0);
    printf("%d\n", result);
    return (result == 0);
    // return (result == 0) && (validate_card(number));
}

int main(void)
{
    regex_t regex;
    int result;
    result = regcomp(&regex, "\b(?:(?:(?:37|34)\\d{13})|(?:(?:51|52|53|54|55)\\d{14})|(?:4(?:\\d{12}|\\d{15})))\b", 0);
    // regcomp(&regex, "\b(?:\\d{13,16})\b", 0);

    string number = "";
    do
    {
        number = get_string("Number: ");
    } while (!validate_input(regex, number));
    // } while (!validate_card(number));
}
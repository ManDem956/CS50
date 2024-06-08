#include <cs50.h>
#include <regex.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const string invalid = "INVALID";

string cards[3][2] = {
    {"^(3[47][0-9]{13})$", "AMEX"}, 
    {"^(5[12345][0-9]{14})$", "MASTERCARD"}, 
    {"^(4[0-9]{12}|4[0-9]{15})$", "VISA"}};

bool validate_card(string number)
{
    int sum = 0;
    int idx = 1;
    for (int i = strlen(number) - 1; i >= 0; i--)
    {
        // A cool way to convert char to number.
        //  ASCII values of digits are sequential, starting from '0' (48) to '9' (57).
        // So, subtracting the ASCII value of a digit character from '0'
        // will give us its numeric value.
        int digit = number[i] - '0';
        // printf("%d, %d\n", i, idx);
        if (idx % 2 == 0)
        {
            digit *= 2;
            // Fun way to get a sum of 2-digit number below 20
            // e.g. 12 => 1+2 = 12-9 = 3
            if (digit > 9)
            {
                digit -= 9;
            }
        }
        sum += digit;
        idx++;
    }
    return sum % 10 == 0;
}

bool validate_input(regex_t regex, string number)
{
    int result = regexec(&regex, number, 0, NULL, 0);

    return (result == 0);
}

string detect_carrier(string number)
{
    if (!validate_card(number))
    {
        return invalid;
    }

    regex_t regex;
    for (int i = 0; i < 3; i++)
    {
        int result = regcomp(&regex, cards[i][0], REG_EXTENDED | REG_NOSUB);

        result = regexec(&regex, number, 0, NULL, 0);
        if (result == 0)
        {
            return cards[i][1];
        }
    }

    return invalid;
}

int main(void)
{
    regex_t regex;
    int result;
    char regex_all[80];

    sprintf(regex_all, "%s|%s|%s", cards[0][0], cards[1][0], cards[2][0]);
    result = regcomp(&regex, "[0-9]{1,16}", REG_EXTENDED | REG_NOSUB);

    if (result != 0)
    {
        printf("regcomp: %d\n", result);
        return 1;
    }

    string number = "";
    do
    {
        number = get_string("Number: ");
    }
    while (!validate_input(regex, number));

    printf("%s\n", detect_carrier(number));
}
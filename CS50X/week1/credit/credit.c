#include <cs50.h>
#include <regex.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const string invalid = "INVALID";
const string visa = "VISA";
const string mastercard = "MASTERCARD";
const string amex = "AMEX";

const string regex_general = "\b(?:(?:(?:3[47])\\d{13})|(?:(?:5[12345])\\d{14})|(?:4(?:\\d{12}|\\d{15})))\b";
const string regex_amex = "\b(?:3[47]\\d{13})\b";
const string regex_mastercard = "\b(?:5[12345]\\d{14})\b";
const string regex_visa = "\b(?:4\\d{12}|4\\d{15})\b";

string cards[3][2] = {{"\\b(?:3[47]\\d{13})\\b", "AMEX"},
                      {"\\b(?:5[12345]\\d{14})\\b", "MASTERCARD"},
                      {"\\b(?:4\\d{12}|4\\d{15})\\b", "VISA"}};

bool validate_card(string number)
{
    int sum = 0;
    for (int i = 0; i < strlen(number); i++)
    {
        int digit = number[i] - '0';
        if (i % 2 == 0)
        {
            digit *= 2;
            if (digit > 9)
            {
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
    if (result == 0)
    {
        return true;
    }

    return false;
}

string detect_carrier(string number)
{
    regex_t regex;
    for (int i = 0; i < 3; i++)
    {
        printf("Regex: %s\n", cards[i][0]);
        printf("regcomp: %d\n", regcomp(&regex, cards[i][0], 0));
        int result = regexec(&regex, number, 0, NULL, 0);
        printf("regcomp: %d\n", result);
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
    for (int i = 0; i < 3; i++)
    {
        printf("%s\n", cards[i][0]);
    }

    sprintf(regex_all, "%s|%s|%s", cards[0][0], cards[1][0], cards[2][0]);

    // result = regcomp(&regex, regex_all, 0);
    result = regcomp(&regex, "(?:(?:(?:37|34)\\d{13})|(?:(?:51|52|53|54|55)\\d{14})|(?:4(?:\\d{12}|\\d{15})))", 0);

    string number = "";
    do
    {
        number = get_string("Number: ");
    } while (!validate_input(regex, number));

    printf("%s\n", detect_carrier(number));
}
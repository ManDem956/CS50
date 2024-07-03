import re


cards = {"AMEX": "^(3[47][0-9]{13})$", "MASTERCARD": "^(5[12345][0-9]{14})$",
         "VISA": "^(4[0-9]{12}|4[0-9]{15})$"}


def get_user_input(prompt: str) -> str:
    """
    Prompt the user for input, convert it to an integer, and return the result.

    Parameters:
        prompt (str): The string to prompt the user with.

    Returns:
        str: The user's input as a string.
    """
    while True:
        try:
            result = input(f"{prompt}: ")
            int(result)
        except ValueError:
            continue
        else:
            return result


def validate_number(number: str) -> bool:
    """
    Calculates the checksum of a credit card number and checks if it is valid.

    Args:
        number (str): The credit card number.

    Returns:
        bool: True if the checksum is valid, False otherwise.
    """
    sum = 0
    # Sum of every second digit multiplied by 2 from right to left
    for i in number[-2::-2]:
        double = int(i) * 2
        # Creating way to calculate the sum pf a 2-digit number
        if double > 9:
            double -= 9
        sum += double

    # Sum of every odd digit from right to left
    for i in number[-1::-2]:
        sum += int(i)

    # If the sum is divisible by 10, the number is valid
    return (sum % 10) == 0


def detect_carrier(number: str) -> str:
    """
    Detects the carrier of a credit card based on the given number.

    Args:
        number (str): The credit card number.

    Returns:
        str: The name of the carrier if the number is valid and matches a known pattern,
             otherwise "INVALID".
    """
    if validate_number(number):
        for key, val in cards.items():
            # Check if the number matches the pattern
            if re.fullmatch(val, number) is not None:
                return key
    return "INVALID"


def main() -> None:
    number = get_user_input("Number")
    print(detect_carrier(number))


if __name__ == "__main__":
    main()

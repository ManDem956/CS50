import re


REG_WORDS = "[a-z0-9-']+[a-z0-9-']*"
REG_LETTERS = "[a-z0-9]"
REG_SENTENCES = "[.!?]"


def calculate(line: str) -> int:
    """
    Calculates the Coleman-Liau index for the given text line.

    Parameters:
        line (str): The text input for which the index needs to be calculated.

    Returns:
        int: The Coleman-Liau index rounded to the nearest integer.
    """
    wordCount = len(re.findall(REG_WORDS, line, re.IGNORECASE))
    letterCount = len(re.findall(REG_LETTERS, line, re.IGNORECASE))
    sentenceCount = len(re.findall(REG_SENTENCES, line))

    # Calculate the percentage of words and sentences
    letterPerWords = (float(letterCount) / float(wordCount)) * 100
    sentencePerWords = (float(sentenceCount) / float(wordCount)) * 100

    # Calculate the Coleman-Liau index 
    cli = 0.0588 * letterPerWords - 0.296 * sentencePerWords - 15.8

    return round(cli)


def humanize(cli: int) -> str:
    """
    Returns a string representation of the given Coleman-Liau index (cli).

    Parameters:
        cli (int): The Coleman-Liau index.

    Returns:
        str: A string representation of the index, either "Before Grade 1", "Grade 16+", or "Grade {cli}".
    """
    if cli < 1:
        return "Before Grade 1"
    elif cli > 16:
        return "Grade 16+"
    else:
        return f"Grade {cli}"


def get_user_input(prompt: str) -> str:
    """
    Prompts the user with the given string and returns the user's input as a string.

    Parameters:
        prompt (str): The string to prompt the user with.

    Returns:
        str: The user's input as a string.
    """
    return input(f"{prompt}: ")


def main() -> None:
    line = get_user_input("Text: ")

    res = calculate(line)
    print(humanize(res))


if __name__ == "__main__":
    main()

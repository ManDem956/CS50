import re


REG_WORDS = "[a-z0-9-']+[a-z0-9-']*"
REG_LETTERS = "[a-z0-9]"
REG_SENTENCES = "[.!?]"


def calculate(line: str) -> int:
    wordCount = len(re.findall(REG_WORDS, line, re.IGNORECASE))
    letterCount = len(re.findall(REG_LETTERS, line, re.IGNORECASE))
    sentenceCount = len(re.findall(REG_SENTENCES, line))

    letterPerWords = (float(letterCount) / float(wordCount)) * 100
    sentencePerWords = (float(sentenceCount) / float(wordCount)) * 100

    cli = 0.0588 * letterPerWords - 0.296 * sentencePerWords - 15.8

    return round(cli)


def humanize(cli: int) -> str:
    if cli < 1:
        return "Before Grade 1"
    elif cli > 16:
        return "Grade 16+"
    else:
        return f"Grade {cli}"


def get_user_input(prompt: str) -> str:
    return input(f"{prompt}: ")


def main() -> None:
    line = get_user_input("Text: ")

    res = calculate(line)
    print(humanize(res))


if __name__ == "__main__":
    main()

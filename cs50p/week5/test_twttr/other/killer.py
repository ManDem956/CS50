def main():
    user_input = input('Input: ')
    shortened_word = shorten(user_input)
    print(shortened_word)


def shorten(word):
    result = ""
    for vowel in word:
        if vowel not in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
            result += vowel
    return result


if __name__ == "__main__":
    main()

def get_int(prompt: str):
    """
    Prompt the user with the given string and return the user's input as an integer.

    Parameters:
        prompt (str): The string to prompt the user with.

    Returns:
        int: The user's input as an integer.
    """
    return int(input(f"{prompt}: "))


def main() -> None:
    while True:
        try:
            # Get the height of the pyramid
            height = get_int("Height: ")
            # Check if height is valid
            if height < 1 or height > 8:
                raise ValueError
            break
        except ValueError:
            continue

    # Print the pyramid
    for i in range(height):
        print(f"{'#'*(i+1): >{height}}  {'#'*(i+1)}")


if __name__ == "__main__":
    main()

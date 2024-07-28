CONST_FILE_MAP = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

CONST_DEFAULT_VALUE = "application/octet-stream"


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def get_ext(filename: str) -> str:
    dot_index = filename.rfind(".")
    result = CONST_FILE_MAP.get(filename[dot_index:].lower(), CONST_DEFAULT_VALUE)
    return result


if __name__ == "__main__":
    user_input: str = get_user_input("File name: ").strip()

    print(get_ext(user_input))

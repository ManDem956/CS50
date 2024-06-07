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

if __name__ == "__main__":
    user_input: str = input("File name: ").strip().lower()
    dot_index = user_input.rfind(".")
    result = CONST_FILE_MAP.get(user_input[dot_index:], CONST_DEFAULT_VALUE)
    print(result)

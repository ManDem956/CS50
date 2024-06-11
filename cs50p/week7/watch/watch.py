import re

# REGEXP = r'"(.*)"'
REGEX_URL = r'src="((.*//)(.*youtube.com)(/embed.*?))"'
REGEX_REPLACE = r"(.*//)(.*youtube.com)(/embed)(/.*?)"
# src=\"(.*//(.*)/embed.*?)\"
# REGEXP = r"\b(?:(?:25[0-5]?))\b"


def parse(html):
    res = re.search(REGEX_URL, html)
    if not res:
        return None

    res2 = re.sub(REGEX_REPLACE, r"https://youtu.be\4", res.groups()[0])
    return res2


def main() -> None:
    print(parse(input("HTML: ")))


if __name__ == "__main__":
    main()

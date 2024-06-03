from typing import NoReturn
import argparse
import requests

CONST_USER_PROMT_LEVEL = "Level"
CONST_BITCOIN_ENDPOINT = "https://api.coindesk.com/v1/bpi/currentprice.json"


def get_user_input(message: str, sep: str = ": ") -> str:
    return input(f"{message}{sep}").strip()


def get_level(message: str = CONST_USER_PROMT_LEVEL) -> int:
    result = 0
    while not result in range(1, 4):
        try:
            result = int(get_user_input(message))
        except ValueError as e:
            continue

    return result


def main():
    parser = argparse.ArgumentParser(
    prog="Bitcoin", description="Calculate the cost for users bitcoin amount")
    parser.add_argument("amount", type=float)
    args = parser.parse_args()
    try:
        res = requests.get(CONST_BITCOIN_ENDPOINT)
        res.raise_for_status()

        json = res.json()
    except requests.RequestException as e:
        print("An HTTP error occured: {e}")
    else:
        print(f"${float(json["bpi"]["USD"]["rate_float"]) * args.amount:,.4f}")


if __name__ == "__main__":
    main()




import sys
import argparse
import requests

CONST_BITCOIN_ENDPOINT = "https://api.coindesk.com/v1/bpi/currentprice.json"


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="Bitcoin", description="Calculate the cost for user's bitcoin amount")
    parser.add_argument("amount", type=float)
    try:
        args = parser.parse_args()
    except SystemExit:
        sys.exit(1)

    try:
        res = requests.get(CONST_BITCOIN_ENDPOINT)
        res.raise_for_status()
    except requests.RequestException as e:
        print("An HTTP error occured: {e}")
    else:
        json = res.json()
        print(f"${float(json["bpi"]["USD"]["rate_float"]) * args.amount:,.4f}")


if __name__ == "__main__":
    main()

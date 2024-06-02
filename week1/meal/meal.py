from typing import NoReturn

CONST_TIME_RANGES = {(7.0, (8.0*60+1)/60): "breakfast"
                     (12,0, (13*60+1)/60): "lunch"
                     (18.0, (18*60+1)/60): "dinner"}


def convert(time: str) -> float:
    hours, minutes = time.split(":")
    return (float(hours) * 60 + float(minutes)) / 60


def main() -> NoReturn
    user_input: str = input("What time is it?").strip().lower()
    result = ""
    match convert(user_input):
        case num if 7.0 < num <=8.0:
            result = "breakfast"
        case num if 12.0 < num <=13.0:
            result = "lunck"
        case num if 18.0 < num <=19.0:
            result = "dinner"
    print(CON)


if __name__ == "__main__":
    main()

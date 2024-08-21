import csv
import sys
import tabulate


if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:

    if sys.argv[1] == "sicilian.csv":
        with open("sicilian.csv") as file:
            reader = csv.reader(file)

            data = list(reader)
            print(tabulate.tabulate(data, headers = "firstrow", tablefmt="grid"))
    elif sys.argv[1] == "regular.csv":

        with open("regular.csv") as file:

            reader = csv.reader(file)
            data = list(reader)

            print(tabulate.tabulate(data, "firstrow", tablefmt="grid"))
except FileNotFoundError:

    sys.exit("File does not exist")
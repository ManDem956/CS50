import csv


with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    for name, *home in reader:
        print(f"{name=}, {home}")
        print(f'{name=}, {", ".join(home)}')
        print()

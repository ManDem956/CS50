import sys
from PIL import ImageOps
from PIL import Image


if len(sys.argv) == 0:
    sys.exit(1)
elif len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    before = sys.argv[1]
    after = sys.argv[2]
    a = before.split(".")
    b = after.split(".")
    if a[1] != b[1]:
        print("Input and output have different extensions")

        sys.exit(1)
    else:

        try:

            bef = Image.open(before)
            print("jk")

            shirt = Image.open("shirt.png")
            size = shirt.size

            resize = ImageOps.fit(shirt, bef.size)
            af = Image.new("RGB", resize.size)
            af = bef.copy()
            print(resize.size)
            print(af.size)
            af.paste(resize, (0, -100), resize)
            af.save(after)

        except FileNotFoundError:
            print("File not found")
            sys.exit(1)

import sys
from pyfiglet import Figlet

figlet = Figlet()


if len(sys.argv) == 1:
    user_input = input('Input: ').lower()
    print(figlet.renderText(user_input))


elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        figlet.setFont(font=sys.argv[2])

        # if sys.argv[2] not in figlet.getFonts():
        #     sys.exit("Invalid font")
        user_input = input('Input: ')

        print(figlet.renderText(user_input))
    else:
        sys.exit('Invalid usage')

else:
    print('Invalid usage')
    sys.exit(1)

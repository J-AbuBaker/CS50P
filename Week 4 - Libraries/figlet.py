import pyfiglet
import sys
import random

figlet = pyfiglet.Figlet()
fonts_names = figlet.getFonts()

if len(sys.argv) == 1:
    font_name = random.choice(fonts_names)
elif len(sys.argv) == 3:
    if sys.argv[1] in ['-f', '--font'] and sys.argv[2] in fonts_names:
        font_name = sys.argv[2]
    else:
        sys.exit('Invalid usage')
else:
    sys.exit('Invalid usage')

figlet.setFont(font=font_name)
txt = input('Input: ')
print('Output:')
print(figlet.renderText(txt))

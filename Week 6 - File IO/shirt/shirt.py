import sys
from PIL import Image, ImageOps

valid_extensions = ['jpg', 'jpeg', 'png']
if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

input_image_path = sys.argv[1]
input_image_extension = input_image_path.lower().split('.')[-1]

output_image_path = sys.argv[2]
output_image_extension = output_image_path.lower().split('.')[-1]

if input_image_extension not in valid_extensions:
    sys.exit('Invalid input file extension')
elif output_image_extension not in valid_extensions:
    sys.exit('Invalid output file extension')
elif input_image_extension != output_image_extension:
    sys.exit('Input and output have different extensions')

try:
    input_image = Image.open(input_image_path)
    shirt_image = Image.open("shirt.png")
    shirt_size = shirt_image.size

    output_image = ImageOps.fit(input_image, shirt_size)
    output_image.paste(shirt_image, (0, 0), shirt_image)
    output_image.save(output_image_path)
    sys.exit(0)  
except FileNotFoundError:
    sys.exit('Input does not exist')
except Exception as e:
    sys.exit(e)

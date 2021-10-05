from PIL import Image, ImageFilter

image1 = Image.open('misc/racoon.jpg')

image1 = image1.getcolors(100000)

print(image1)

image1.show()
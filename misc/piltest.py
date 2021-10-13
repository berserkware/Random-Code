from PIL import Image, ImageFilter

image1 = Image.open('misc/wallpaper.jpg')
image2 = Image.open("misc/fog.jpg")

image1 = image1.resize((1920, 1080))
image2 = image2.resize((1920, 1080))

image1 = image1.convert("RGB")
image2 = image2.convert("RGB")

image3 = Image.blend(image1, image2, 0.5)

image3.show()
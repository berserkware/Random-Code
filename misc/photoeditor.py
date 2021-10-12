from PIL import Image, ImageFilter
import os

commands = ["filter", "resize", "reset", "save", "help"]
filters = ["BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EDGE_ENHANCE_MORE", "EMBOSS", "FIND_EDGES", "SHARPEN", "SMOOTH", "SMOOTH_MORE"]

print("Welocme to photo editor")

global path

while True:
    print("What is the path of the image")
    try:
        path = input("path->")
        image = Image.open(path)
        break
    except:
        print("Could not find that image")


print("Type help for list of commands")

while True:
    command = input(">>>").split(" ")

    if command[0] == commands[0]:
        if command[1] == filters[0]:
            image = image.filter(ImageFilter.BLUR)
            image.show()
        elif command[1] == filters[1]:
            image = image.filter(ImageFilter.CONTOUR)
            image.show()
        elif command[1] == filters[2]:
            image = image.filter(ImageFilter.DETAIL)
            image.show()
        elif command[1] == filters[3]:
            image = image.filter(ImageFilter.EDGE_ENHANCE)
            image.show()
        elif command[1] == filters[4]:
            image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
            image.show()
        elif command[1] == filters[5]:
            image = image.filter(ImageFilter.EMBOSS)
            image.show()
        elif command[1] == filters[6]:
            image = image.filter(ImageFilter.FIND_EDGES)
            image.show()
        elif command[1] == filters[7]:
            image = image.filter(ImageFilter.SHARPEN)
            image.show()
        elif command[1] == filters[8]:
            image = image.filter(ImageFilter.SMOOTH)
            image.show()
        elif command[1] == filters[9]:
            image = image.filter(ImageFilter.SMOOTH_MORE)
            image.show()
        else:
            print("That is not a valid command")
    elif command[0] == commands[1]:
        try:
            image = image.resize((int(command[1]), int(command[2])))
            image.show()
        except:
            print("That is not a valid command")
    elif command[0] == commands[2]:
        image = Image.open(path)
        image.show()
    elif command[0] == commands[3]:

        image.save(path)
        print("Saved.")
    elif command[0] == commands[4]:
        print(" 1. filter [filter name] - adds a filter ot the image")
        print("     Filter names:")
        print("     BLUR")
        print("     CONTOUR")
        print("     DETAIL")
        print("     EDGE_ENHANCE")
        print("     EDGE_ENHANCE_MORE")
        print("     EMBOSS")
        print("     FIND_EDGES")
        print("     SHARPEN")
        print("     SMOOTH")
        print("     SMOOTH_MORE")
        print(" ")
        print(" 2. resize [width] [height] - resizes the image")
        print(" ")
        print(" 3. reset - resets the image to its original state")
        print(" ")
        print(" 4. save - saves the image")


    else:
        print("That is not a valid command")
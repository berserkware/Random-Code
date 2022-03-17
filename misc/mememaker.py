from PIL import Image, ImageDraw, ImageFont

class Mememaker():
    def __init__(self, template, toptext, bottomtext, name):
        self.template = Image.open(template).resize((500, 500))
        self.toptext = toptext
        self.bottomtext = bottomtext
        self.name = name
        self.font = ImageFont.truetype("misc/impact.ttf", 50)

    def Create(self):
        self.meme = Image.new("RGB", (500, 700), (255, 255, 255))
        self.template.copy()
        self.meme.paste(self.template, (0, 100))
        self.memed = ImageDraw.Draw(self.meme)
        self.memed.text((10, 10), self.toptext, (0,0,0), self.font)
        self.memed.text((10, 610), self.bottomtext, (0,0,0), self.font)
        self.meme.save(self.name + ".jpg")
        self.meme.show()


mememaker = Mememaker("misc/Images/racoon.jpg", "funni", "racoon", "testmeme")
mememaker.Create()
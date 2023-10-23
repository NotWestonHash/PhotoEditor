from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from os import system
system('pip install Pillow')
from PIL import Image, ImageDraw
import math, random

class PhotoEditorApp(App):
    pass

class Display(Screen,Widget):
    coordinates = []

    def recClick(self, touch):
        x,y=touch.x,touch.y
        self.coordinates.append(int(x))
        self.coordinates.append(int(y))
        if len(self.coordinates)>6:
            self.coordinates=self.coordinates[2:]
    def display_image(self):
        return images[index]

    def advance_image(self):
        global index
        if index < len(images)-1:
            index += 1
        else:
            index = 0
        self.ids.image.source = self.display_image()

    def back_image(self):
        global index
        if index > 0:
            index -= 1
        else:
            index = len(images)-1
        self.ids.image.source = self.display_image()
    def load(self,file):
        global index
        print(file)
        if file in images:
            index = images.index(file)

        self.ids.image.source = self.display_image()
    def inv(self):
        mage = Image.open(self.display_image())
        wiz = Image.new("RGB", (mage.size[0], mage.size[1]), "white")
        pixels = mage.load()
        magic = wiz.load()
        for y in range(mage.size[1]):
            for x in range(mage.size[0]):
                magic[x, y] = (255 - pixels[x, y][0], 255 - pixels[x, y][1], 255 - pixels[x, y][2])
        wiz.save("inverse" + self.display_image())
        images.append("inverse" + self.display_image())
        self.ids.image.source = "inverse" + self.display_image()
    def bw(self):
        mage = Image.open(self.display_image())
        wiz = Image.new("RGB", (mage.size[0], mage.size[1]), "white")
        pixels = mage.load()
        magic = wiz.load()
        for x in range(mage.size[0]):
            for y in range(mage.size[1]):
                red = pixels[x, y][0]  # value stored for red color channel
                green = pixels[x, y][1]  # value stored for green color channel
                blue = pixels[x, y][2]  # value stored for blue color channel
                avg = int((red + green + blue) / 3)
                magic[x, y] = (avg, avg, avg)  # assigns the pixel a new tuple made up of average of the red, green and blue
        wiz.save("bw"+self.display_image())
        images.append("bw" + self.display_image())
        self.ids.image.source = "bw" + self.display_image()
    def sp(self):
        mage = Image.open(self.display_image())
        wiz = Image.new("RGB", (mage.size[0], mage.size[1]), "white")
        pixels = mage.load()
        magic = wiz.load()
        for y in range(mage.size[1]):
            for x in range(mage.size[0]):
                magic[x, y] = (int(pixels[x, y][0] * .393 + pixels[x, y][1] * 0.769 + pixels[x, y][2] * 0.189),
                                int(pixels[x, y][0] * .349 + pixels[x, y][1] * 0.686 + pixels[x, y][2] * 0.168),
                                int(pixels[x, y][0] * .272 + pixels[x, y][1] * 0.534 + pixels[x, y][2] * 0.131))
        wiz.save("sepia" + self.display_image())
        images.append("sepia" + self.display_image())
        self.ids.image.source = "sepia" + self.display_image()
    def ln(self):
        mage = Image.open(self.display_image())
        wiz = Image.new("RGB", (mage.size[0], mage.size[1]), "white")
        pixels = mage.load()
        magic = wiz.load()
        for ty in range(5, mage.size[1] - 5, 5):
            for tx in range(5, mage.size[0] - 5, 5):
                for y in range(ty - 3, ty + 3):
                    for x in range(tx - 5, tx + 5):
                        d = int(math.sqrt(((x - tx) ** 2) + ((y - ty) ** 2)))
                        if d <= 5 and (abs(pixels[tx, ty][0] - pixels[x, y][0]) > 10 or abs(
                                pixels[tx, ty][1] - pixels[x, y][1]) > 10 or abs(
                                pixels[tx, ty][2] - pixels[x, y][2]) > 10):
                            magic[x, y] = (0, 0, 0)
        wiz.save("lin"+self.display_image())
        images.append("lin"+self.display_image())
        self.ids.image.source="lin"+self.display_image()
    def pt(self):
        mage = Image.open(self.display_image())
        wiz = Image.new("RGB", (mage.size[0], mage.size[1]), "white")
        pixels = mage.load()
        magic = wiz.load()
        for i in range(100):
            for y in range(50, mage.size[1] - 50, 100):
                for x in range(50, mage.size[0] - 50, 100):
                    xa = x + random.randint(-50, 50)
                    ya = y + random.randint(-50, 50)
                    size = random.randint(40, 60)
                    ellipsebox = [(xa, ya), (xa + size, ya + size)]
                    draw = ImageDraw.Draw(wiz)
                    draw.ellipse(ellipsebox, fill=(pixels[xa, ya][0], pixels[xa, ya][1], pixels[xa, ya][2]))
                    del draw
        wiz.save("point" + self.display_image())
        images.append("point"+self.display_image())
        self.ids.image.source = "point" + self.display_image()
    def px(self):
        #imge
        #nam
        #cx
        #cy
        #width
        #height
        img = Image.open(imge)
        pixels = img.load()
        for y in range(cy - (height // 2), cy + (height // 2), height // 8):
            for x in range(cx - (width // 2), cx + (width // 2), height // 8):
                avg = [0, 0, 0]
                for ye in range(y, y + (height // 8)):
                    for xe in range(x, x + (height // 8)):
                        avg[0] += pixels[xe, ye][0]
                        avg[1] += pixels[xe, ye][1]
                        avg[2] += pixels[xe, ye][2]
                avg = [(avg[0] // ((height // 8) ** 2)), (avg[1] // ((height // 8) ** 2)),
                       (avg[2] // ((height // 8) ** 2))]
                for ye in range(y, y + (height // 8)):
                    for xe in range(x, x + (height // 8)):
                        pixels[xe, ye] = (avg[0], avg[1], avg[2])
        img.save(nam + "ix.png")
images = ["cliff.jpg","chipmunk.jpg","train.jpg"]
index = 0

PhotoEditorApp().run()
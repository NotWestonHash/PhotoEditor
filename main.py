from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from os import system
system('pip install Pillow')
from PIL import Image
import math

class PhotoEditorApp(App):
    pass

class Display(Screen):
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
    def load(self):
    def inv(self):
        pass
    def bw(self):
        pass
    def sp(self):
        pass
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
        self.ids.image.source="lin"+self.display_image()
    def pt(self):
        pass
    def px(self):
        pass
images = ["cliff.jpg","chipmunk.jpg","train.jpg"]
index = 0


PhotoEditorApp().run()
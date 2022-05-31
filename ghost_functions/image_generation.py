from PIL import Image, ImageOps
from ghost_functions.generate_info import GenerateGhost
import base64
from io import BytesIO

class ImageProcessing:
    def __init__(self, image):
        self.og_image = image
        self.image = image
        self.image = Image.open(self.image)

    def invert_image(self):
        self.image = self.image.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)

    def apply_filter(self, rarity):
        mask = Image.new('RGBA', self.image.size, (0, 0, 0, 200))
        green = Image.new('RGB', self.image.size, (0, 255, 0))
        blue = Image.new('RGB', self.image.size, (0, 0, 255))
        yellow = Image.new('RGB', self.image.size, (255, 255, 0))
        purple = Image.new('RGB', self.image.size, (255, 0, 255))
        if rarity == "common":
            self.image = ImageOps.grayscale(self.image)
        elif rarity == "uncommon":
            self.image = Image.composite(self.image, green, mask).convert('RGB')
        elif rarity == "rare":
            self.image = Image.composite(self.image, blue, mask).convert('RGB')
        elif rarity == "epic":
            self.image = Image.composite(self.image, purple, mask).convert('RGB')
        elif rarity == "legendary":
            self.image = Image.composite(self.image, yellow, mask).convert('RGB')

    def show_image(self):
        self.image.show()

    def save_image(self):
        self.image.save('output.png')
        with open('output.png',"rb") as image_file:
            data = base64.b64encode(image_file.read())
        return data


#def random_image():
   # return ImageProcessing("../assets/3.png")
ghost = GenerateGhost()

print(ghost.print_info())
#ghost_image = random_image()
#ghost_image.invert_image()
#ghost_image.apply_filter(ghost.ghost_rarity)

#print(ghost_image.save_image())
#im = Image.open(BytesIO(base64.b64decode(ghost_image.save_image())))
#im.show()




#with open ("../assets/3.png","rb") as image_file:
 #   data = base64.b64encode(image_file.read())




#print(data)
#im = Image.open(BytesIO(base64.b64decode(data)))
#im.show()



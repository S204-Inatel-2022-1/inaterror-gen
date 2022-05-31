from PyQt5 import QtWidgets, QtGui, QtCore
from PIL.ImageQt import ImageQt
import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QLabel
from PyQt5.uic.properties import QtCore, QtGui
from ghost_functions.image_generation import ImageProcessing
from ghost_functions.generate_info import GenerateGhost

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 512, 512)
        self.setWindowTitle("PyQt5 Window")
        self.show()
        self.ghost = ImageProcessing("../assets/3.png")
        self.ghost_info = GenerateGhost()
        self.updated_image = ImageQt(self.ghost.image)

        self.generate_image()
    def button(self):
        self.button = QtWidgets.QPushButton("Generate Image", self)
        self.button.move(200, 400)
        self.button.clicked.connect(self.generate_image)
        self.button.show()

    def generate_image(self):
        print("Gerando")
        self.ghost.apply_filter(self.ghost_info.ghost_rarity)
        self.updated_image = ImageQt(self.ghost.image)
        self.show_image(self.updated_image)
        self.show_info()




    def show_image(self, image_path):
        self.image_label = QLabel(self)
        self.pixmap = QPixmap.fromImage(image_path)
        self.image_label.setPixmap(self.pixmap)
        self.image_label.resize(512, 512)
        self.image_label.move(125,0)
        self.image_label.show()


    def show_info(self):
        self.info_label = QLabel(self)
        self.info_label.setText(self.ghost_info.ghost_name+" - "+self.ghost_info.ghost_rarity)
        self.info_label.resize(512, 512)
        self.info_label.move(100,200)
        font = QFont()
        font.setPointSize(20)
        self.info_label.setFont(font)

        self.info_label.show()


def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()

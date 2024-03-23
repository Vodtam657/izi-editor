from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import os
from PIL.ImageFilter import *
from PyQt6.QtGui import QPixmap, QImage
from PIL import Image


def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap


papka = ""
app = QApplication([])

window = QWidget()
window.resize(800, 600)
window.setWindowTitle("ІЗІ ФОТОШОП")

folderBtn = QPushButton("Папка")
leftBtn = QPushButton("Ліворуч")
rightBtn = QPushButton("праворуч")
mirrorBtn = QPushButton("дзеркало")
blurBtn = QPushButton("Розмиття")

imgLbl = QLabel("фоточка")
fileList = QListWidget()

mainLine = QHBoxLayout()
columnLeft = QVBoxLayout()
columnLeft.addWidget(folderBtn)
columnLeft.addWidget(fileList)
mainLine.addLayout(columnLeft)
columnRight = QVBoxLayout()
columnRight.addWidget(imgLbl)
line1 = QHBoxLayout()
line1.addWidget(leftBtn)
line1.addWidget(rightBtn)
line1.addWidget(blurBtn)
columnRight.addLayout(line1)
mainLine.addLayout(columnRight)


class WorkWithPhoto:
 def __init__ (self):
    self.image = None
    self.folder = None
    self.image_name = None


def load(self):
    full_path = os.path.join(self.folder, self.image_name)
    self.image = Image.open(full_path)

    def show_image(self):
        pixel = pil2pixmap(self.image)
        imgLbl.setPixmap(pixel)


work_with_photo = WorkWithPhoto()


def show_directory():
    work_with_photo.folder = QFileDialog.getExistingDirectory()
    list_files = os.listdir(work_with_photo.folder)
    fileList.clear()
    for file in list_files:
        fileList.addItem(list_files)


def show_photo():
    image_name = fileList.currentItem().text()
    work_wint_photo.image_name = image_name
    work_with_photo.load()
    wowk_with_photo.show_image()


fileList.currentRowChanged.connect(show_photo)
folderBtn.clicke.connect(show_directory)
window.setLayout(mainLine)
window.show()
app.exec()

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QPainter, QImage, QColor
from PyQt5.QtCore import QPoint
from numpy import asarray 
from PIL import Image 
class ImageDisplay(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.Image = QImage()
        self.ImageDisplayer = QPixmap()
        self.RGBArray = []


    def setImage(self, imagePath):
        self.Image.load(imagePath)
        self.setRGBArray(imagePath)

    def Display(self):
        self.ImageDisplayer = QPixmap.fromImage(self.Image)
        self.update()

    def paintEvent(self, event):
        if not self.ImageDisplayer.isNull():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            painter.drawPixmap(self.rect(), self.ImageDisplayer)

    def height(self):
        return self.Image.height()
    
    def width(self):
        return self.Image.width()

    def setRGBArray(self, imagePath):
        image = Image.open(imagePath)
        self.RGBArray = asarray(image)
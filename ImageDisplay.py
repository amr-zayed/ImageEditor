from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, QRect
from Image import Image
import logging

InfoLogger = logging.getLogger(__name__)
InfoLogger.setLevel(logging.INFO)

DebugLogger = logging.getLogger(__name__)
DebugLogger.setLevel(logging.DEBUG)

FileHandler = logging.FileHandler('ImageEditor.log')
Formatter = logging.Formatter('%(levelname)s:%(filename)s:%(funcName)s:   %(message)s')
FileHandler.setFormatter(Formatter)
InfoLogger.addHandler(FileHandler)
DebugLogger.addHandler(FileHandler)

class ImageDisplay(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.ImageDisplayer = QPixmap()
        self.Image = None

    def SetPath(self, imagePath):
        self.Image = Image(imagePath)

    def Display(self):
        self.ImageDisplayer = self.Image.GetMainImage()
        self.update()

    def paintEvent(self, event):
        if not self.ImageDisplayer.isNull():
            height = 0
            width = 0
            #print("Width: ", event.rect().width(), " height: ", event.rect().height(),"\n")
            painter = QPainter(self)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)

            width = event.rect().width()
            height = self.ImageDisplayer.height()*(event.rect().width()/self.ImageDisplayer.width())

            HeightShift = event.rect().height()/4

            painter.drawPixmap(QRect(0 ,HeightShift ,width, height), self.ImageDisplayer)

    def height(self):
        return self.Image.height()
    
    def width(self):
        return self.Image.width()


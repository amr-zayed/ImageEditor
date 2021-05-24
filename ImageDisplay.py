from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QPainter, QImage
from PyQt5.QtCore import Qt, QRect
from Image import Image
import logging
import numpy as np
from PIL.Image import fromarray
import cv2

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

    def Display(self, image):
        pixmap = self.ArrToQpixmap(image)
        self.ImageDisplayer = pixmap
        self.update()

    def paintEvent(self, event):
        if not self.ImageDisplayer.isNull():
            height = 0
            width = 0
            painter = QPainter(self)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)

            width = event.rect().width()
            height = self.ImageDisplayer.height()*(event.rect().width()/self.ImageDisplayer.width())

            HeightShift = event.rect().height()/4

            painter.drawPixmap(QRect(0 ,HeightShift ,width, height), self.ImageDisplayer)

    def ArrToQpixmap(self,array):
        image = fromarray(array.astype(np.int8), 'L')
        image = ImageQt(image)
        image = QPixmap.fromImage(image)
        return image
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QPainter, QImage, QColor
from Image import Image 

class ImageDisplay(QWidget):
    def __init__(self, count, parent=None):
        QWidget.__init__(self, parent=parent)
        self.Image = Image(count)
        self.ImageDisplayer = QPixmap()

    def setImage(self, imagePath):
        self.Image.SetInitialImage(imagePath)

    def Display(self):
        self.ImageDisplayer = QPixmap.fromImage(self.Image.GetMainImage())
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


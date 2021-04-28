from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QPainter, QImage
class ImageDisplay(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.Image = QImage()
        self.ImageDisplayer = QPixmap()


    def setImage(self, imagePath):
        self.Image.load(imagePath)
        self.ImageDisplayer = QPixmap.fromImage(self.Image)
        self.update()

    def paintEvent(self, event):
        if not self.ImageDisplayer.isNull():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            painter.drawPixmap(self.rect(), self.ImageDisplayer)
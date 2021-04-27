from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QPainter
class ImageDisplay(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.Image = QPixmap()

    def setPixmap(self, image):
        self.Image = QPixmap.fromImage(image)
        self.update()

    def paintEvent(self, event):
        if not self.Image.isNull():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            painter.drawPixmap(self.rect(), self.Image)
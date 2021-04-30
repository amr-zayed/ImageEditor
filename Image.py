from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from numpy import asarray 
from PIL.Image import open

class Image(QWidget):
    def __init__(self, count, parent=None):
        QWidget.__init__(self, parent=parent)
        self.count = count
        self.MainImage = QImage()
        self.ImageList = []
        for _ in range(count):
            self.ImageList.append(QImage())
        self.PixelsList = []

    def SetInitialImage(self,path):
        self.MainImage.load(path)
        image = open(path)
        self.PixelsList.append(asarray(image))
        for i in range(1,self.count):
            self.PixelsList.append(self.PixelsList[0].copy())

    def GetMainImage(self):
        return self.MainImage
    
    def height(self):
        return self.MainImage.height()
    
    def width(self):
        return self.MainImage.width()
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from numpy import asarray 
from PIL.Image import open

class Image(QWidget):
    def __init__(self, path, count, parent=None):
        QWidget.__init__(self, parent=parent)
        self.Path = path
        self.Count = count
        
        self.MainImage = QPixmap()
        self.MainImage.load(self.Path)
        
        self.FourierLists = []
        self.FourierQpixmapLists = []

        for i in range(count):
            if i == 0:
                self.FourierLists.append(asarray(open(self.Path)))
            else:
                self.FourierLists.append(self.FourierLists[0].copy())
            self.FourierQpixmapLists.append(QPixmap())

    def GetMainImage(self):
        return self.MainImage
    
    def SetMainImage(sefl, index):
        self.MainImage = self.FourierQpixmapLists[index]
        
    def height(self):
        return self.MainImage.height()
    
    def width(self):
        return self.MainImage.width()
    
    def GetImageList(self):
        return self.ImageList

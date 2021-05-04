from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from numpy import asarray 
from PIL.Image import open
from Fourier import FT
from PIL.ImageQt import ImageQt
  


class Image(QWidget):
    def __init__(self, path, count=0, parent=None):
        QWidget.__init__(self, parent=parent)
        self.Path = path
        self.Count = count
        self.Greysscale = open(self.Path).convert('L')
        self.MainImage = QPixmap.fromImage(ImageQt(self.Greysscale))
        self.FourierLists = []
        for i in range(count):
            if i == 0:
                self.FourierLists.append(asarray(self.Greysscale))
            else:
                self.FourierLists.append(self.FourierLists[0].copy())

    def GetMainImage(self):
        return self.MainImage

    def height(self):
        return self.MainImage.height()
    
    def width(self):
        return self.MainImage.width()
        
    def SetFourierLists(self):
        isFour=False
        if self.Count==0:
            return
        if self.Count==4:
            isFour=True
        self.FourierLists=FT(self.Greysscale,isFour)





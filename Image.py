from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
import numpy
from numpy import asarray 
from PIL.Image import open
from Fourier import FT
from PIL.Image import fromarray
from PIL.ImageQt import ImageQt
  


class Image(QWidget):
    def __init__(self, path, count, parent=None):
        QWidget.__init__(self, parent=parent)
        self.Path = path
        self.Count = count
        
        self.MainImage = QPixmap()
        self.MainImage.load(self.Path)
        
        self.FourierLists = []
        self.FourierQpixmapLists = []
        print(count)

        for i in range(count):
            if i == 0:
                self.FourierLists.append(asarray(open(self.Path)))
            else:
                self.FourierLists.append(self.FourierLists[0].copy())

    def GetMainImage(self):
        return self.MainImage
    
    def SetMainImage(self, index):
        self.MainImage = self.FourierQpixmapLists[index]
    
    def GetComponentQpixMap(self,index):
        return self.FourierQpixmapLists[index]

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
            

        self.FourierLists=FT(open(self.Path),isFour)

    def SetFourierQpixmapLists(self):
        if self.Count==0:
            return    

        for Component in self.FourierLists:
            RGBimg=fromarray(Component,'RGB')
            Qimg=QPixmap.fromImage(ImageQt(RGBimg))
            self.FourierQpixmapLists.append(Qimg)
        print(self.FourierQpixmapLists)
        print(len(self.FourierQpixmapLists))
        





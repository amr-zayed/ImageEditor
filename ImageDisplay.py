from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QPainter, QImage, QColor
from Image import Image

"""Make sure to uncomment this"""
from Mixer import Mixer

class ImageDisplay(QWidget):
    def __init__(self, Mood, count, parent=None):
        QWidget.__init__(self, parent=parent)
        self.IsImage = Mood
        self.Count = count
        self.ImageDisplayer = QPixmap()
        self.Image = None
        self.ImageMixer = None

    def SetPath(self, imagePath):
        if self.IsImage:
            self.Image = Image(imagePath, self.Count)
        else:
            #pass #Make sure to remove this line

            """imagePath is a list of 2 paths...Class images takes only string in initialization"""
            #self.ImageMixer = Mixer(imagePath, self.Count) 
    def SetMainImage(self,index):
        self.ImageDisplayer=self.Image.GetComponentQpixMap(index)
        self.update()


    def Display(self):
        if self.IsImage:
            self.Image.SetFourierLists()
            self.Image.SetFourierQpixmapLists()
            self.ImageDisplayer = self.Image.GetMainImage()
            self.update()
        else:
            pass #Make sure to remove this line
        
            """Returns the mixed image as a qpixmap... you should create an object of type qpixmap in the Mixer class initialization"""
            #self.ImageDisplayer = self.ImageMixer.GetMixedImage()

    def paintEvent(self, event):
        if not self.ImageDisplayer.isNull():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            painter.drawPixmap(self.rect(), self.ImageDisplayer)

    def height(self):
        return self.Image.height()
    
    def width(self):
        return self.Image.width()


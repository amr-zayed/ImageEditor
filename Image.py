from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from numpy import asarray 
from PIL.Image import open
import cv2
from matplotlib import pyplot as plt

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
    
    def GetImageList(self):
        return self.ImageList
    
    def GetPixelsList(self):
        return self.PixelsList

    # def FtImage(self):
    #     img=cv2.imread('input.png')
    #     img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #     dft = asarray.fft.fft2(img)
    #     dft_shift = asarray.fft.fftshift(dft)
    #     phase_spectrum = asarray.angle(dft_shift)

    #     ax1 = plt.subplot(1,2,1)
    #     ax1.imshow(img, cmap='gray')

    #     ax2 = plt.subplot(1,2,2)
    #     ax2.imshow(phase_spectrum, cmap='gray')

    #     plt.show()
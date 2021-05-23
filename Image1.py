from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from numpy import asarray 
from PIL.Image import open, new, 
from PIL import Image
from PIL import ImageQt
from os import stat
import logging
from math import ceil
import numpy as np

InfoLogger = logging.getLogger(__name__)
InfoLogger.setLevel(logging.INFO)

DebugLogger = logging.getLogger(__name__)
DebugLogger.setLevel(logging.DEBUG)

FileHandler = logging.FileHandler('ImageEditor.log')
Formatter = logging.Formatter('%(levelname)s:%(filename)s:%(funcName)s:   %(message)s')
FileHandler.setFormatter(Formatter)
InfoLogger.addHandler(FileHandler)
DebugLogger.addHandler(FileHandler)



class Image(QWidget):
    def __init__(self, path, count=0, parent=None):
        QWidget.__init__(self, parent=parent)
        self.Path = path
        self.Count = count
        InfoLogger.info('File Size: {}KB'.format(ceil(stat(self.Path).st_size/125)))
        self.Greysscale = open(self.Path).convert('L')
        self.MainImage = asarray(self.Greysscale)
        self.FourierLists = []
        

    def GetMainImage(self):
        return self.MainImage

    def height(self):
        return self.MainImage.shape[1]
    
    def width(self):
        return self.MainImage.shape[0]
    
    def GetFourierElement(self, index):
        if index<0 or index>3:
            DebugLogger.debug('Requested fourier element is outside of range index = {}'.format(index))
        else:
            image = new('L',self.FourierLists[index].shape)
            image.putdata(self.FourierLists)
            image = QPixmap.fromImage(ImageQt(image))
            return image
        
    def SetFourierLists(self):
        self.FourierLists = self.FT(self.Greysscale)
        InfoLogger.info('FourierList created su')
    
    def FT(img):
        dft= np.fft.fft2(img)
        dft_shift = np.fft.fftshift(dft)
        phaseSpectrum = np.angle(dft)
        magnitudeSpectrum = np.abs(dft)
        Real = dft_shift.real
        Imag = dft_shift.imag
        ComponentsList=[magnitudeSpectrum,phaseSpectrum,Real,Imag]

        return ComponentsList
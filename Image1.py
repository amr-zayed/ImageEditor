from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage, QPixmap
import numpy as np
from PIL.Image import open
from os import stat
import logging
from math import ceil
import cv2

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
    def __init__(self, path, count=10, parent=None):
        QWidget.__init__(self, parent=parent)
        self.Path = path
        self.Count = count
        InfoLogger.info('File Size: {}KB'.format(ceil(stat(self.Path).st_size/125)))
        self.Greysscale = open(self.Path).convert('L')
        self.MainImage = np.asarray(self.Greysscale, dtype=np.uint8)
        self.FourierLists = []
        self.MixedList = []
        

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
            if index==0:
                return 20*np.log(self.FourierLists[index])
            else:
                return self.FourierLists[index]

        
    def SetFourierLists(self):
        self.FourierLists = self.FT(self.Greysscale)
        InfoLogger.info('FourierList created successfully')
    
    def FT(self, img):
        dft= np.fft.fft2(img)
        dft_shift = np.fft.fftshift(dft)
        phaseSpectrum = np.angle(dft)
        magnitudeSpectrum = np.abs(dft)
        Real = dft_shift.real
        Imag = dft_shift.imag
        ComponentsList=[magnitudeSpectrum,phaseSpectrum,Real,Imag]
        return ComponentsList

    def GetMixedList(self, Image2, slider1=0, slider2=0, comp1type=0, comp2type=0, comp1img=0, comp2img=0):
        if comp1type == 4 or comp1type == 5:
            if comp2type == 4 or comp2type == 5:
                self.MixedList = np.ones(self.FourierLists[0].shape)
                return
        if comp1img==0 and comp1type <= 3:
            comp1ListImage1 = self.FourierLists[comp1type]
            comp1ListImage2 = Image2.FourierLists[comp1type]
        elif comp1img==1 and comp1type <= 3:
            comp1ListImage1 = Image2.FourierLists[comp1type]
            comp1ListImage2 = self.FourierLists[comp1type]
        if comp2type==0 and comp2type <= 3:
            comp2ListImage1 = self.FourierLists[comp2type]
            comp2ListImage2 = Image2.FourierLists[comp2type]
        elif comp2type==1 and comp2type <= 3:
            comp2ListImage1 = Image2.FourierLists[comp2type]
            comp2ListImage2 = self.FourierLists[comp2type]
        
        if comp1type <= 3:
            Comp1 = comp1ListImage1*(slider1/100) + comp1ListImage2*(1-(slider1/100))
        if comp2type <= 3:
            Comp2 = comp2ListImage1*(slider2/100) + comp2ListImage2*(1-(slider2/100))

        if comp1type == 0 or comp1type == 1:
            if comp2type == 0 or comp2type == 1:
                if comp1type == 0:
                    Comp2 = np.exp(1j*Comp2)
                    self.MixedList = np.fft.ifft2(Comp1*Comp2)
                else:
                    Comp1 = np.exp(1j*Comp1)
                    self.MixedList = np.fft.ifft2(Comp2*Comp1)
                self.MixedList = np.abs(self.MixedList)
            else:
                if comp2type == 4:
                    Comp1 = np.exp(1j*Comp1)
                self.MixedList = np.fft.ifft2(Comp1)
                self.MixedList = np.abs(self.MixedList)
                if comp2type == 4:
                    self.MixedList *= 10000

        if comp1type == 2 or comp1type == 3:
            if comp1type == 2:
                real = Comp1
                imaginary = 1j * (Comp2)
            else:
                real = Comp2
                imaginary = 1j * (Comp1)
            self.MixedList = real + imaginary
            self.MixedList = np.fft.ifft2(self.MixedList)
            self.MixedList = np.abs(self.MixedList)
        
        if comp1type == 4 or comp1type == 5:
            if comp2type == 4 or comp2type == 5:
                self.MixedList = np.ones(comp1ListImage1.shape)

            if comp2type == 0 or comp2type == 1:
                if comp1type == 4:
                    Comp2 = np.exp(1j*Comp2)
                self.MixedList = np.fft.ifft2(Comp2)
                self.MixedList = np.abs(self.MixedList)
                if comp1type == 4:
                    self.MixedList *= 10000

        return self.MixedList
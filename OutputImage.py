from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
import numpy as np
from numpy import asarray 
from PIL.Image import open
import cv2
from matplotlib import pyplot as plt
from Image import Image
class ImageOutput(QWidget):
    def __init__(self,parent=None):
        # self.count = count
        self.PathsList=[]
        self.Magnitude=[[],[]]
        self.Phase=[[],[]]
        self.Real=[[],[]]
        self.Imag=[[],[]]
        self.MainOutputImage = QImage()
        self.OutputComp1ImageList = []
        self.OutputComp2ImageList = []
        for _ in range(2):
            self.OutputComp1ImageList.append(QImage())
        self.PixelsListComp1 = []
        self.PixelsListComp2 = []
    def GetMainOutputImage(self):
        return self.MainOutputImage
    
    # def SetInitialImage(self,path):
    #     self.MainImage.load(path)
    #     image = open(path)
    #     self.PixelsList.append(asarray(image))
    #     for i in range(1,self.count):
    #         self.PixelsList.append(self.PixelsList[0].copy())
    #     print(self.PixelsList)
    
    def height(self):
        return self.MainOutputImage.height()
    
    def width(self):
        return self.MainOutputImage.width()
    
    def SetImagePathsList(self,List):
        self.PathsList=List
        print(self.PathsList)
        
    def FT(self):
        img=[0]*2
        dft=[0]*2
        for i in range(2):
            # img[i] = open(self.PathsList[i])
            img[i]= cv2.imread(self.PathsList[i],0)
            # img[i]= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            dft[i] = np.fft.fft2(img[i])
            dft_shift = np.fft.fftshift(dft[i])
            phase_spectrum = np.angle(dft_shift)
            magnitude_spectrum = 20*np.log(np.abs(dft_shift))
            self.Phase[i]=phase_spectrum
            self.Magnitude[i]=magnitude_spectrum
            self.Real[i] = dft_shift.real
            self.Imag[i] = dft_shift.imag
            # if i==0:
            #     plt.subplot(121),plt.imshow(phase_spectrum)
            #     plt.title('Input Image'), plt.xticks([]), plt.yticks([])
            #     plt.subplot(122),plt.imshow( magnitude_spectrum)
            #     plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
            #     plt.show()

            # im=np.fft.ifft2(self.Phase[i])
            
            # ax1 = plt.subplot(1,2,1)
            # ax1.imshow(img, cmap='gray')

            # ax2 = plt.subplot(1,2,2)
            # ax2.imshow(phase_spectrum, cmap='gray')

            # plt.show()
        #print(self.Imag)
        


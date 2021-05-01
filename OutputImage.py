from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
import numpy as np
from numpy import asarray 
from PIL.Image import open
from PIL import Image as mg
import cv2
from matplotlib import pyplot as plt
from Image import Image
class ImageOutput(QWidget):
    def __init__(self,parent=None):
        # self.count = count
        self.MainImage = QImage()
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
    
    #def SetComponentsImage(self,count):

        
        
    
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
            img[i] = open(self.PathsList[i])
            #img[i]= cv2.imread(self.PathsList[i],0)
            # img[i]= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            dft[i] = np.fft.fft2(img[i])
            dft_shift = np.fft.fftshift(dft[i])
            phase_spectrum = np.angle(dft_shift)
            magnitude_spectrum = 20*np.log(np.abs(dft_shift))
            self.Phase[i]=phase_spectrum
            self.Magnitude[i]=magnitude_spectrum
            self.Real[i] = dft_shift.real
            self.Imag[i] = dft_shift.imag
            print(type(self.Magnitude[i]))
            #fft_img_mod = np.fft.ifftshift(dft_shift)
            # img_mod = np.fft.ifft2(self.Magnitude[i])
            # img_mod = np.abs(img_mod)
            # test=mg.fromarray(self.Phase[i],'RGB')
            # test.save('test_phase.png')
            # test.show

            # if i==1:
            #     plt.subplot(121),plt.imshow(img[i])
            #     plt.title('Input Image'), plt.xticks([]), plt.yticks([])
            #     plt.subplot(122),plt.imshow( img_mod)
            #     plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
            #     plt.show()

            
    


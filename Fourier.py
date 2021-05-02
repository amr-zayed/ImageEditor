from PIL import Image as mg
import cv2
from matplotlib import pyplot as plt
import numpy as np
def FT(img):
    # img[i] = open(self.PathsList[i])
    #img[i]= cv2.imread(self.PathsList[i],0)
    # img[i]= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    dft= np.fft.fft2(img)
    dft_shift = np.fft.fftshift(dft)
    phaseSpectrum = np.angle(dft_shift)
    magnitudeSpectrum = 20*np.log(np.abs(dft_shift))
    Real = dft_shift.real
    Imag = dft_shift.imag
    ComponentsList=[magnitudeSpectrum,phaseSpectrum,Real,Imag]
    return ComponentsList
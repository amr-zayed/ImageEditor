from PIL import Image as mg
import cv2
from matplotlib import pyplot as plt
import numpy as np
def FT(img,isfour):
    if isfour==True:
        # img[i] = open(self.PathsList[i])
        #img[i]= cv2.imread(self.PathsList[i],0)
        # img[i]= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        dft= np.fft.fft2(img)
        dft_shift = np.fft.fftshift(dft)
        phaseSpectrum = np.angle(dft_shift)
        magnitudeSpectrum = 20*np.log(np.abs(dft_shift))
        Real = dft_shift.real
        Imag = dft_shift.imag
        img_mod_Phase = np.abs(np.fft.ifft2(phaseSpectrum))
        img_mod_magnitude= np.abs(np.fft.ifft2(magnitudeSpectrum))
        img_mod_Real= np.abs(np.fft.ifft2(Real))
        img_mod_Imag= np.abs(np.fft.ifft2(Imag))

        ComponentsList=[img_mod_magnitude,img_mod_Phase,img_mod_Real,img_mod_Imag]
        return ComponentsList
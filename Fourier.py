from matplotlib import pyplot as plt
import numpy as np
def FT(img,isfour):
    dft= np.fft.fft2(img)
    dft_shift = np.fft.fftshift(dft)
    phaseSpectrum = np.angle(dft_shift)
    magnitudeSpectrum = 20*np.log(np.abs(dft_shift))
    Real = dft_shift.real
    Imag = dft_shift.imag
    img_mod_Phase = phaseSpectrum
    img_mod_magnitude= magnitudeSpectrum
    img_mod_Real= Real
    img_mod_Imag= Imag
    if isfour==True:
        ComponentsList=[img_mod_magnitude,img_mod_Phase,img_mod_Real,img_mod_Imag]
    else:
        Uniform_magnitude =np.ones(magnitudeSpectrum.shape)*5
        Uniform_phase =np.zeros(phaseSpectrum.shape)
        ComponentsList=[img_mod_magnitude,img_mod_Phase,img_mod_Real,img_mod_Imag, Uniform_magnitude, Uniform_phase]

    return ComponentsList
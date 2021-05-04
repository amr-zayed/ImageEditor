from matplotlib import pyplot as plt
import numpy as np
def FT(img,isfour):
    dft= np.fft.fft2(img)
    dft_shift = np.fft.fftshift(dft)
    phaseSpectrum = np.angle(dft_shift)
    magnitudeSpectrum = 20*np.log(np.abs(dft_shift))
    Real = dft_shift.real
    Imag = dft_shift.imag
   
    if isfour==True:
        ComponentsList=[magnitudeSpectrum,phaseSpectrum,Real,Imag]
    else:
        UniformMagnitude =np.ones(magnitudeSpectrum.shape)*5
        UniformPhase =np.zeros(phaseSpectrum.shape)
        ComponentsList=[magnitudeSpectrum,phaseSpectrum,Real,Imag, UniformMagnitude, UniformPhase]

    return ComponentsList
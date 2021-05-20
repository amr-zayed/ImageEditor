from matplotlib import pyplot as plt
import numpy as np
def FT(img):
    dft= np.fft.fft2(img)
    dft_shift = np.fft.fftshift(dft)
    phaseSpectrum = np.angle(dft)
    magnitudeSpectrum = np.abs(dft)
    Real = dft_shift.real
    Imag = dft_shift.imag
    ComponentsList=[magnitudeSpectrum,phaseSpectrum,Real,Imag]

    return ComponentsList
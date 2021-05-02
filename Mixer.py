from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
import numpy as np
from numpy import asarray 
from PIL.Image import open
from Fourier import FT
from PIL.Image import fromarray
from PIL import ImageQt
from Image import Image

class Mixer(QWidget):
    def __init__(self, PathList, count, parent=None):
        QWidget.__init__(self, parent=parent)
        Image1=Image(PathList[0],count)
        Image2=Image(PathList[1],count)
        self.MixerImage = QPixmap()




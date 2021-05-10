from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from FourierDisplayer import MplCanvas
import numpy as np

class MixerDisplayer(FigureCanvasQTAgg):
    def __init__(self, PathList, count, parent=None):
        self.fig = Figure()
        self.MixerDisplayer = self.fig.add_subplot(111)
        super(MixerDisplayer, self).__init__(self.fig)

        self.slider1=0
        self.slider2=0
        self.Component1Image=0
        self.Component2Image=0
        self.Component1Type=0
        self.Component2Type=1

        self.Image1= MplCanvas(PathList[0],count)
        self.Image2= MplCanvas(PathList[1],count)

        self.GetMixedList()

    def Display(self):
        self.MixerDisplayer.cla()
        self.fig.subplots_adjust(bottom=0, top=1, left=0, right=1)
        self.MixerDisplayer.imshow(self.MixedList, cmap='gray', vmin=0, vmax=255)
        self.MixerDisplayer.set_axis_off()
        self.draw()

    def SetMixingVariables(self, slider1=0, slider2=0, comp1=0, comp2=0, comp1img=0, comp2img=0):
        self.slider1 =  slider1
        self.slider2 = slider2
        self.Component1Image = comp1img  
        self.Component2Image = comp2img
        self.Component1Type = comp1
        self.Component2Type = comp2

        self.GetMixedList()
        self.Display()

    def GetMixedList(self):
        if self.Component1Image==0:
            comp1ListImage1 = self.Image1.Image.FourierLists[self.Component1Type]
            comp1ListImage2 = self.Image2.Image.FourierLists[self.Component1Type]
        elif self.Component1Image==1:
            comp1ListImage1 = self.Image2.Image.FourierLists[self.Component1Type]
            comp1ListImage2 = self.Image1.Image.FourierLists[self.Component1Type]
        if self.Component2Image==0:
            comp2ListImage1 = self.Image1.Image.FourierLists[self.Component2Type]
            comp2ListImage2 = self.Image2.Image.FourierLists[self.Component2Type]
        elif self.Component2Image==1:
            comp2ListImage1 = self.Image2.Image.FourierLists[self.Component2Type]
            comp2ListImage2 = self.Image1.Image.FourierLists[self.Component2Type]
        
        Comp1 = comp1ListImage1*(self.slider1/100) + comp1ListImage2*(1-(self.slider1/100))
        Comp2 = comp2ListImage1*(self.slider2/100) + comp2ListImage2*(1-(self.slider2/100))

        if self.Component1Type == 0 or self.Component1Type == 1:
            if self.Component2Type == 0 or self.Component2Type == 1:
                if self.Component1Type == 0:
                    Comp2 = np.exp(1j*np.angle(Comp2))
                    self.MixedList = np.fft.ifft2(Comp1*Comp2)
                else:
                    Comp1 = np.exp(1j*Comp1)
                    self.MixedList = np.fft.ifft2(Comp2*Comp1)
                self.MixedList = np.abs(self.MixedList)
            else:
                if self.Component2Type == 4:
                    Comp1 = np.exp(1j*np.angle(Comp1))
                self.MixedList = np.fft.ifft2(Comp1)
                self.MixedList = np.abs(self.MixedList)
                if self.Component2Type == 4:
                    self.MixedList *= 10000

        if self.Component1Type == 2 or self.Component1Type == 3:
            if self.Component1Type == 2:
                real = Comp1
                imaginary = 1j * (Comp2)
            else:
                real = Comp2
                imaginary = 1j * (Comp1)
            self.MixedList = real + imaginary
            self.MixedList = np.fft.ifft2(self.MixedList)
            self.MixedList = np.abs(self.MixedList)
        
        if self.Component1Type == 4 or self.Component1Type == 5:
            if self.Component2Type == 4 or self.Component2Type == 5:
                self.MixedList = np.ones(comp1ListImage1.shape)

            if self.Component2Type == 0 or self.Component2Type == 1:
                if self.Component1Type == 4:
                    Comp2 = np.exp(1j*np.angle(Comp2))
                self.MixedList = np.fft.ifft2(Comp2)
                self.MixedList = np.abs(self.MixedList)
                if self.Component1Type == 4:
                    self.MixedList *= 10000
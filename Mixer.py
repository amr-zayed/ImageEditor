from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from FourierDisplayer import MplCanvas

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
        self.Component2Type=0

        self.Image1= MplCanvas(PathList[0],count)
        self.Image2= MplCanvas(PathList[1],count)

        self.GetMixedList()

    def Display(self):
        self.MixerDisplayer.cla()
        self.fig.subplots_adjust(bottom=0, top=1, left=0, right=1)
        self.MixerDisplayer.imshow(self.MixedList)
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
            comp1List = self.Image1.Image.FourierLists[self.Component1Type]
        elif self.Component1Image==1:
            comp1List = self.Image2.Image.FourierLists[self.Component1Type]
        
        if self.Component2Image==0:
            comp2List = self.Image1.Image.FourierLists[self.Component2Type]
        elif self.Component2Image==1:
            comp2List = self.Image2.Image.FourierLists[self.Component2Type]
        
        self.MixedList = comp1List*(self.slider1/100) + comp2List*(self.slider2/100)

    
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from Image import Image
from numpy import abs, log, exp, angle 
from numpy.fft import fftshift

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, path, count, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure()
        self.ImageDisplayer = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

        self.GraphData = None
        self.Image = Image(path, count)
        self.Image.SetFourierLists()
        self.GraphData = 20*log(self.Image.FourierLists[0])
        
        
    def Display(self):
        self.ImageDisplayer.cla()
        self.fig.subplots_adjust(bottom=0, top=1, left=0, right=1)
        self.ImageDisplayer.imshow(self.GraphData, cmap='gray', vmin=0, vmax=255)
        self.ImageDisplayer.set_axis_off()
        self.draw()
    
    def SetGraphData(self, index):
        print(index)
        if index == 0:
            self.GraphData = 20*log(self.Image.FourierLists[index])
        elif index == 1 or index == 2 or index == 3:
            self.GraphData = self.Image.FourierLists[index]
        self.Display()
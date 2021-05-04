from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from Image import Image

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, path, count, parent=None, width=5, height=4, dpi=100):
        #fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig = Figure()
        self.ImageDisplayer = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

        self.GraphData = None
        self.Image = Image(path, count)
        self.Image.SetFourierLists()
        self.GraphData = self.Image.FourierLists[0]
        
        
    def Display(self):
        self.ImageDisplayer.cla()
        self.fig.subplots_adjust(bottom=0, top=1, left=0, right=1)
        self.ImageDisplayer.imshow(self.GraphData)
        self.ImageDisplayer.set_axis_off()
        self.draw()
    
    def SetGraphData(self, index):
        self.GraphData = self.Image.FourierLists[index]
        self.Display()
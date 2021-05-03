import numpy as np

from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from Image import Image

"""
class MyMplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #fig = Figure()
        self.Input = fig.add_subplot(111)


        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

class MyDynamicMplCanvas(MyMplCanvas):

    def __init__(self, path, count, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        self.Graph = Image(path, count)
        self.Graph.SetFourierLists()
        self.MainData = self.Graph.FourierLists[0]

    def Display(self):
        self.Input.plot(self.MainData)
        print(type(self.MainData))
        print(self.MainData)
"""
"""class MyDynamicMplCanvas(QWidget):
    def __init__(self, path, count, parent=None,):
        QWidget.__init__(self, parent=parent)
        #super().__init__(parent)

        self.figure = Figure(figsize=(5, 3))
        self.canvas = FigureCanvas(self.figure)
        self.Graph = self.figure.subplots()

        self.GraphData = Image(path, count)
        self.GraphData.SetFourierLists()
        self.MainData = self.GraphData.FourierLists[0]        

    def Display(self):
        print(self.MainData)
        self.Graph.imshow(self.MainData)
        self.Graph.set_axis_off()"""

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
        self.ImageDisplayer.imshow(self.GraphData)
        self.ImageDisplayer.set_axis_off()
        self.draw()
    
    def SetGraphData(self, index):
        print(index)
        self.GraphData = self.Image.FourierLists[index]
        self.Display()

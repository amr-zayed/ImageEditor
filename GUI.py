from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from ImageDisplay import ImageDisplay
from Image import Image
from numpy import log
#from C_Functions import *
#from C_Functions import C_Functions
from ctypes import c_double, c_int, CDLL
import sys

import logging

InfoLogger = logging.getLogger(__name__)
InfoLogger.setLevel(logging.INFO)

DebugLogger = logging.getLogger(__name__)
DebugLogger.setLevel(logging.DEBUG)

FileHandler = logging.FileHandler('ImageEditor.log')
Formatter = logging.Formatter('%(levelname)s:%(filename)s:%(funcName)s:   %(message)s')
FileHandler.setFormatter(Formatter)
InfoLogger.addHandler(FileHandler)
DebugLogger.addHandler(FileHandler)

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")
        self.resize(500,300)
        self.main_widget = QtWidgets.QWidget(self)
        
        self.ImageDisplayList = []
        
        #instanse of c_functions
        #self.CFunctions=C_Functions()

        #Adding File in menubar
        self.file_menu = QtWidgets.QMenu('File', self)
        self.file_menu.addAction('Open File', self.SelectFiles, QtCore.Qt.CTRL + QtCore.Qt.Key_O)
        self.file_menu.addAction('Show Graphs', self.Show_Graphs, QtCore.Qt.CTRL + QtCore.Qt.Key_O)
        self.file_menu.addAction('Quit', self.fileQuit, QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.Layout_AllImages = QtWidgets.QGridLayout()
        self.ControlsColor = QtWidgets.QWidget()
        self.Layout_Controls = QtWidgets.QVBoxLayout(self.ControlsColor)
        self.ControlsColor.setStyleSheet("background-color:#d9d9d9;")
        self.Layout_Main = QtWidgets.QGridLayout(self.main_widget)
        self.Layout_Main.addLayout(self.Layout_AllImages,0,0)
        self.Layout_Main.addLayout(self.Layout_Controls,0,1)
        self.Layout_Main.addWidget(self.ControlsColor,0,1)
        self.Layout_Main.setColumnStretch(0,4)
        self.Layout_Main.setColumnStretch(1,1)
        self.Layout_Main.setContentsMargins(0, 0, 0, 0)

        self.ImagesSignalMapper = QtCore.QSignalMapper()

        self.Image1Label = QtWidgets.QLabel("Image 1")
        self.Image1Label.setFont(QFont('impact', 15))
        self.Image1ComboBox = QtWidgets.QComboBox()
        self.Image1ComboBox.addItems(["Magnitude", "Phase", "Real component", "Imaginary component"])
        self.Image1ComboBox.currentIndexChanged.connect(self.ImagesSignalMapper.map)
        self.ImagesSignalMapper.setMapping(self.Image1ComboBox, 0)
        self.Layout_Image1 = QtWidgets.QGridLayout()
        self.Layout_Image1.addWidget(self.Image1Label,0,0)
        self.Layout_Image1.addWidget(self.Image1ComboBox,0,1)

        self.Image2Label = QtWidgets.QLabel("Image 2")
        self.Image2Label.setFont(QFont('impact', 15))
        self.Image2ComboBox = QtWidgets.QComboBox()
        self.Image2ComboBox.addItems(["Magnitude", "Phase", "Real component", "Imaginary component"])
        self.Image2ComboBox.currentIndexChanged.connect(self.ImagesSignalMapper.map)
        self.ImagesSignalMapper.setMapping(self.Image2ComboBox, 1)
        self.Layout_Image2 = QtWidgets.QGridLayout()
        self.Layout_Image2.addWidget(self.Image2Label,0,0)
        self.Layout_Image2.addWidget(self.Image2ComboBox,0,1)
        
        self.ImagesSignalMapper.mapped.connect(self.ImageIndexChanged)

        self.Layout_Output1 = QtWidgets.QGridLayout()
        self.Layout_Output2 = QtWidgets.QGridLayout()

        self.Output1Label = QtWidgets.QLabel("Output 1")
        self.Output1Label.setFont(QFont('impact', 15))
        self.Output1Label.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        
        self.Output2Label = QtWidgets.QLabel("Output 2")
        self.Output2Label.setFont(QFont('impact', 15))
        self.Output2Label.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)

        self.Layout_1stMixer = QtWidgets.QHBoxLayout()
        self.MixerLabel = QtWidgets.QLabel("Mixer output to:")
        self.MixerLabel.setFont(QFont('Helvetica [Cronyx]', 10))
        self.OutputSelectorComboBox = QtWidgets.QComboBox()
        self.OutputSelectorComboBox.addItems(["Output 1", "Output 2"])
        self.OutputSelectorComboBox.currentIndexChanged.connect(lambda: self.MixerOuputChanged())
        self.OutputSelectorComboBox.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        self.Layout_1stMixer.addWidget(self.MixerLabel)
        self.Layout_1stMixer.addWidget(self.OutputSelectorComboBox)

        self.ComponentMapper = QtCore.QSignalMapper()

        self.Layout_2ndMixer = QtWidgets.QHBoxLayout()
        self.component1Label = QtWidgets.QLabel("Component 1:")
        self.component1Label.setFont(QFont('Helvetica [Cronyx]', 10))
        self.Comp1ImgSelectorComboBox = QtWidgets.QComboBox()
        self.Comp1ImgSelectorComboBox.addItems(["Image 1", "Image 2"])
        self.Comp1ImgSelectorComboBox.currentIndexChanged.connect(self.ComponentMapper.map)
        self.ComponentMapper.setMapping(self.Comp1ImgSelectorComboBox, 0)
        self.Comp1ImgSelectorComboBox.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        self.Layout_2ndMixer.addWidget(self.component1Label)
        self.Layout_2ndMixer.addWidget(self.Comp1ImgSelectorComboBox)

        self.Layout_3rdMixer = QtWidgets.QHBoxLayout()
        self.Comp1TypeComboBox = QtWidgets.QComboBox()
        self.Comp1TypeComboBox.addItems(["Magnitude", "Phase", "Real", "Imaginary", "uniform magnitude", "uniform phase"])
        self.Comp1TypeComboBox.currentIndexChanged.connect(self.ComponentMapper.map)
        self.ComponentMapper.setMapping(self.Comp1TypeComboBox, 1)
        self.Layout_3rdMixer.addWidget(self.Comp1TypeComboBox)

        self.Component1Slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.Component1Slider.sliderReleased.connect(self.ComponentMapper.map)
        self.ComponentMapper.setMapping(self.Component1Slider, 2)
        
        self.Layout_4thMixer = QtWidgets.QHBoxLayout()
        self.component2Label = QtWidgets.QLabel("Component 2:")
        self.component2Label.setFont(QFont('Helvetica [Cronyx]', 10))
        self.Comp2ImgSelectorComboBox = QtWidgets.QComboBox()
        self.Comp2ImgSelectorComboBox.currentIndexChanged.connect(self.ComponentMapper.map)
        self.ComponentMapper.setMapping(self.Comp2ImgSelectorComboBox, 3)
        self.Comp2ImgSelectorComboBox.addItems(["Image 1", "Image 2"])
        self.Comp2ImgSelectorComboBox.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        self.Layout_4thMixer.addWidget(self.component2Label)
        self.Layout_4thMixer.addWidget(self.Comp2ImgSelectorComboBox)

        self.Component2Slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.Component2Slider.sliderReleased.connect(self.ComponentMapper.map)
        self.ComponentMapper.setMapping(self.Component2Slider, 5)

        self.Layout_5thMixer = QtWidgets.QHBoxLayout()
        self.Comp2TypeComboBox = QtWidgets.QComboBox()
        self.Comp2TypeComboBox.currentIndexChanged.connect(self.ComponentMapper.map)
        self.ComponentMapper.setMapping(self.Comp2TypeComboBox, 4)
        self.Comp2TypeComboBox.addItems(["Magnitude", "Phase", "Real", "Imaginary", "uniform magnitude", "uniform phase"])
        self.Comp2TypeComboBox.setCurrentIndex(1)
        self.Layout_5thMixer.addWidget(self.Comp2TypeComboBox)

        self.ComponentMapper.mapped.connect(self.ComponentChanged)

        self.ImageList = []
        for _ in range(6):
            self.ImageDisplayList.append(ImageDisplay())

        self.Layout_Output1.addWidget(self.Output1Label, 0,0)
        self.Layout_Output1.setRowStretch(0,1)
        self.Layout_Output1.addWidget(self.ImageDisplayList[4],1,0)
        self.Layout_Output1.setRowStretch(1,30)
        self.Layout_Output2.addWidget(self.Output2Label, 0,0)
        self.Layout_Output2.setRowStretch(0,1)
        self.Layout_Output2.addWidget(self.ImageDisplayList[5],1,0)
        self.Layout_Output2.setRowStretch(1,30)

        self.Layout_Image1.addWidget(self.ImageDisplayList[0],1,0)
        self.Layout_Image1.addWidget(self.ImageDisplayList[1],1,1)
        self.Layout_Image1.setRowStretch(1,30)
        self.Layout_Image2.addWidget(self.ImageDisplayList[2],1,0)
        self.Layout_Image2.addWidget(self.ImageDisplayList[3],1,1)
        self.Layout_Image2.setRowStretch(1,30)

        self.Layout_Controls.addLayout(self.Layout_1stMixer)
        self.Layout_Controls.addStretch(2)
        self.Layout_Controls.addLayout(self.Layout_2ndMixer)
        self.Layout_Controls.addLayout(self.Layout_3rdMixer)
        self.Layout_Controls.addWidget(self.Component1Slider)
        self.Layout_Controls.addStretch(1)
        self.Layout_Controls.addLayout(self.Layout_4thMixer)
        self.Layout_Controls.addLayout(self.Layout_5thMixer)
        self.Layout_Controls.addWidget(self.Component2Slider)
        self.Layout_Controls.addStretch(50)

        self.Layout_AllImages.addLayout(self.Layout_Image1, 1,1)
        self.Layout_AllImages.addLayout(self.Layout_Image2, 3,1)
        self.Layout_AllImages.addLayout(self.Layout_Output1, 1,3)
        self.Layout_AllImages.addLayout(self.Layout_Output2, 3,3)
        self.Layout_AllImages.setColumnStretch(0,1)
        self.Layout_AllImages.setColumnStretch(1,30)
        self.Layout_AllImages.setColumnStretch(2,1)
        self.Layout_AllImages.setColumnStretch(3,20)
        self.Layout_AllImages.setRowStretch(0,1)
        self.Layout_AllImages.setRowStretch(1,30)
        self.Layout_AllImages.setRowStretch(2,1)
        self.Layout_AllImages.setRowStretch(3, 30)

        self.ComponentTypeComboBoxes = []
        self.ComponentTypeComboBoxes.append(self.Comp1TypeComboBox)
        self.ComponentTypeComboBoxes.append(self.Comp2TypeComboBox)
        #Creating A messagebox For errors
        self.MessageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "Error", "Error")

        #Disabling components
        self.EnableComponents(False)
    
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        self.resize(1280,720)

        self.OutputIndex = 4
        InfoLogger.info("GUI created")

    def fileQuit(self):
        InfoLogger.info("App closed")
        self.close()

    def DisplayError(self, title, Message):
        DebugLogger.debug('{}\n'.format(title))
        self.MessageBox.setWindowTitle(title)
        self.MessageBox.setText(Message)
        self.MessageBox.exec()

    def open_dialog_box(self):
        filename = QtWidgets.QFileDialog.getOpenFileNames()
        Imagepaths = filename[0]
        DebugLogger.debug('Number of images selected:{}'.format(len(Imagepaths)))
        while len(Imagepaths)!=2 and len(Imagepaths)!=0:
            self.DisplayError("SELECTION ERROR", "you should select exactly 2 images")
            filename = QtWidgets.QFileDialog.getOpenFileNames()
            Imagepaths = filename[0]
            DebugLogger.debug('Number of images selected:{}'.format(len(Imagepaths)))
    
        for path in Imagepaths:
            i=0
            FileName = ""
            while path[i] != ".":
                if path[i] == '/':
                    FileName =""
                else:
                    FileName = FileName + path[i]
                i=i+1
            FileName = FileName + path[i:]
            DebugLogger.debug('FileName:{}'.format(FileName))
            if path[i:] != ".png" and path[i:] != ".JPG" and path[i:] != ".jpg" and path[i:] != ".PNG":
                self.DisplayError("FILE TYPE ERROR", "File type must be an image (e.g. png or jpg)")
                Imagepaths = self.open_dialog_box()
                break
            
        return Imagepaths

    def SelectFiles(self):
        Imagepaths = self.open_dialog_box()

        if len(Imagepaths)==0:
            return

        for i in range(2):
            self.ImageList.append(Image(Imagepaths[i]))
            InfoLogger.info('\nPath of image {} added and initialized'.format(i+1))

        if not self.SimilarSize():
            self.DisplayError("DIMENSION ERROR", "The 2 images must have same size")
            self.ImageList = []
            self.SelectFiles()
        else:
            InfoLogger.info('Images selected successfully')
            self.EnableComponents(True)
            self.ImageList[0].SetFourierLists()
            self.ImageList[1].SetFourierLists()
            for i in range(2):
                self.ImageDisplayList[2*i].Display(self.ImageList[i].GetMainImage())
                InfoLogger.info('Displayer {} Generated Successfully'.format(2*i))
                self.ImageDisplayList[2*i+1].Display(self.ImageList[i].GetFourierElement(0))
                InfoLogger.info('Displayer {} Generated Successfully'.format(2*i+1))
                self.ImageDisplayList[i+4].Display(self.ImageList[i].GetMixedList(self.ImageList[-i+1], comp2type=1))
                InfoLogger.info('Displayer {} Generated Successfully'.format(i+4))

    def SimilarSize(self):
        DebugLogger.debug('Image1 dimensions {}x{}, Image2 dimensions {}x{}'.format(self.ImageList[0].height(), self.ImageList[0].width(), self.ImageList[1].height(), self.ImageList[1].width()))      
        if self.ImageList[0].height() != self.ImageList[1].height() or self.ImageList[0].width() != self.ImageList[1].width():
            return False  
        return True

    def ImageIndexChanged(self, index):
        if index == 0:
            InfoLogger.info('Signal emited: comboBox of image 1 changed to:{}'.format(self.Image1ComboBox.currentText()))
            self.ImageDisplayList[1].Display(self.ImageList[0].GetFourierElement(self.Image1ComboBox.currentIndex()))
        if index == 1:
            InfoLogger.info('Signal emited: comboBox of image 2 changed to:{}'.format(self.Image1ComboBox.currentText()))
            self.ImageDisplayList[3].Display(self.ImageList[1].GetFourierElement(self.Image2ComboBox.currentIndex()))

    def MixerOuputChanged(self):
        InfoLogger.info('Signal emited: {} activated'.format(self.OutputSelectorComboBox.currentText()))
        self.OutputIndex = self.OutputSelectorComboBox.currentIndex()+4 

    def ComponentChanged(self, index):
        InfoLogger.info('Signal emited: component 1 image {} [fourier component: {}, slider value: {}]'.format(self.Comp1ImgSelectorComboBox.currentIndex()+1, self.Comp1TypeComboBox.currentText(), self.Component1Slider.value()))
        InfoLogger.info('Signal emited: component 2 image {} [fourier component: {}, slider value: {}]'.format(self.Comp2ImgSelectorComboBox.currentIndex()+1, self.Comp2TypeComboBox.currentText(), self.Component2Slider.value()))
        AddIndex = 1
        for i in range(2):
            if i==1:
                AddIndex = -1
            if self.ComponentTypeComboBoxes[i].currentIndex() == 0:
                if self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 0 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 2 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 3 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 4:
                    self.DisplayError("MIXER ERROR", "Magnitude component can be matched only with phase or uniform phase")
                    return

        AddIndex = 1
        for i in range(2):
            if i==1:
                AddIndex = -1
            if self.ComponentTypeComboBoxes[i].currentIndex() == 1:
                if self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 1 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 2 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 3 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 5:
                    self.DisplayError("MIXER ERROR", "Phase component can be matched only with magnitude or uniform magnitude")
                    return
        
        AddIndex = 1
        for i in range(2):
            if i==1:
                AddIndex = -1
            if self.ComponentTypeComboBoxes[i].currentIndex() == 2:
                if self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 0 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 1 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 2 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 4 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 5:
                    self.DisplayError("MIXER ERROR", "Real component can be matched only with imaginary")
                    return
        
        AddIndex = 1
        for i in range(2):
            if i==1:
                AddIndex = -1
            if self.ComponentTypeComboBoxes[i].currentIndex() == 3:
                if self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 0 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 1 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 3 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 4 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 5:
                    self.DisplayError("MIXER ERROR", "Imaginary component can be matched only with real")
                    return

        AddIndex = 1
        for i in range(2):
            if i==1:
                AddIndex = -1
            if self.ComponentTypeComboBoxes[i].currentIndex() == 4:
                if self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 0 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 2 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 3 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 4:
                    self.DisplayError("MIXER ERROR", "Uniform magnitude component can be matched only with phase or uniform phase")
                    return

        AddIndex = 1
        for i in range(2):
            if i==1:
                AddIndex = -1
            if self.ComponentTypeComboBoxes[i].currentIndex() == 5:
                if self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 1 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 2 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 3 or self.ComponentTypeComboBoxes[i+AddIndex].currentIndex() == 5:
                    self.DisplayError("MIXER ERROR", "Uniform phase component can be matched only with magnitude or uniform magnitude")
                    return
        
        MixedList = self.ImageList[self.OutputIndex-4].GetMixedList(self.ImageList[-self.OutputIndex+5], slider1=self.Component1Slider.value(),
        slider2=self.Component2Slider.value(),
        comp1type=self.Comp1TypeComboBox.currentIndex(),
        comp2type=self.Comp2TypeComboBox.currentIndex(),
        comp1img=self.Comp1ImgSelectorComboBox.currentIndex(),
        comp2img=self.Comp2ImgSelectorComboBox.currentIndex())
        
        self.ImageDisplayList[self.OutputIndex].Display(MixedList)

    def EnableComponents(self, bool):
        self.Image1ComboBox.setEnabled(bool)
        self.Image2ComboBox.setEnabled(bool)
        self.Comp1TypeComboBox.setEnabled(bool)
        self.Comp2TypeComboBox.setEnabled(bool)
        self.Comp1ImgSelectorComboBox.setEnabled(bool)
        self.Comp2ImgSelectorComboBox.setEnabled(bool)
        self.OutputSelectorComboBox.setEnabled(bool)
        self.Component1Slider.setEnabled(bool)
        self.Component2Slider.setEnabled(bool)

    def Show_Graphs(self):
        pass
        #self.CFunctions.c_graphs()
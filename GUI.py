from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from ImageDisplay import ImageDisplay

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")
        self.resize(500,300)
        self.main_widget = QtWidgets.QWidget(self)
        
        self.ImageDisplayList = []
        
        #Adding File in menubar
        self.file_menu = QtWidgets.QMenu('File', self)
        self.file_menu.addAction('Open File', self.SelectFiles, QtCore.Qt.CTRL + QtCore.Qt.Key_O)
        self.file_menu.addAction('Quit', self.fileQuit, QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.Layout_AllImages = QtWidgets.QGridLayout()
        self.ControlsColor = QtWidgets.QWidget()
        self.Layout_Controls = QtWidgets.QVBoxLayout(self.ControlsColor)
        self.ControlsColor.setStyleSheet("background-color:#d9d9d9;")
        self.Layout_Main = QtWidgets.QGridLayout(self.main_widget)
        self.Layout_Main.addLayout(self.Layout_AllImages,0,0)
        self.Layout_Main.addWidget(self.ControlsColor,0,1)
        self.Layout_Main.addLayout(self.Layout_Controls,0,1)
        self.Layout_Main.setColumnStretch(0,4)
        self.Layout_Main.setColumnStretch(1,1)

        self.Image1Label = QtWidgets.QLabel("Image 1")
        self.Image1ComboBox = QtWidgets.QComboBox()
        self.Image1ComboBox.addItems(["Magnitude", "Phase", "Real component", "Imaginary component"])
        #self.Image1ComboBox.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.Layout_Image1 = QtWidgets.QGridLayout()
        self.Layout_Image1.addWidget(self.Image1Label,0,0)
        self.Layout_Image1.addWidget(self.Image1ComboBox,0,1)

        self.Image2Label = QtWidgets.QLabel("Image 2")
        self.Image2ComboBox = QtWidgets.QComboBox()
        self.Image2ComboBox.addItems(["Magnitude", "Phase", "Real component", "Imaginary component"])
        #self.Image2ComboBox.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.Layout_Image2 = QtWidgets.QGridLayout()
        self.Layout_Image2.addWidget(self.Image2Label,0,0)
        self.Layout_Image2.addWidget(self.Image2ComboBox,0,1)
        
        for _ in range(6):
            self.ImageDisplayList.append(ImageDisplay())

        self.Layout_Image1.addWidget(self.ImageDisplayList[0],1,0)
        self.Layout_Image1.addWidget(self.ImageDisplayList[1],1,1)
        
        self.Layout_Image2.addWidget(self.ImageDisplayList[2],1,0)
        self.Layout_Image2.addWidget(self.ImageDisplayList[3],1,1)

        self.Layout_Output1 = QtWidgets.QVBoxLayout()
        self.Layout_Output2 = QtWidgets.QVBoxLayout()

        self.Output1Label = QtWidgets.QLabel("Output 1")
        self.Output1Label.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.Output2Label = QtWidgets.QLabel("Output 2")
        self.Output2Label.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)

        self.Layout_Output1.addWidget(self.Output1Label)
        self.Layout_Output1.addWidget(self.ImageDisplayList[4])
        self.Layout_Output2.addWidget(self.Output2Label)
        self.Layout_Output2.addWidget(self.ImageDisplayList[5])

        self.Layout_1stMixer = QtWidgets.QHBoxLayout()
        self.MixerLabel = QtWidgets.QLabel("Mixer Output to:")
        self.OutputSelectorComboBox = QtWidgets.QComboBox()
        self.OutputSelectorComboBox.addItems(["Output 1", "Output 2"])
        self.OutputSelectorComboBox.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        self.Layout_1stMixer.addWidget(self.MixerLabel)
        self.Layout_1stMixer.addWidget(self.OutputSelectorComboBox)

        self.Layout_2ndMixer = QtWidgets.QHBoxLayout()
        self.component1Label = QtWidgets.QLabel("Component 1:")
        self.Comp1ImgSelectorComboBox = QtWidgets.QComboBox()
        self.Comp1ImgSelectorComboBox.addItems(["Image 1", "Image 2"])
        self.Component1Slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.Layout_2ndMixer.addWidget(self.component1Label)
        self.Layout_2ndMixer.addWidget(self.Comp1ImgSelectorComboBox)
        self.Layout_2ndMixer.addWidget(self.Component1Slider)

        self.Layout_3rdMixer = QtWidgets.QHBoxLayout()
        self.Comp1TypeComboBox = QtWidgets.QComboBox()
        self.Comp1TypeComboBox.addItems(["Magnitude", "Phase", "Real", "Imaginary", "uniform magnitude", "uniform phase"])
        self.Layout_3rdMixer.addWidget(self.Comp1TypeComboBox)
        
        self.Layout_4thMixer = QtWidgets.QHBoxLayout()
        self.component2Label = QtWidgets.QLabel("Component 2:")
        self.Comp2ImgSelectorComboBox = QtWidgets.QComboBox()
        self.Comp2ImgSelectorComboBox.addItems(["Image 1", "Image 2"])
        self.Component2Slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.Layout_4thMixer.addWidget(self.component2Label)
        self.Layout_4thMixer.addWidget(self.Comp2ImgSelectorComboBox)
        self.Layout_4thMixer.addWidget(self.Component2Slider)

        self.Layout_5thMixer = QtWidgets.QHBoxLayout()
        self.Comp2TypeComboBox = QtWidgets.QComboBox()
        self.Comp2TypeComboBox.addItems(["Magnitude", "Phase", "Real", "Imaginary", "uniform magnitude", "uniform phase"])
        self.Layout_5thMixer.addWidget(self.Comp2TypeComboBox)

        # self.Layout_Controls.addStretch(0)
        self.Layout_Controls.addLayout(self.Layout_1stMixer)
        self.Layout_Controls.addStretch(2)
        self.Layout_Controls.addLayout(self.Layout_2ndMixer)
        self.Layout_Controls.addLayout(self.Layout_3rdMixer)
        self.Layout_Controls.addStretch(1)
        self.Layout_Controls.addLayout(self.Layout_4thMixer)
        self.Layout_Controls.addLayout(self.Layout_5thMixer)
        self.Layout_Controls.addStretch(50)

        self.Layout_AllImages.addLayout(self.Layout_Image1, 0,0)
        self.Layout_AllImages.addLayout(self.Layout_Image2, 1,0)
        #self.Layout_AllImages.addWidget(, 0,1)
        #self.Layout_AllImages.addWidget(QtWidgets.QLayoutItem.spacerItem().changeSize(0, 5), 1,1)
        self.Layout_AllImages.addLayout(self.Layout_Output1, 0,2)
        self.Layout_AllImages.addLayout(self.Layout_Output2, 1,2)
        self.Layout_AllImages.setColumnStretch(0,30)
        self.Layout_AllImages.setColumnStretch(1,1)
        self.Layout_AllImages.setColumnStretch(2,20)
        self.Layout_AllImages.setRowStretch(0,2)
        self.Layout_AllImages.setRowStretch(1,2)



        #Creating A messagebox For errors
        self.MessageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "Error", "Error")
    
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        self.resize(1280,720)

    def fileQuit(self):
        self.close()

    def DisplayError(self, title, Message):
        self.MessageBox.setWindowTitle(title)
        self.MessageBox.setText(Message)
        self.MessageBox.exec()

    def open_dialog_box(self):
        filename = QtWidgets.QFileDialog.getOpenFileNames()
        Imagepaths = filename[0]
        while len(Imagepaths)!=2 and len(Imagepaths)!=0:
            self.DisplayError("ERROR", "you should select exactly 2 images")
            filename = QtWidgets.QFileDialog.getOpenFileNames()
            Imagepaths = filename[0]
    
        for path in Imagepaths:
            i=0
            FileName = ""
            while path[i] != ".":
                if path[i] == '/':
                    FileName =""
                else:
                    FileName = FileName + path[i]
                i=i+1

            if path[i:] != ".png" and path[i:] != ".JPG" and path[i:] != ".jpg" and path[i:] != ".PNG":
                self.DisplayError("ERROR", "File type must be an image (e.g. png or jpg)")
                Imagepaths = self.open_dialog_box()
                break
            
        return Imagepaths

    def SelectFiles(self):
        Imagepaths = self.open_dialog_box()

        if len(Imagepaths)==0:
            return

        x=[0,1]
        for path in Imagepaths:
            for i in x:
                self.ImageDisplayList[i].setImage(path)
                
                #FOR GUI PREVIEW ONLY
                if i==0:
                    self.ImageDisplayList[4].setImage(path)
                if i==2:
                    self.ImageDisplayList[5].setImage(path)
            x = [2,3]
        
        """Uncomment this to display images without width hieght check"""
        # for i in range(6):
        #     self.ImageDisplayList[i].Display()

        """Error is here"""
        # if not self.SimilarSize():
        #     self.DisplayError("SIZE ERROR", "The 2 images must have same size")
        #     self.SelectFiles()
        # else:
        #     for i in range(6):
        #         self.ImageDisplayList[i].Display()

    def SimilarSize(self):        
        if self.ImageDisplayList[0].height() != self.ImageDisplayList[2].height() or self.ImageDisplayList[0].width() != self.ImageDisplayList[2].width():
            print("Width check: \nImage 1: ", self.ImageDisplayList[0].width(), "\nImage 2: ", self.ImageDisplayList[1].width(), "\n")
            print("Height check: \nImage 1: ",self.ImageDisplayList[0].height(), "\nImage 2: ", self.ImageDisplayList[1].height(), "\n")
            return False  
        return True

        

        

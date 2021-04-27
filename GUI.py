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
        

        self.ImagesList = []
        self.ImageDisplayList = []
        
        #Adding File in menubar
        self.file_menu = QtWidgets.QMenu('File', self)
        self.file_menu.addAction('Open File', self.SelectFiles, QtCore.Qt.CTRL + QtCore.Qt.Key_O)
        self.file_menu.addAction('Quit', self.fileQuit, QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.MainLayout = QtWidgets.QGridLayout(self.main_widget)
        
        self.Image1Label = QtWidgets.QLabel("Image 1")
        self.Image1ComboBox = QtWidgets.QComboBox()
        self.Image1ComboBox.addItems(["Magnitude", "Phase", "Real component", "Imaginary component"])
        self.Image1Layout = QtWidgets.QGridLayout()
        self.Image1Layout.addWidget(self.Image1Label,0,0)
        self.Image1Layout.addWidget(self.Image1ComboBox,0,1)

        self.Image2Label = QtWidgets.QLabel("Image 2")
        self.Image2ComboBox = QtWidgets.QComboBox()
        self.Image2ComboBox.addItems(["Magnitude", "Phase", "Real component", "Imaginary component"])
        self.Image2Layout = QtWidgets.QGridLayout()
        self.Image2Layout.addWidget(self.Image2Label,0,0)
        self.Image2Layout.addWidget(self.Image2ComboBox,0,1)
        
        for _ in range(6):
            self.ImagesList.append(QImage())
            self.ImageDisplayList.append(ImageDisplay())

        self.Image1Layout.addWidget(self.ImageDisplayList[0],1,0)
        self.Image1Layout.addWidget(self.ImageDisplayList[1],1,1)
        
        self.Image2Layout.addWidget(self.ImageDisplayList[2],1,0)
        self.Image2Layout.addWidget(self.ImageDisplayList[3],1,1)

        self.MainLayout.addLayout(self.Image1Layout, 0,0)
        self.MainLayout.addLayout(self.Image2Layout, 1,0)

        #Creating A messagebox For errors
        self.MessageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "Error", "Error")
    
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

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

            if path[i:] != ".png" and path[i:] != ".JPG" and path[i:] != ".jpg":
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
                print(i)
                self.ImagesList[i].load(path)
                self.ImageDisplayList[i].setPixmap(self.ImagesList[i])
            x = [2,3]
        

        

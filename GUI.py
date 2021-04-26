from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")
        
        self.MainImagesList = []
        
        #Adding File in menubar
        self.file_menu = QtWidgets.QMenu('File', self)
        self.file_menu.addAction('Open File', self.SelectFiles, QtCore.Qt.CTRL + QtCore.Qt.Key_O)
        self.file_menu.addAction('Quit', self.fileQuit, QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        #Creating A messagebox For errors
        self.MessageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "Error", "Error")
    
        self.main_widget = QtWidgets.QWidget(self)
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

            if path[i:] != ".png":
                print(path[i:])
                self.DisplayError("ERROR", "File type must be an image (e.g. png or jpg)")
                Imagepaths = self.open_dialog_box()
                break
            
        return Imagepaths

    def SelectFiles(self):
        Imagepaths = self.open_dialog_box()

        if len(Imagepaths)==0:
            return

        for path in Imagepaths:
            print(path)
        

        

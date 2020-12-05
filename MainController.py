import sys
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog
from MainWin import Ui_MainMenu


class Controller:

    def __init__(self):
        self.mw = QtWidgets.QMainWindow()
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self.mw)
        self.ui.ImgBtn.clicked.connect(self.clickImgBtn)
        self.ui.NgBtn.clicked.connect(self.clickNgBtn)
        self.img = ''


        self.mw.show()

    def clickImgBtn(self):
        dialog = QFileDialog.getOpenFileName()
        self.img = Image.open(dialog[0])
        self.ui.imgPathLineEdit.setText(dialog[0])
        self.ui.imgPathLineEdit.setReadOnly(True)

    def clickNgBtn(self):
        self.img.show()



#MAIN
app = QtWidgets.QApplication(sys.argv)
cntrl = Controller()
sys.exit(app.exec_())

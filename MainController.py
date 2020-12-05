import sys
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog
from MainWin import Ui_MainMenu
from PyQt5.QtGui import QPixmap


class Controller:

    def __init__(self):
        self.mw = QtWidgets.QMainWindow()
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self.mw)
        self.ui.ImgBtn.clicked.connect(self.clickImgBtn)
        self.ui.NgBtn.clicked.connect(self.clickNgBtn)


        self.mw.show()

    def clickImgBtn(self):
        dialog = QFileDialog.getOpenFileName(None, "Open Image", '', "Image Files (*.png *.jpg *.bmp)")
        self.ui.imgPathLineEdit.setText(dialog[0])
        self.ui.imgPathLineEdit.setReadOnly(True)
        pix = QPixmap(dialog[0])
        pix = pix.scaled(630, 630, QtCore.Qt.KeepAspectRatio)
        pix = pix.copy(0,0,200,200)
        item = QtWidgets.QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)
        self.ui.imgView.resize(630,630)
        self.ui.imgView.setScene(scene)

    def clickNgBtn(self):
        pass

class Tiles():

    def __init__(self):
        self.tiles = []

    def createTiles(self,img, dif):
        if dif == 'Easy':
            for x in range(5):
                for y in range(5):
                    # tile =
                    self.tiles.append()

        if dif == 'Normal':
            pass
        if dif == 'Hard':
            pass

#MAIN
app = QtWidgets.QApplication(sys.argv)
cntrl = Controller()
sys.exit(app.exec_())

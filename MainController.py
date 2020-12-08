import sys
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

    def clickImgBtn(self):                  # Kép betöltésére használt gomb metódusa
        dialog = QFileDialog.getOpenFileName(None, "Open Image", '', "Image Files (*.png *.jpg *.bmp)")
        self.ui.imgPathLineEdit.setText(dialog[0])          # Line Edit, amiben láthatjuk a betöltött fotó helyét,
        self.ui.imgPathLineEdit.setReadOnly(True)           # de nem írhatjuk át. Visszajelzés a sikeres betöltésre
        pix = QPixmap(dialog[0])                                # innen a metódus végéig a kép pixmapként való betöltése
        pix = pix.scaled(630, 630)   # kép át méretezése
        # pix = pix.copy(0,0,200,200)                             # Ez a sor csak teszt hogy hogyan tudok körbevágni egy képrészt
        item = QtWidgets.QGraphicsPixmapItem(pix)               # majd a GraphicView GraphicScene-é való állítása
        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)
        # self.ui.imgView.resize(630,630)       # Ez a parancs feleslegesnek tűnik de félek kitörölni, nehogy elfelejtsem
        self.ui.imgView.setScene(scene)
        print(pix.size())

    def clickNgBtn(self):
        pass

class Tiles():          # Félkész class amiben valahogy majd meg akarom oldani a kép kockákra vágását

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

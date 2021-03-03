import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog
from MainWin import Ui_MainMenu
from PyQt5.QtGui import QPixmap
from timeit import default_timer as timer

class Controller:

    def __init__(self):
        self.mw = QtWidgets.QMainWindow()
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self.mw)
        self.ui.ImgBtn.clicked.connect(self.clickImgBtn)
        self.ui.NgBtn.clicked.connect(self.clickNgBtn)
        self.ui.GiveUpBtn.clicked.connect(self.clickGiveUpButton)
        self.imPath = ''
        self.solution = []



        self.mw.show()

    def clickImgBtn(self):                  # Kép betöltésére használt gomb metódusa

        dialog = QFileDialog.getOpenFileName(None, "Open Image", '', "Image Files (*.png *.jpg *.bmp)")
        self.ui.imgPathLineEdit.setText(dialog[0])          # Line Edit, amiben láthatjuk a betöltött fotó helyét,
        self.ui.imgPathLineEdit.setReadOnly(True)           # de nem írhatjuk át. Visszajelzés a sikeres betöltésre
        self.imPath = dialog[0]
        pix = QPixmap(dialog[0])                            # innen a metódus végéig a kép pixmapként való betöltése
        pix = pix.scaled(630, 630)                          # kép át méretezése
        scene = QtWidgets.QGraphicsScene()                  # Kép megjelenítéséhez való Scene és SceneRect inicializálása
        self.ui.imgView.setScene(scene)                     # -||-
        self.ui.imgView.setSceneRect(0, 0, 630, 630)        # -||-
        self.ui.imgView.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)          # Bal fentről való indulás beállítása
        darabok = Tiles()                                   # Tiles class példányosításával
        darabok.createTiles(self.imPath, self.ui.DiffBox.currentText()) # Kép négyzetekre vágása a Tiles class segítségével
        TilesLs = darabok.getTiles()                        # A képrészleteket tartalmazó lista létrehozása
        diff = self.ui.DiffBox.currentText()                # Nehézségkiválasztó helyzete

        x = 0                                                                             # A kép megjelenítése helyesen,
        y = 0                                                                             # de már feldarabolva,
                                                                                          # hogy helyzetüket eltárolva
        if diff =='Easy':                                                                 # lehessen megoldást eltárolni
            for i in TilesLs:                                                             # a pozíciók listája alapján
                item = QtWidgets.QGraphicsPixmapItem(i)
                scene.addItem(item)
                item.setPos(x * (pix.size().height()/5), y * (pix.size().width()/5))
                self.solution.append(item.pos())
                y += 1
                if y == 5:
                    x += 1
                    y = 0
                if x == 5:
                    break

        if diff =='Normal':
            for i in TilesLs:
                item = QtWidgets.QGraphicsPixmapItem(i)
                scene.addItem(item)
                item.setPos(x * (pix.size().height()/7), y * (pix.size().width()/7))
                self.solution.append(item.pos())
                y += 1
                if y == 7:
                    x += 1
                    y = 0
                if x == 7:
                    break

        if diff =='Hard':
            for i in TilesLs:
                item = QtWidgets.QGraphicsPixmapItem(i)
                scene.addItem(item)
                item.setPos(x * (pix.size().height()/9), y * (pix.size().width()/9))
                self.solution.append(item.pos())
                y += 1
                if y == 9:
                    x += 1
                    y = 0
                if x == 9:
                    break



    def clickNgBtn(self):                                                   # New Game gombhoz tartozó funkciók
                                                                            # Kép beolvasása és kijelzése mostmár
        pix = QPixmap(self.imPath)                                          # szétszort darabkákkal, nehézség alapján
        pix = pix.scaled(630, 630)
        scene = QtWidgets.QGraphicsScene()
        self.ui.imgView.setScene(scene)
        self.ui.imgView.setSceneRect(0, 0, 630, 630)
        self.ui.imgView.setAlignment(QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft)
        darabok = Tiles()
        diff = self.ui.DiffBox.currentText()
        darabok.createTiles(self.imPath, diff)
        TilesLs = darabok.getTiles()
        Controller.start = timer()

        x = 0
        y = 0

        if diff == 'Easy':
            for i in TilesLs:
                item = QtWidgets.QGraphicsPixmapItem(i)
                scene.addItem(item)
                item.setPos(y * (pix.size().height()/5), x * (pix.size().width()/5))
                y += 1
                if y == 5:
                    x += 1
                    y = 0
                if x == 5:
                    break

        if diff == 'Normal':
            for i in TilesLs:
                item = QtWidgets.QGraphicsPixmapItem(i)
                scene.addItem(item)
                item.setPos(y * (pix.size().height()/7), x * (pix.size().width()/7))
                y += 1
                if y == 7:
                    x += 1
                    y = 0
                if x == 7:
                    break

        if diff == 'Hard':
            for i in TilesLs:
                item = QtWidgets.QGraphicsPixmapItem(i)
                scene.addItem(item)
                item.setPos(y * (pix.size().height()/9), x * (pix.size().width()/9))
                y += 1
                if y == 9:
                    x += 1
                    y = 0
                if x == 9:
                    break

    def clickGiveUpButton(self):                                    # Give up gomb funkciói, eltelt idő kijelzése
                                                                    # és a kép alaphelyzetbe állítása
        Controller.end = timer()
        Tneeded = Controller.end-Controller.start
        Tneeded = '{time:.2f}'.format(time=Tneeded)
        QtWidgets.QMessageBox.information(None, "You gave up",
                                            'You were trying for {} seconds'.format(Tneeded),
                                            QtWidgets.QMessageBox.Ok)

        pix = QPixmap(self.imPath)
        pix = pix.scaled(630, 630)
        scene = QtWidgets.QGraphicsScene()
        self.ui.imgView.setScene(scene)
        self.ui.imgView.setSceneRect(0, 0, 630, 630)
        self.ui.imgView.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        darabok = Tiles()
        darabok.createTiles(self.imPath, self.ui.DiffBox.currentText())
        TilesLs = darabok.getTiles()
        diff = self.ui.DiffBox.currentText()

        x = 0
        y = 0

        if diff == 'Easy':
            for i in TilesLs:
                item = QtWidgets.QGraphicsPixmapItem(i)
                scene.addItem(item)
                item.setPos(x * (pix.size().height() / 5), y * (pix.size().width() / 5))
                self.solution.append(item.pos())
                y += 1
                if y == 5:
                    x += 1
                    y = 0
                if x == 5:
                    break

        if diff == 'Normal':
            for i in TilesLs:
                item = QtWidgets.QGraphicsPixmapItem(i)
                scene.addItem(item)
                item.setPos(x * (pix.size().height() / 7), y * (pix.size().width() / 7))
                self.solution.append(item.pos())
                y += 1
                if y == 7:
                    x += 1
                    y = 0
                if x == 7:
                    break

        if diff == 'Hard':
            for i in TilesLs:
                item = QtWidgets.QGraphicsPixmapItem(i)
                scene.addItem(item)
                item.setPos(x * (pix.size().height() / 9), y * (pix.size().width() / 9))
                self.solution.append(item.pos())
                y += 1
                if y == 9:
                    x += 1
                    y = 0
                if x == 9:
                    break


class Tiles():          # A kép egyenlő négyzetekre való felvágására szolgáló osztály

    def __init__(self):
        self.tiles = []

    def createTiles(self, img, dif):

        pix = QPixmap(img)
        pix = pix.scaled(630, 630)

        if dif == 'Easy':
            for x in range(5):
                for y in range(5):
                    self.tiles.append(pix.copy(x*int((pix.size().width()/5)), y*int((pix.size().width()/5))
                                               , int((pix.size().width()/5)), int((pix.size().width()/5))))

        if dif == 'Normal':
            for x in range(7):
                for y in range(7):
                    self.tiles.append(pix.copy(x * int((pix.size().width() / 7)), y * int((pix.size().width() / 7))
                                               , int((pix.size().width() / 7)), int((pix.size().width() / 7))))

        if dif == 'Hard':
            for x in range(9):
                for y in range(9):
                    self.tiles.append(pix.copy(x * int((pix.size().width() / 9)), y * int((pix.size().width() / 9))
                                               , int((pix.size().width() / 9)), int((pix.size().width() / 9))))

    def getTiles(self):
        return self.tiles


#MAIN
app = QtWidgets.QApplication(sys.argv)
cntrl = Controller()
sys.exit(app.exec_())

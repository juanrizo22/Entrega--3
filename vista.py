from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import os

class Vista(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('base.ui', self)
        

    def setup(self):
        self.slider.setMinimum(1)
        self.slider.setMaximum(len(self.mi_coordinador.modelo.current_images))
        self.slider.setValue(1)
        self.slider.valueChanged.connect(self.cargar)
        self.pushButton.clicked.connect(self.cerrar)
        self.mostrar_info()

    def addControlador(self, c):
        self.mi_coordinador = c
        self.setup()

    def cargar(self):
        self.mi_coordinador.img_conexion(self.slider.value() - 1)
        pixmap = QPixmap("temp_image.png")
        self.img.setPixmap(pixmap)
        os.remove('temp_image.png')
        self.mostrar_info()

    def mostrar_info(self):
        info = self.mi_coordinador.obtener_info_actual()
        self.info1.setText(info[0])
        self.info2.setText(info[1])
        self.info3.setText(info[2])
        self.info4.setText(info[3])
        self.info5.setText(info[4])

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self, "Error", mensaje)

    def cerrar(self):
        self.hide()

    
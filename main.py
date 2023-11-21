from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
from modelo import Modelo
from vista import Vista
from controlador import Controlador



def main():
    app = QApplication([])
    login=uic.loadUi("login.ui")
    error=uic.loadUi("loginfallo.ui")

    def gui_login():
        user= login.lineEdit.text()
        contra=login.lineEdit_2.text()
        if user== "medicoAnalitico" and contra == "bio12345":
            gui_entrar()
        else:
            gui_error()
    
    def gui_entrar():
        login.hide()
        modelo = Modelo()
        modelo.cargar_imagenes()
        vista = Vista()
        controlador = Controlador(vista, modelo)
    
        vista.addControlador(controlador)
    
        vista.show()
    
    def gui_error():
        login.hide()
        error.show()
    

    def regresar_error():
        error.hide()
        login.show()
    
    login.pushButton.clicked.connect(gui_login)
    error.pushButton.clicked.connect(regresar_error)
    login.show()

    app.exec_()

main()
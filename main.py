from PyQt5.QtWidgets import QApplication
from modelo import Modelo
from vista import Vista
from controlador import Controlador

def main():
    app = QApplication([])

    modelo = Modelo()
    vista = Vista()
    controlador = Controlador(vista,modelo)

    vista.addControlador(controlador)

    vista.show()
    app.exec_()
    
main()
class Controlador:
    def __init__(self, vista,modelo):
        self.vista = vista
        self.modelo = modelo

    def img_conexion(self, index):
        self.modelo.cargar_imagenes()
        self.modelo.current_index = index
        self.modelo.crear_imagen_temporal()
        self.vista.mostrar_info()

    def obtener_info_actual(self):
        return self.modelo.obtener_info_actual()
    
    def agregarmodelo(self,m):
        self.modelo=m

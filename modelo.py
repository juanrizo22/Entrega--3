from PyQt5.QtCore import QObject
import pydicom
import os
import matplotlib.pyplot as plt

class Modelo(QObject):
    def __init__(self):
        super().__init__()
        self.carpeta = 'images'
        self.current_images = []
        self.current_index = 0

    def cargar_imagenes(self):
        self.current_images = [imagen for imagen in os.listdir(self.carpeta) if imagen.endswith('.dcm')]
        self.current_index = 0

    def obtener_info_actual(self):
        if self.current_images:
            imagen_actual = self.current_images[self.current_index]
            ds = pydicom.dcmread(os.path.join(self.carpeta, imagen_actual))
            return [
                f"Nombre del archivo: {imagen_actual}",
                f"Tipo de escaneo: {ds.Modality}",
                f"Fecha del escaneo: {ds.StudyDate}",
                f"Descripción del paciente: {ds.PatientName}",
                f"Institución: {ds.InstitutionName}"
            ]
        else:
            return ["", "", "", "", ""]

    def crear_imagen_temporal(self):
        if self.current_images:
            imagen_actual = self.current_images[self.current_index]
            ds = pydicom.dcmread(os.path.join(self.carpeta, imagen_actual))
            pixel_data = ds.pixel_array

            if len(pixel_data.shape) == 3:
                slice_index = pixel_data.shape[0] // 2
                selected_slice = pixel_data[slice_index, :, :]
                plt.imshow(selected_slice, cmap=plt.cm.bone)
            else:
                plt.imshow(pixel_data, cmap=plt.cm.bone)

            plt.axis('off')
            plt.savefig("temp_image.png")
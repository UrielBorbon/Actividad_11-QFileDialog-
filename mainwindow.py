from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from listapar import ListaPar
from particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super (MainWindow, self).__init__()

        self.listapar = ListaPar()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregarinicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.agregarfinal_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)


    @Slot()
    def action_abrir_archivo(self):
        # print('abrir_archivo')
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.listapar.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrio correctamente el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                'Error',
                'No se pudo abrir el archivo' + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self): #nos regresa la ubicacion del archivo
        # print('guardar_archivo') #referencia a la carpeta donde se ejecuta el archivo (raiz)
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.listapar.guardar(ubicacion):
            QMessageBox.information(
                self, 
                "Exito",
                "El archivo se creo correctamente" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se puedo crear el archivo" + ubicacion
            )


    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.id_lineEdit.text()
        origen_X = self.ui.origenx_spinBox.value()
        origen_Y = self.ui.origeny_spinBox.value()
        destino_X = self.ui.destinox_spinBox.value()
        destino_Y = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_X, origen_Y, destino_X, destino_Y, velocidad, red, green, blue)
        self.listapar.agregar_inicio(particula)

        #print(id, origen_X, origen_Y, destino_X, destino_Y, velocidad, red, green, blue)
       # self.ui.salida.insertPlainText(id + str(origen_X) + str(origen_Y) + str(destino_X) + str(destino_Y) + velocidad + str(red) + str(green) + str(blue))

    @Slot()
    def click_agregar_final(self):
        id = self.ui.id_lineEdit.text()
        origen_X = self.ui.origenx_spinBox.value()
        origen_Y = self.ui.origeny_spinBox.value()
        destino_X = self.ui.destinox_spinBox.value()
        destino_Y = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_X, origen_Y, destino_X, destino_Y, velocidad, red, green, blue)
        self.listapar.agregar_final(particula)
        
    
    @Slot()
    def click_mostrar(self):
       # self.listapar.mostrar()
       self.ui.salida.clear()
       self.ui.salida.insertPlainText(str(self.listapar))
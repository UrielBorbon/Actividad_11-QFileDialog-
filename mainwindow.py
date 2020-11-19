from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from listapar import ListaPar
from particula import Particula

def methodsort_by_id(Particula):
    return Particula.Id


class MainWindow(QMainWindow):

    particula = Particula()
    

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


        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.ui.ordenari_pushButton.clicked.connect(self.click_ordenari)
        self.ui.ordenarv_pushButton.clicked.connect(self.click_ordenarv)
        self.ui.ordenard_pushButton.clicked.connect(self.click_ordenard)


    @Slot()
    def click_ordenari(self):
        self.listapar.particles.sort(key= methodsort_by_id)


    @Slot()
    def click_ordenarv(self):
        self.listapar.particles.sort(key=lambda Particula: Particula.velocidad, reverse=True)



    @Slot()
    def click_ordenard(self):
        self.listapar.particles.sort(key=lambda Particula: Particula.distancia)



    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for particula in self.listapar:
            r = particula.red
            g = particula.green
            b = particula.blue
            OX = particula.origen_X
            OY = particula.origen_Y
            DX = particula.destino_X
            DY = particula.destino_Y

            color = QColor(r, g, b)
            pen.setColor(color)

            self.scene.addEllipse(OX, OY, 3, 3, pen)
            self.scene.addEllipse(DX, DY, 3, 3, pen)
            self.scene.addLine(OX+3 , OY+3, DX, DY, pen)



    @Slot()
    def limpiar(self):
        self.scene.clear()    

    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()

        encontrado = False
        for particula in self.listapar:
            if id == particula.Id:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(str(particula.Id))
                origen_X_widget = QTableWidgetItem(str(particula.origen_X))
                origen_Y_widget = QTableWidgetItem(str(particula.origen_Y))
                destino_X_widget = QTableWidgetItem(str(particula.destino_X))
                destino_Y_widget = QTableWidgetItem(str(particula.destino_Y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origen_X_widget)
                self.ui.tabla.setItem(0, 2, origen_Y_widget)
                self.ui.tabla.setItem(0, 3, destino_X_widget)
                self.ui.tabla.setItem(0, 4, destino_Y_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self, 
                "Atencion",
                f'La particula con Id "{id}" no fue encontrado'
            )
        

    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["Id", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.listapar))

        row = 0
        for particula in self.listapar:
            id_widget = QTableWidgetItem(str(particula.Id))
            origen_X_widget = QTableWidgetItem(str(particula.origen_X))
            origen_Y_widget = QTableWidgetItem(str(particula.origen_Y))
            destino_X_widget = QTableWidgetItem(str(particula.destino_X))
            destino_Y_widget = QTableWidgetItem(str(particula.destino_Y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_X_widget)
            self.ui.tabla.setItem(row, 2, origen_Y_widget)
            self.ui.tabla.setItem(row, 3, destino_X_widget)
            self.ui.tabla.setItem(row, 4, destino_Y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1



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
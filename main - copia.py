
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# Archivo de GUI Qt Designer
from Ui_MainV2 import Ui_MainWindow

# Importar las funciones
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## toggle menu 
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## Paginas
        ########################################################################

        # Pagina 1
        self.ui.Btn_Menu_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # Pagina 2
        self.ui.Btn_Menu_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # Pagina 3
        self.ui.Btn_Menu_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        self.ui.Btn_Menu_1.clicked.connect(lambda: UIFunctions.show_manos(self))
        self.ui.Btn_Menu_2.clicked.connect(lambda: UIFunctions.show_inferior(self))
        self.ui.Btn_Menu_3.clicked.connect(lambda: UIFunctions.show_cabeza(self))
        
        self.ui.pulgar.pressed.connect(lambda: UIFunctions.cambiarDedo0(self))
        self.ui.indice.pressed.connect(lambda: UIFunctions.cambiarDedo1(self))
        self.ui.medio.pressed.connect(lambda: UIFunctions.cambiarDedo2(self))
        self.ui.anular.pressed.connect(lambda: UIFunctions.cambiarDedo3(self))
        self.ui.menique.pressed.connect(lambda: UIFunctions.cambiarDedo4(self))
        
        self.ui.pulgar2.pressed.connect(lambda: UIFunctions.cambiarDedo0_2(self))
        self.ui.indice2.pressed.connect(lambda: UIFunctions.cambiarDedo1_2(self))
        self.ui.medio2.pressed.connect(lambda: UIFunctions.cambiarDedo2_2(self))
        self.ui.anular2.pressed.connect(lambda: UIFunctions.cambiarDedo3_2(self))
        self.ui.menique2.pressed.connect(lambda: UIFunctions.cambiarDedo4_2(self))
        
        self.ui.sliderdedo.valueChanged.connect(lambda: UIFunctions.mover_dedos(self,self.ui.sliderdedo.value()))
    
        self.ui.hombro.valueChanged.connect(lambda: UIFunctions.mover_hombro(self,self.ui.hombro.value()))
        self.ui.codo.valueChanged.connect(lambda: UIFunctions.mover_codo(self,self.ui.codo.value()))

        self.ui.cuello.valueChanged.connect(lambda: UIFunctions.mover_cuello(self,self.ui.cuello.value()))
        self.ui.ojos.valueChanged.connect(lambda: UIFunctions.mover_ojos(self,self.ui.ojos.value()))

        ## Mostrar la pagina principal
        ########################################################################
        self.show()
        ## FINAL ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
    
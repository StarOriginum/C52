import sys 

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, 
                                QScrollBar, QHBoxLayout, QWidget)
from PySide6.QtGui import QIcon, QPixmap, QColor


#QMainWindow est un QWidget

# Un Widget peut posséder d'autres Widgets
# Losange noir veut dire compososition
# Un Widget peut contenir n Widget
class ColorPickerApplication(QMainWindow):
    
    
 
    def __init__(self):
        # L'appel de super() doit être explicite et non implicite comme dans d'autre langage de prog
        # Pas optionel
        super().__init__(None)
        
        
        
        self.setWindowTitle("Color picker")
        self.setWindowIcon(QIcon('Contexte-Projet0/color_picker_icon.jpg'))
        
        fixed_widget_width = 50
        
        self.__red_color = QLabel()
        red_title = QLabel()
        self.__red_control = QScrollBar()
        red_value = QLabel()
        self.__red_image = QLabel()
        # Creer des valeurs membres est aussi utilse dépendant la situation
        
        red_title.setText('Red')
        red_title.setFixedWidth(fixed_widget_width)
        self.__red_control.setRange(0, 255)
        self.__red_control.setValue(0)
        self.__red_control.setOrientation(Qt.Horizontal)
        red_value.setNum(self.__red_control.value())
        red_value.setAlignment(Qt.AlignCenter)
        
        
        self.__red_color.setFixedWidth(fixed_widget_width)
        
        self.__red_control.valueChanged.connect(red_value.setNum)
        self.__red_control.valueChanged.connect(self.update_red)
        
        self.__red_layout = QHBoxLayout()
        self.__red_layout.addWidget(red_title)
        self.__red_layout.addWidget(self.__red_control)
        self.__red_layout.addWidget(red_value)
        self.__red_layout.addWidget(self.__red_image)
        self.__red_layout.addWidget(self.__red_color)
        
        self.__central_widget = QWidget()
        self.__central_widget.setLayout(self.__red_layout)
        
        self.setCentralWidget(self.__central_widget)
    
    @Slot()    
    def update_red(self):
        image = QPixmap(self.__red_color.size())
        image.fill(QColor(self.__red_control.value(), 0, 0))
        self.__red_color.setPixmap(image)
        

# Concept: Signaux et slots(connexions)
def main():
    app = QApplication(sys.argv)
    
    window = ColorPickerApplication()
    window.show()
    
    # retourne si l'application s'est bien déroulé. Si 0, bon déroulement. Sinon, erreur
    sys.exit(app.exec())

if __name__ == '__main__':
    main()




from GameoFlIFE import GOLEngine
import sys

from PySide6.QtCore import Qt, Slot,QTimer
from PySide6.QtWidgets import ( QApplication, QMainWindow, 
                                QWidget, QLabel, QPushButton,
                                QBoxLayout 
                                )
from PySide6.QtGui import QIcon,QPainter,QImage,QColor, QPixmap



class GolApp(QMainWindow, QPushButton):
    
    def __init__(self):
        super().__init__(None)
        self.setWindowTitle('GolApp')
        self.__height = 250
        self.__width = 200


        self.__simulation_running = True
        self.__app_view = QLabel()


        self.__generations = 0
        self.__alive = 0
        self.__dead = 0

        self.__generations_label = QLabel(f"Generation: {self.__generations}", self)
        self.__alive_label = QLabel(f"Cells vivantes: {self.__alive}", self)
        self.__dead_label = QLabel(f"Cells mortes: {self.__dead}", self)
        self.__alive_percent_label = QLabel(f"Pourcentage vivantes: ", self)
        self.__dead_percent_label = QLabel(f"Pourcentage mortes: ", self)

        self.__stats_layout = QBoxLayout(QBoxLayout.BottomToTop)
        self.__stats_layout.addWidget(self.__generations_label)
        self.__stats_layout.addWidget(self.__alive_label)
        self.__stats_layout.addWidget(self.__dead_label)
        self.__stats_layout.addWidget(self.__alive_percent_label)
        self.__stats_layout.addWidget(self.__dead_percent_label)

        self.__stats_widget = QWidget(self)
        self.__stats_widget.setLayout(self.__stats_layout)
        

        self.__simulation_button = QPushButton("Stop")
        self.__simulation_button.clicked.connect(self.toggle_simulation)

        self.__button_layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.__button_layout.addWidget(self.__simulation_button)
        self.__button_layout.addWidget(self.__app_view)

       


        self.__main_layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.__main_layout.addWidget(self.__simulation_button)
        self.__main_layout.addWidget(self.__app_view)
        self.__main_layout.addWidget(self.__stats_widget)
        
        self.__central_widget = QWidget()
        self.__central_widget.setLayout(self.__main_layout)
        self.setCentralWidget(self.__central_widget)

        self.__gol = GOLEngine(self.__height, self.__width)
        self.__gol.randomize()
        self.__cell_size = 1
        
        
        self.__app_view.setAlignment(Qt.AlignCenter)
        
        self.__image = QImage(self.__gol.width, self.__gol.height, QImage.Format_RGB32)
        
        self.__painter = QPainter()
        #timeout implémenté plus tard
        #timer.timeout.connect
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.__tick)
        self.__timer.start(100)


        
    @Slot()
    def __tick(self):
        self.__gol.process()

        self.updateImage()
        
        
     
    def updateImage(self):
        for y in range(self.__gol.height):
            for x in range(self.__gol.width):
                if self.__gol.get_cell_value(x, y) == 1:
                    color = QColor(255, 255, 255)  # Alive cell: white
                else:
                    color = QColor(0, 0, 0)    # Dead cell: black
                for i in range(self.__cell_size):
                    for j in range(self.__cell_size):
                        self.__image.setPixelColor(x * self.__cell_size + i, 
                                                 y * self.__cell_size + j, 
                                                 color)
        
        pixmap = QPixmap.fromImage(self.__image)
        self.update_stats()
        self.__app_view.setPixmap(pixmap)

    def toggle_simulation(self):
        if self.__simulation_running:
            self.__timer.stop()
            self.__simulation_button.setText("Start")
        else:
            self.__timer.start(100)
            self.__simulation_button.setText("Start")
        
        self.__simulation_running = not self.__simulation_running
    
    def update_stats(self):

        self.__generations += 1

        self.__alive = sum(sum(row) for row in self.__gol.get_grid)
        self.__dead = (self.__gol.width * self.__gol.height) - self.__alive

        self.__total_cells = self.__gol.width * self.__gol.height
        self.__alive_percent = (self.__alive / self.__total_cells) * 100
        self.__dead_percent =  (self.__dead / self.__total_cells) * 100


        #Mise a jour des informations
        if self.__generations_label is not None:
            self.__generations_label.setText(f"Generation: {self.__generations}")
        if self.__alive_label is not None:
            self.__alive_label.setText(f"Alive Cells: {self.__alive}")
        if self.__dead_label is not None:
            self.__dead_label.setText(f"Dead Cells: {self.__dead}")
        if self.__alive_percent_label is not None:
            self.__alive_percent_label.setText(f"Alive Percentage: {self.__alive_percent:.2f}%")
        if self.__dead_percent_label is not None:
            self.__alive_percent_label.setText(f"Dead Percentage: {self.__dead_percent:.2f}%")

    def resize_event(self, event):

        self.__new_width = self.__app_view.width()
        self.__new_height = self.__app_view.height()

        self.__cell_size = min(self.__new_width // self.__gol.width, self.__new_height // self.__gol.height)

        self.__image = QImage(self.__gol.width, self.__gol.height, QImage.Format_RGB3)

        self.updateImage()
        
        
def main():
    app = QApplication(sys.argv)
    window = GolApp()
    window.show()
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()        
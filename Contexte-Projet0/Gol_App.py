
# from GameoFlIFE import GOLEngine
from gol_engine_02 import GOLEngine
import sys

from PySide6.QtCore import Qt, Slot,QTimer, Signal
from PySide6.QtWidgets import ( QApplication, QMainWindow, 
                                QWidget, QLabel, QPushButton,
                                QBoxLayout, QGroupBox, QVBoxLayout,
                                QScrollBar 
                                )
from PySide6.QtGui import QIcon,QPainter,QImage,QColor, QPixmap

from __feature__ import snake_case, true_property



class QInformationPanel(QWidget):
    def __init__(self, parent = None, gol_apps = None, gol_eng = None):
        super().__init__(None)
        
        self.__gol_app = gol_apps
        self.__gol_engine = gol_eng
        self.__generations = 0
        self.__alive = 0
        self.__dead = 0

        self.__generations_label = QLabel(f"Generation: {self.__generations}", self)
        self.__alive_label = QLabel(f"Cells vivantes: {self.__alive}", self)
        self.__dead_label = QLabel(f"Cells mortes: {self.__dead}", self)
        self.__alive_percent_label = QLabel(f"Pourcentage vivantes: ", self)
        self.__dead_percent_label = QLabel(f"Pourcentage mortes: ", self)

        self.__stats_layout = QBoxLayout(QBoxLayout.BottomToTop)
        self.__stats_layout.add_widget(self.__generations_label)
        self.__stats_layout.add_widget(self.__alive_label)
        self.__stats_layout.add_widget(self.__dead_label)
        self.__stats_layout.add_widget(self.__alive_percent_label)
        self.__stats_layout.add_widget(self.__dead_percent_label)
        
        self.set_layout(self.__stats_layout)
        
    def update_stats(self):

        self.__generations += 1
        
        
        self.__alive = sum(sum(row) for row in self.__gol_engine.get_grid())
        self.__dead = (self.__gol_engine.width * self.__gol_engine.height) - self.__alive

        self.__total_cells = self.__gol_engine.width * self.__gol_engine.height
        self.__alive_percent = (self.__alive / self.__total_cells) * 100
        self.__dead_percent =  (self.__dead / self.__total_cells) * 100


        # Mise a jour des informations
        
        self.__generations_label.text = f"Generation: {self.__generations}"

        self.__alive_label.text = f"Alive Cells: {self.__alive}"

        self.__dead_label.text = f"Dead Cells: {self.__dead}"

        self.__alive_percent_label.text = f"Alive Percentage: {self.__alive_percent:.2f}%"

        self.__dead_percent_label.text = f"Dead Percentage: {self.__dead_percent:.2f}%"

class QSimulationView(QWidget):
    def __init__(self, parent = None):
        super().__init__(None)
        
    
class QControlPanels(QWidget):
    def __init__(self, parent = None):
        super().__init__(None)
        
        self.__start_pause_button = QPushButton("Start")
        self.__start_pause_button.clicked.connect(self.toggle_simulation)
        
        self.__step_button = QPushButton("Step")
        self.__step_button.clicked.connect(self.step_simulation)
        
        self.__speed_scrollbar = QScrollBar(Qt.Horizontal)
        self.__speed_scrollbar.valueChanged.connect(self.change_simulation_speed)
        
        self.__controls_layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.__controls_layout.add_widget(self.__start_pause_button)
        self.__controls_layout.add_widget(self.__step_button)
        self.__controls_layout.add_widget(self.__speed_scrollbar)
        
        self.set_layout(self.__controls_layout)
        
    def toggle_simulation(self):
        self.toggle_simulation_signal.emit(self.__start_pause_button)
    
    def step_simulation(self):
        self.step_simulation_signal.emit(self.__step_button)
        
    def change_simulation_speed(self):
        self.speed_changed_signal.emit(self.__speed_scrollbar)
        
        
        
        
        
    

class GolApp(QMainWindow):
    
    toggled = Signal(QPushButton)
    started = Signal(QPushButton)
    stopped = Signal(QPushButton)
    speedChanged = Signal(QScrollBar)
    
    def __init__(self):
        super().__init__(None)
        self.set_window_title('GolApp')
        self.__height = 250
        self.__width = 200
       
        
        
        self.__gol = GOLEngine(self.__height, self.__width)
        self.__gol.randomize()
        
        self.__info_panel = QInformationPanel(gol_apps=self, gol_eng=self.__gol)
        self.__control_panel = QControlPanels()


        self.__simulation_running = True
        self.__app_view = QLabel()
        self.__right_box = QGroupBox("Stats")
        self.__right_box.set_layout(QVBoxLayout(QBoxLayout.BottomToTop))
        self.__right_box.layout().add_widget(self.__info_panel)
        # self.__stats_widget = QWidget(self)
        # self.__stats_widget.set_layout()
        self.__right_layout = QVBoxLayout()
        self.__right_layout.add_widget(self.__right_box)
        
        self.__left_top_box = QGroupBox("Controls")
        self.__left_top_box.set_layout(QVBoxLayout())
        self.__left_top_box.layout().add_widget(self.__button_panel)
        
        self.__left_layout = QVBoxLayout(QBoxLayout.TopToBottom)
        self.__left_layout.add_widget(self.__left_top_box)

        self.__control_panel.toggle_simulation_signal.connect(self.toggle_simulation)
        self.__control_panel.step_simulation_signal.connect(self.step_simulation)
        self.__control_panel.speed_changed_signal.connect(self.change_simulation_speed)

        self.__main_layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.__main_layout.add_widget(self.__simulation_button)
        self.__main_layout.add_widget(self.__app_view)
        self.__main_layout.add_layout(self.__right_layout)
        
        self.__central_widget = QWidget()
        self.__central_widget.set_layout(self.__main_layout)
        self.set_central_widget(self.__central_widget)

              
        
        self.__app_view.alignment = Qt.AlignCenter
        
        self.__image = QImage(self.__gol.width, self.__gol.height, QImage.Format.Format_RGB32)
    
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
                if self.__gol.cell_value(x, y) == 1:
                    color = QColor(255, 255, 255)  # Alive cell: white
                else:
                    color = QColor(0, 0, 0)    # Dead cell: black
                
                self.__image.set_pixel_color(x,
                                        y,
                                        color)
        pixmap = QPixmap.from_image(self.__image)
        
        self.__app_view.pixmap = pixmap
        self.__info_panel.update_stats()
     
    @Slot    
    def toggle_simulation(self):
        if self.__simulation_running:
            self.__timer.stop()
            self.__simulation_button.text = "Start"
        else:
            self.__timer.start(100)
            self.__simulation_button.text = "Start"
        
        self.__simulation_running = not self.__simulation_running

    def resize_event(self, event):

        self.__new_width = self.__app_view.width
        self.__new_height = self.__app_view.height

        self.__image = QImage(self.__gol.width, self.__gol.height, QImage.Format.Format_RGB32)

        self.updateImage()
        
        
def main():
    app = QApplication(sys.argv)
    window = GolApp()
    window.show()
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()        
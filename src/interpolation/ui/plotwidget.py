import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
import numpy as np


class PlotWidget(QWidget):
    def __init__(self, parent=None):
        super(PlotWidget, self).__init__(parent)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.build)
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def build(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        x = np.arange(0, 5, 0.1)
        y = np.sin(x)
        ax.plot(x, y)
        self.canvas.draw()

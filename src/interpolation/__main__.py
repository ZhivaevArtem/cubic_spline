from PyQt5.QtCore import QRunnable, QThread

from .ui.mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets
import matplotlib as plt


plt.use('QT5Agg')


def build_plot():
    import numpy as np
    from numpy import (sin, sinh, arcsin, arcsinh,
                       cos, cosh, arccos, arccosh,
                       tan, tanh, arctan, arctanh, arctan2,
                       degrees, radians, deg2rad, rad2deg,
                       round, floor, ceil,
                       exp, expm1, exp2, log, log10, log1p, logaddexp, logaddexp2,
                       power, mod,
                       sqrt, cbrt, square, absolute, sign, maximum, minimum, fmax, fmin)
    formula = ui.lineEdit_formula.text()
    x = np.arange(float(ui.lineEdit_xmin.text()),
                  float(ui.lineEdit_xmax.text()),
                  float(ui.lineEdit_xdpi.text()))
    y = eval(formula)
    ui.widget_plot.build(x, y)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    global ui
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_buildPlot.clicked.connect(build_plot)
    MainWindow.show()
    sys.exit(app.exec_())

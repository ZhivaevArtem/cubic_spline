from PyQt5.QtCore import QRunnable, QThread

from .ui.mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets
import matplotlib as plt
from .spline import build_cubic_spline


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
    xmin = float(ui.lineEdit_xmin.text())
    xmax = float(ui.lineEdit_xmax.text())
    xstep = float(ui.lineEdit_xstep.text())
    s1 = float(ui.lineEdit_s1.text())
    s2 = float(ui.lineEdit_s2.text())

    x = np.arange(xmin, xmax + xstep, xstep)
    x1 = x[:]
    y1 = eval(formula)
    print(x1)
    print(y1)
    ui.widget_plot.build(x1, y1)

    cubic_spline = build_cubic_spline(x1, y1, (s1, s2))

    xdpi = (cubic_spline.x_consts[-1] - cubic_spline.x_consts[0]) / 100
    x2 = np.arange(cubic_spline.x_consts[0], cubic_spline.x_consts[-1] + xdpi, xdpi)
    y2 = cubic_spline.calculate_all(x2)

    ui.widget_plot.clear()
    ui.widget_plot.build(x2, y2)


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

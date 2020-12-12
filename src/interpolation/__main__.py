from .ui import Ui_MainWindow
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
    xmin = eval(ui.lineEdit_xmin.text())
    xmax = eval(ui.lineEdit_xmax.text())
    xstep = eval(ui.lineEdit_xstep.text())
    s1 = eval(ui.lineEdit_s1.text())
    s2 = eval(ui.lineEdit_s2.text())

    pieces = 500

    xdpi = (xmax - xmin) / pieces
    x = np.arange(xmin, xmax + xstep, xstep)
    x1 = x[:]
    y1 = eval(formula)
    print(x1)
    print(y1)

    x = np.arange(xmin, xmax + xdpi, xdpi)
    x3 = x
    y3 = eval(formula)

    # ui.widget_plot.build(x1, y1)

    cubic_spline = build_cubic_spline(x1, y1, (s1, s2))

    x2 = x
    y2 = cubic_spline.calculate_all(x2)

    max_difference = 0
    md_x = 0
    for i in range(len(x)):
        if absolute(y2[i] - y3[i]) > max_difference:
            max_difference = absolute(y2[i] - y3[i])
            md_x = x[i]

    ui.label_maxDifference.setText(f'max difference: {max_difference} (x = {md_x})')

    print(f'max difference: {max_difference}')
    ui.widget_plot.clear()
    ui.widget_plot.build(x2, y2)
    ui.widget_plot.build(x3, y3)


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

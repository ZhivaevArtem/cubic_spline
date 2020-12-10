from .ui.mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets
import matplotlib as plt

plt.use('QT5Agg')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

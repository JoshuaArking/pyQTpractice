import PySide2, sys
from PySide2 import QtCore, QtWidgets, QtGui
import my_widget


def print_version():
    print("QT for Python Version " + PySide2.__version__ + "Compiled with QT " + PySide2.QtCore.__version__)


if __name__ == '__main__':
    print_version()
    app = QtWidgets.QApplication([])

    widget = my_widget.MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())



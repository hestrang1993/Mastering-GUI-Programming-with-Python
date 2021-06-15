"""
:mod:`Chapter01.my_qt_template`

This module contains the template for future applications I will make.
"""

import sys

from PyQt5 import QtWidgets as qtw


# from PyQt5 import QtGui as qtg
# from PyQt5 import QtCore as qtc

class MainWindow(qtw.QWidget):
    """
    The :class:`MainWindow` class will serve as the template for all future applications I write.
    """

    def __init__(self):
        """
        Create a new :class:`MainWindow` instance.
        """
        super().__init__()
        # Main UI code goes here

        # End main UI code
        self.show()


# It is required to save a reference to MainWindow.
# If it goes out of scope, it will be destroyed.
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())

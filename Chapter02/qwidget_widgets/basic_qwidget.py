"""
:mod:`Chapter02.qtwidget_widgets.basic_qwidget`

This module an example of several different simple widgets.
"""

import sys

# from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """
    The :class:`MainWindow` class will serve as the template for all future applications I write.
    """

    def __init__(self):
        """
        Create a new :class:`MainWindow` instance.
        """
        super().__init__()
        # Top level window
        tool_tip_string = "This is my widget"
        """
        str: The string I want to use for the tool tip of this subwidget.
        """
        cursor_property = qtc.Qt.ArrowCursor
        """
        PyQt5.QtCore.Qt.ArrowCursor: A CursorShape that tells the application to make the cursor look like an arrow 
        when I hover over the application.
        """
        subwidget = qtw.QWidget(
                self,
                toolTip = tool_tip_string,
                cursor = cursor_property
        )
        """
        PyQt5.QtWidgets.QWidget: A simple widget within another widget.
        
        The ``self`` argument is passed as an argument to ensure that the subwidget only functions within a running 
        parent widget.
        """
        sheet_attribute = qtc.Qt.Sheet
        """
        PyQt5.QtCore.Qt.Sheet: An attribute that tells the program to treat the window like a sheet.
        """
        popup_attribute = qtc.Qt.Popup
        """
        PyQt5.QtCore.Qt.Sheet: An attribute that tells the program to treat the window like a popup.
        """
        subwidget.setWindowFlags(sheet_attribute | popup_attribute)

        # Label
        label_string = '<b>Hello Widgets!</b>'
        """
        str: The string I want the label to display.
        """
        margin_size = 10
        """
        int: The size of the margins I want to use for my label.
        """
        label = qtw.QLabel(
                label_string,
                self,
                margin = margin_size
        )
        self.show()


# It is required to save a reference to MainWindow.
# If it goes out of scope, it will be destroyed.
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())

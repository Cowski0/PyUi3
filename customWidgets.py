from PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qframelesswindow import TitleBar


class QTitleBar(TitleBar):
    """ Custom title bar """

    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet('background-color:transparent')
        self.label = QLabel('PyUi3', self)
        self.label.setStyleSheet("QLabel{color:white;font: 13px 'Segoe UI'; margin: 10px}")
        self.label.adjustSize()

class QToggleButton(QPushButton):
    def __init__(self, text, parent):
        super().__init__(parent)
        self.setCheckable(True)
        self.setText(text)
        self.setStyleSheet("""
            QPushButton{background-color:#2D2D2D;border-radius:6;color:white;font: 13px 'Segoe UI';border:1px solid #313131}
            QPushButton::hover{background-color:#323232;color:white;font: 13px 'Segoe UI';}
            QPushButton::checked{background-color:#4CC2FF;color:black;font: 13px 'Segoe UI';}
            """)

class QAccentButton(QPushButton):
    def __init__(self, text, parent):
        super().__init__(parent)
        self.setStyleSheet()

class QHomeStack(QStackedWidget):
    def __init__(self, parent):
        super().__init__(parent)        
        self.setStyleSheet("background-color:rgba(255,255,255,10);border-radius:5;border:1px solid #1D1D1D")
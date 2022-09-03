import sys

from PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from qframelesswindow import AcrylicWindow
from customWidgets import QTitleBar, QToggleButton, QAccentButton, QHomeStack

class Window(AcrylicWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(700,700)
        self.setTitleBar(QTitleBar(self))
        self.windowEffect.setMicaEffect(self.winId(), True)
        self.titleBar.raise_()
        self.installEventFilter(self)

        self.main = QHomeStack(self)
        self.homepage = QWidget()

        self.sidebar = QFrame(self)


        self.label = QLabel(self.homepage)
        self.label.setStyleSheet("QLabel{color:rgba(255,255,255,170);font: 15px 'Segoe UI'; margin: 5px;border:none;background-color:rgba(0,0,0,0)}")
        self.label.setText("Windows 11")
        self.label.setGeometry(int((self.width()/2)-50), int((self.height()/2)-50), 100,50)
        self.togbtn = QToggleButton("toggle Button",self.homepage)
        self.togbtn.setGeometry(20, 20,100,40)

        self.main.addWidget(self.homepage)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Resize:


            if self.width() > 807:
                self.sidebar.setGeometry(0,48, 291, self.height()-48)
                self.main.setGeometry(291, 48, self.width()-291, self.height()-48)
                self.label.setGeometry(int((self.width()/2)/1.5), int((self.height()/2)-50), 100,50)

            else:
                self.sidebar.setGeometry(0,48, 0, self.height()-48)
                self.label.setGeometry(int((self.width()/2)-50), int((self.height()/2)-50), 100,50)
                self.main.setGeometry(0, 48, self.width(), self.height()-48)


        return super(Window, self).eventFilter(obj, event)


if __name__ == "__main__":
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    # run app
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()
    sys.exit(app.exec_())
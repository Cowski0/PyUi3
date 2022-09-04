from PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qframelesswindow import TitleBar, AcrylicWindow
from winreg import *
from PyUi3 import DARKTHEME

def no_sup():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle("This version of windows 11 is not supported yet.")
    msg.setText("This beta version of windows breaks the window.")
    msg.exec_()


class FWindow(AcrylicWindow):
    def __init__(self,parent):
        super().__init__(parent)
        #get win version
        key = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows NT\CurrentVersion')
        value = QueryValueEx(key,"DisplayVersion")
        if value[0] == "22H2":
            no_sup()
            exit()
        self.installEventFilter(self)
    
        self.main = QFrame(self)
        self.main.setStyleSheet(DARKTHEME)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Resize:
            self.main.setGeometry(0,0,self.width(), self.height())


        return super(FWindow, self).eventFilter(obj, event)


class FTitleBar(TitleBar):

    def __init__(self, parent):
        super().__init__(parent)
        self.label = QLabel('PyUi3', self)
        self.label.setStyleSheet("QLabel{color:white;font: 13px 'Segoe UI'; margin: 10px}")
        self.label.adjustSize()

class FToggleButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(parent=None)
        self.setCheckable(True)
        self.setText(text)
        self.setStyleSheet("""
            QPushButton{background-color:#2D2D2D;border-radius:6;color:white;font: 13px 'Segoe UI';border:1px solid #313131}
            QPushButton::hover{background-color:#323232;color:white;font: 13px 'Segoe UI';}
            QPushButton::checked{background-color:#4CC2FF;color:black;font: 13px 'Segoe UI';}
            """)

class FAccentButton(QPushButton):
    def __init__(self, text, parent):
        super().__init__(parent)
        self.setText(text)
        self.setStyleSheet("""
            QPushButton{background-color:#2D2D2D;border-radius:6;color:white;font: 13px 'Segoe UI';border:1px solid #313131;}
            QPushButton::hover{background-color:#323232;color:white;font: 13px 'Segoe UI';}
            QPushButton::pressed{background-color:#4CC2FF;color:black;font: 13px 'Segoe UI';}
            """)


class FHomeStack(QStackedWidget):
    def __init__(self, parent):
        super().__init__(parent)        
        self.setStyleSheet(DARKTHEME)


class FPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet(DARKTHEME)



#simply a test widget for example, not for standard use, as its bad.
class FShowCase(QFrame):
    def __init__(self,title,widget,parent,min_size):
        super().__init__(parent)
        layout = QVBoxLayout()
        head = QLabel(title)
        self.setMinimumSize(100,30)
        self.setStyleSheet("QFrame{background-color:transparent;border:none}")
        head.setStyleSheet("QLabel{color:rgba(255,255,255,170);font: 15px 'Segoe UI'; margin: 2px;border:none;background-color:rgba(0,0,0,0)}")

        item_frame = QWidget()

        item = QVBoxLayout()
        item_frame.setMinimumSize(min_size)
        self.setMinimumSize(min_size)

        item.setContentsMargins(10,3,3,3)
        self.setContentsMargins(0,0,0,0)
        item_frame.setStyleSheet("background-color:#202020")
        item.addWidget(widget)
        item_frame.setLayout(item)
        layout.addWidget(head)
        layout.addWidget(item_frame)
        self.setLayout(layout)


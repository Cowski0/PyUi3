import sys

from PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyUi3.FWidgets import FTitleBar, FToggleButton, FAccentButton, FHomeStack, FShowCase, FWindow, FPage

class home_page(FPage):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.installEventFilter(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        spacerItem = QtWidgets.QSpacerItem(20, 222, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel("Windows 11",self.frame)
        self.label.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(332, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton("Start",self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(120, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(332, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 222, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addWidget(self.frame)





class Window(FWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(700,700)
        self.setTitleBar(FTitleBar(self.main))
        self.installEventFilter(self)

        self.stack = FHomeStack(self.main)
        self.homepage = home_page()
        self.sidebar = QFrame(self.main)

        self.buttonpage = FPage(self.main)

        toggle = QSlider(Qt.Orientation.Horizontal, self.buttonpage)
        toggle.setFixedSize(111,31)
        self.buttonshowcase = FShowCase(title="Toggle Button",widget=toggle,min_size=QSize(130,50),parent=self.buttonpage)

        self.stack.addWidget(self.homepage)
        self.stack.addWidget(self.buttonpage)


    def eventFilter(self, obj, event):
        if event.type() == QEvent.Resize:


            if self.width() > 807:
                self.sidebar.setGeometry(0,48, 291, self.height()-48)
                self.stack.setGeometry(291, 48, self.width()-291, self.height()-48)

            else:
                self.sidebar.setGeometry(0,48, 0, self.height()-48)
                self.stack.setGeometry(0, 48, self.width(), self.height()-48)

            self.buttonshowcase.setGeometry(20,20, self.main.width()-40, 100)

        return super(Window, self).eventFilter(obj, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()
    sys.exit(app.exec_())